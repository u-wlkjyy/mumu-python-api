#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/30 下午3:06
# @Author : wlkjyy
# @File : gui.py
# @Software: PyCharm
import copy
import json
import time

import cv2
import numpy
import collections
from adbutils import adb
import threading
import mumu.config as config


class Gui:

    def __init__(self, utils):
        self.utils = utils

    def __connect(self):
        """
            获取可用的连接
        :return:
        """

        self.utils.set_operate("adb")
        ret_code, retval = self.utils.run_command([''])
        if ret_code != 0:
            return self

        try:
            data = json.loads(retval)
        except json.JSONDecodeError:
            return None, None

        for key, value in data.items():
            if key == "adb_host" and "adb_port" in data:
                yield data["adb_host"], data["adb_port"], self.utils.get_vm_id()
                return

            if 'errcode' in value:
                continue
            else:
                # connect_list.append((value.get("adb_host"), value.get("adb_port")))
                yield value.get("adb_host"), value.get("adb_port"), key

        return

    def __vm_handle_frame(self, handle, vm_id):
        while True:
            if vm_id in config.FRAME_CACHE:

                while True:
                    frame = config.FRAME_CACHE[vm_id]

                    if frame is not None:
                        handle(frame, self.utils.get_mumu_root_object().select(vm_id))
                        time.sleep(0.01)

            else:
                continue

    def create_handle(self, handle_func):
        """
            创建帧处理函数
        :param handle_func:
        :return:
        """
        try:
            import scrcpy
        except:
            raise RuntimeError(
                "scrcpy is not installed, please install it first by running 'pip install scrcpy-client'")

        client_list = []

        for (k, v, id) in self.__connect():
            host = str(k) + ":" + str(v)
            adb.connect(host)
            for i in adb.device_list():
                if i.serial == host:
                    client = scrcpy.Client(device=i)

                    threading.Thread(target=self.__vm_handle_frame, args=(handle_func, id)).start()

                    def func(vm_id):
                        def save_frame(frame):
                            config.FRAME_CACHE[vm_id] = frame
                            return

                        return save_frame

                    client.add_listener(scrcpy.EVENT_FRAME, func(id))
                    client_list.append(client)
        for cli_row in client_list:
            cli_row.start(threaded=True, daemon_threaded=True)

    def locateOnScreen(self, haystack_frame, needle_image, confidence=0.8, grayscale=None):
        """
            在屏幕上查找图片
        :param haystack_frame: 屏幕帧
        :param needle_image: 图片
        :param confidence: 置信度
        :param grayscale: 灰度值找图
        :return:
        """
        needle_image = _load_cv2(needle_image)
        haystack_frame = _load_cv2(haystack_frame)

        for r in _locateAll_opencv(needle_image, haystack_frame, confidence=confidence, grayscale=None):
            return r

        return False

    def center(self, box):
        """
            获取中心点
        :param box: Box
        :return:
        """
        return int(box.left + box.width / 2), int(box.top + box.height / 2)

    def locateCenterOnScreen(self, haystack_frame, needle_image, confidence=0.8, grayscale=None):
        """
            在屏幕上查找图片
        :param haystack_frame: 屏幕帧
        :param needle_image: 图片
        :param confidence: 置信度
        :param grayscale: 灰度值找图
        :return:
        """
        needle_image = _load_cv2(needle_image)
        haystack_frame = _load_cv2(haystack_frame)

        for r in _locateAll_opencv(needle_image, haystack_frame, confidence=confidence, grayscale=None):
            return self.center(r)

        return False

    def locateAllOnScreen(self, haystack_frame, needle_image, confidence=0.8, grayscale=None):
        """
            在屏幕上查找所有图片
        :param haystack_frame: 屏幕帧
        :param needle_image: 图片
        :param confidence: 置信度
        :param grayscale: 灰度值找图
        :return:
        """
        arr = []
        needle_image = _load_cv2(needle_image)
        haystack_frame = _load_cv2(haystack_frame)

        for r in _locateAll_opencv(needle_image, haystack_frame, confidence=confidence, grayscale=None):
            arr.append(r)

        return arr



    def save(self, frame, path):
        """
            保存帧
        :param path: 路径
        :return:
        """
        cv2.imwrite(path, frame)


GRAYSCALE_DEFAULT = True
USE_IMAGE_NOT_FOUND_EXCEPTION = True
Box = collections.namedtuple('Box', 'left top width height')


def _load_cv2(img, grayscale=None):
    """
    TODO
    """
    # load images if given filename, or convert as needed to opencv
    # Alpha layer just causes failures at this point, so flatten to RGB.
    # RGBA: load with -1 * cv2.CV_LOAD_IMAGE_COLOR to preserve alpha
    # to matchTemplate, need template and image to be the same wrt having alpha

    if grayscale is None:
        grayscale = GRAYSCALE_DEFAULT
    if isinstance(img, str):
        # The function imread loads an image from the specified file and
        # returns it. If the image cannot be read (because of missing
        # file, improper permissions, unsupported or invalid format),
        # the function returns an empty matrix
        # http://docs.opencv.org/3.0-beta/modules/imgcodecs/doc/reading_and_writing_images.html
        if grayscale:
            img_cv = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
        else:
            img_cv = cv2.imread(img, cv2.IMREAD_COLOR)
        if img_cv is None:
            raise IOError(
                "Failed to read %s because file is missing, "
                "has improper permissions, or is an "
                "unsupported or invalid format" % img
            )
    elif isinstance(img, numpy.ndarray):
        # don't try to convert an already-gray image to gray
        if grayscale and len(img.shape) == 3:  # and img.shape[2] == 3:
            img_cv = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            img_cv = img
    elif hasattr(img, 'convert'):
        # assume its a PIL.Image, convert to cv format
        img_array = numpy.array(img.convert('RGB'))
        img_cv = img_array[:, :, ::-1].copy()  # -1 does RGB -> BGR
        if grayscale:
            img_cv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    else:
        raise TypeError('expected an image filename, OpenCV numpy array, or PIL image')
    return img_cv


def _locateAll_opencv(needleImage, haystackImage, grayscale=None, limit=10000, region=None, step=1, confidence=0.999):
    """
    TODO - rewrite this
        faster but more memory-intensive than pure python
        step 2 skips every other row and column = ~3x faster but prone to miss;
            to compensate, the algorithm automatically reduces the confidence
            threshold by 5% (which helps but will not avoid all misses).
        limitations:
          - OpenCV 3.x & python 3.x not tested
          - RGBA images are treated as RBG (ignores alpha channel)
    """
    if grayscale is None:
        grayscale = GRAYSCALE_DEFAULT

    confidence = float(confidence)

    needleImage = _load_cv2(needleImage, grayscale)
    needleHeight, needleWidth = needleImage.shape[:2]
    haystackImage = _load_cv2(haystackImage, grayscale)

    if region:
        haystackImage = haystackImage[region[1]: region[1] + region[3], region[0]: region[0] + region[2]]
    else:
        region = (0, 0)  # full image; these values used in the yield statement
    if haystackImage.shape[0] < needleImage.shape[0] or haystackImage.shape[1] < needleImage.shape[1]:
        # avoid semi-cryptic OpenCV error below if bad size
        raise ValueError('needle dimension(s) exceed the haystack image or region dimensions')

    if step == 2:
        confidence *= 0.95
        needleImage = needleImage[::step, ::step]
        haystackImage = haystackImage[::step, ::step]
    else:
        step = 1

    # get all matches at once, credit: https://stackoverflow.com/questions/7670112/finding-a-subimage-inside-a-numpy-image/9253805#9253805
    result = cv2.matchTemplate(haystackImage, needleImage, cv2.TM_CCOEFF_NORMED)
    match_indices = numpy.arange(result.size)[(result > confidence).flatten()]
    matches = numpy.unravel_index(match_indices[:limit], result.shape)

    if len(matches[0]) == 0:
        if USE_IMAGE_NOT_FOUND_EXCEPTION:
            # raise ImageNotFoundException('Could not locate the image (highest confidence = %.3f)' % result.max())
            # print('Could not locate the image (highest confidence = %.3f)' % result.max())
            return
        else:
            return

    # use a generator for API consistency:
    matchx = matches[1] * step + region[0]  # vectorized
    matchy = matches[0] * step + region[1]
    for x, y in zip(matchx, matchy):
        yield Box(x, y, needleWidth, needleHeight)
