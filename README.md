# Mumu模拟器Python API

- [Mumu模拟器Python API](#mumu模拟器python-api)
    - [项目介绍](#项目介绍)
    - [如何使用？](#如何使用)
        - [设置MuMuManager路径](#设置mumumanager路径)
        - [模拟器索引说明](#模拟器索引说明)
        - [选择模拟器](#选择模拟器)
        - [举个例子](#举个例子)
        - [注意](#注意)
    - [API类](#api类)
        - [驱动类（driver）](#驱动类driver)
            - [网络桥接驱动（bride）](#网络桥接驱动bride)
                - [安装桥接驱动（install）](#安装桥接驱动install)
                - [卸载桥接驱动（uninstall）](#卸载桥接驱动uninstall)
        - [权限类（permission）](#权限类permission)
            - [\* ROOT权限（root）](#-root权限root)
                - [开启ROOT权限（enable）](#开启root权限enable)
                - [关闭ROOT权限（disable）](#关闭root权限disable)
        - [电源类（power）](#电源类power)
            - [启动模拟器（start）](#启动模拟器start)
            - [关闭模拟器（shutdown|stop）](#关闭模拟器shutdownstop)
            - [重启模拟器（restart|reboot）](#重启模拟器restartreboot)
        - [窗口类（window）](#窗口类window)
            - [显示窗口（show）](#显示窗口show)
            - [隐藏窗口（hidden）](#隐藏窗口hidden)
            - [调整窗口大小或位置（layout）](#调整窗口大小或位置layout)
        - [应用类（app）](#应用类app)
            - [安装一个应用（install）](#安装一个应用install)
            - [卸载一个应用（uninstall）](#卸载一个应用uninstall)
            - [启动模拟器里的应用（launch）](#启动模拟器里的应用launch)
            - [关闭模拟器里的应用（close）](#关闭模拟器里的应用close)
            - [\* 判断应用是否存在（exists）](#-判断应用是否存在exists)
            - [\* 判断应用是否不存在（doesntExists）](#-判断应用是否不存在doesntexists)
            - [获取已经安装的应用列表（get\_installed）](#获取已经安装的应用列表get_installed)
            - [\* 获取应用状态（state）](#-获取应用状态state)
        - [核心类（core）](#核心类core)
            - [创建模拟器（create）](#创建模拟器create)
            - [克隆模拟器（clone）](#克隆模拟器clone)
            - [删除模拟器（delete）](#删除模拟器delete)
            - [重命名模拟器（rename）](#重命名模拟器rename)
            - [备份模拟器（export）](#备份模拟器export)
            - [导入模拟器（import\_）](#导入模拟器import_)
            - [限制CPU使用率（limit\_cpu）](#限制cpu使用率limit_cpu)
        - [安卓事件类（androidEvent）](#安卓事件类androidevent)
            - [屏幕旋转（rotate）](#屏幕旋转rotate)
            - [返回主页（go\_home）](#返回主页go_home)
            - [返回（back）](#返回back)
            - [窗口置顶（top\_most）](#窗口置顶top_most)
            - [窗口全屏（fullscreen）](#窗口全屏fullscreen)
            - [摇一摇（shake）](#摇一摇shake)
            - [截图（screenshot）](#截图screenshot)
            - [音量增加（volume\_up）](#音量增加volume_up)
            - [音量减少（volume\_down）](#音量减少volume_down)
            - [音量静音（volume\_mute）](#音量静音volume_mute)
            - [任务键（go\_task）](#任务键go_task)
            - [修改虚拟定位（location）](#修改虚拟定位location)
            - [修改重力感应（gyro）](#修改重力感应gyro)
        - [快捷方式类（shortcut）](#快捷方式类shortcut)
            - [创建桌面快捷方式（create）](#创建桌面快捷方式create)
            - [删除桌面快捷方式（delete）](#删除桌面快捷方式delete)
        - [机型类（simulation）](#机型类simulation)
            - [修改MAC地址（mac\_address）](#修改mac地址mac_address)
            - [修改IMEI（imei）](#修改imeiimei)
            - [修改IMSI（imsi）](#修改imsiimsi)
            - [修改Android ID（android\_id）](#修改android-idandroid_id)
            - [设置模拟器设备型号（model）](#设置模拟器设备型号model)
            - [设置模拟器主板品牌（brand）](#设置模拟器主板品牌brand)
            - [设置模拟器硬件制造商（solution）](#设置模拟器硬件制造商solution)
            - [设置模拟器手机号码（phone\_number）](#设置模拟器手机号码phone_number)
            - [设置模拟器GPU型号（gpu\_model）](#设置模拟器gpu型号gpu_model)
        - [配置类（setting）](#配置类setting)
            - [获取模拟器配置所有配置项（all）](#获取模拟器配置所有配置项all)
            - [获取一个或多个配置项（get）](#获取一个或多个配置项get)
            - [修改一个或多个配置（set）](#修改一个或多个配置set)
            - [根据JSON文件内容修改配置（set\_by\_json）](#根据json文件内容修改配置set_by_json)
            - [\*判断某个配置是否等于某个值（equal）](#判断某个配置是否等于某个值equal)
            - [\*判断某个配置是否不等于某个值（not\_equal）](#判断某个配置是否不等于某个值not_equal)
            - [\*判断某个配置等于某个值时，修改为另一个值（equal\_then\_set）](#判断某个配置等于某个值时修改为另一个值equal_then_set)
            - [\*判断某个配置不等于某个值时，修改为另一个值（not\_equal\_then\_set）](#判断某个配置不等于某个值时修改为另一个值not_equal_then_set)
        - [\*屏幕类（screen）](#屏幕类screen)
            - [调整模拟器分辨率（resolution）](#调整模拟器分辨率resolution)
            - [设置为手机分辨率（resolution\_mobile）](#设置为手机分辨率resolution_mobile)
            - [设置为平板分辨率（resolution\_tablet）](#设置为平板分辨率resolution_tablet)
            - [设置为超宽屏分辨率（resolution\_ultrawide）](#设置为超宽屏分辨率resolution_ultrawide)
            - [调整模拟器DPI（dpi）](#调整模拟器dpidpi)
            - [调整模拟器亮度（brightness）](#调整模拟器亮度brightness)
            - [调整模拟器最大帧率（max\_frame\_rate）](#调整模拟器最大帧率max_frame_rate)
            - [设置动态调整帧率（dynamic\_adjust\_frame\_rate）](#设置动态调整帧率dynamic_adjust_frame_rate)
            - [设置垂直同步（vertical\_sync）](#设置垂直同步vertical_sync)
            - [显示帧率（show\_frame\_rate）](#显示帧率show_frame_rate)
            - [设置窗口自动旋转（window\_auto\_rotate）](#设置窗口自动旋转window_auto_rotate)
        - [性能类（performance）](#性能类performance)
            - [设置CPU和内存（set）](#设置cpu和内存set)
            - [设置CPU个数（cpu）](#设置cpu个数cpu)
            - [设置内存大小（memory）](#设置内存大小memory)
            - [设置强制使用独立显卡（force\_discrete\_graphics）](#设置强制使用独立显卡force_discrete_graphics)
            - [显存使用策略（renderer\_strategy）](#显存使用策略renderer_strategy)
            - [设置磁盘类型（disk\_readonly）](#设置磁盘类型disk_readonly)
        - [\*网络类（network）](#网络类network)
            - [获取所有可被桥接的网卡（get\_bridge\_card）](#获取所有可被桥接的网卡get_bridge_card)
            - [设置网络桥接模式（bridge）](#设置网络桥接模式bridge)
            - [设置网络为NAT模式（nat）](#设置网络为nat模式nat)
            - [设置桥接模式IP设置方式为DHCP（bridge\_dhcp）](#设置桥接模式ip设置方式为dhcpbridge_dhcp)
            - [设置桥接模式IP设置方式为静态（bridge\_static）](#设置桥接模式ip设置方式为静态bridge_static)
        - [ADB类（adb）](#adb类adb)
            - [获取模拟器的ADB连接信息（get\_connect\_info）](#获取模拟器的adb连接信息get_connect_info)
            - [点击屏幕（click）](#点击屏幕click)
            - [滑动屏幕（swipe）](#滑动屏幕swipe)
            - [文本输入（input\_text）](#文本输入input_text)
            - [模拟按键（key\_event）](#模拟按键key_event)
            - [上传文件（push）](#上传文件push)
            - [上传文件到Download目录（push\_download）](#上传文件到download目录push_download)
            - [下载文件（pull）](#下载文件pull)
            - [清理应用数据（clear)](#清理应用数据clear)
        - [GUI自动化类（auto）](#gui自动化类auto)
            - [处理模拟器实时帧（create\_handle）](#处理模拟器实时帧create_handle)
            - [保存模拟器实时帧（save）](#保存模拟器实时帧save)
            - [在帧中查找第一个图片（locateOnScreen）](#在帧中查找第一个图片locateonscreen)
            - [在帧中查找第一张图片的中心点（locateCenterOnScreen）](#在帧中查找第一张图片的中心点locatecenteronscreen)
            - [在帧中查找所有图片（locateAllOnScreen）](#在帧中查找所有图片locateallonscreen)
            - [获取Box的中心点（center）](#获取box的中心点center)
            - [实战举例](#实战举例)
    - [支持本项目](#支持本项目)

## 项目介绍

该项目是基于MuMu提供的``MuMuManager.exe``实现的Python API，可以通过Python代码控制MuMu模拟器的大量操作。

该项目要求你已经安装了MuMu模拟器，且Mumu模拟器版本`>=4.0.0`以上。

## 如何使用？

将本项目安装到您的Python环境中

导入模块

```python
from mumu.mumu import Mumu
```

### 设置MuMuManager路径

如果你的Mumu模拟器不是使用``默认路径``安装，则需要在创建Mumu对象时传入MuMuManager的路径。
默认路径``C:\Program Files\Netease\MuMu Player 12\shell\MuMuManager.exe``

```python
from mumu.mumu import Mumu

Mumu(r'your_path').select(1)
```

### 模拟器索引说明

在Mumu模拟器种，操作模拟器通过索引，索引可以在创建时指定，也可以创建时自动分配，如果你不知道你的模拟器索引是多少，可以打开“Mumu多开器”，找到你的模拟器，最前面那个数字就是你的模拟器索引。

### 选择模拟器

如果指定的操作需要操作模拟器，可以通过``select``方法选择模拟器

```python
from mumu.mumu import Mumu

mumu = Mumu().select(1)
```

对于选择多个模拟器时可以这样，一下4种方式都是等价的，均可以选择1、2、3号模拟器

```python
from mumu.mumu import Mumu

# 第一种
mumu = Mumu().select([1, 2, 3])
# 第二种
mumu = Mumu().select(1, 2, 3)
# 第三种
mumu = Mumu().select((1, 2, 3))
# 也可以混合使用
mumu = Mumu().select([1, 2], 3)
```

如果希望选择所有模拟器，可以使用以下两种方法

```python
from mumu.mumu import Mumu

# 第一种
mumu = Mumu().select()  # 当select什么都不传时，默认选择所有模拟器
# 第二种：通过all方法选择所有模拟器
mumu = Mumu().all()
```

### 举个例子

我希望开启索引为1的模拟器的root权限，然后启动它。

```python
from mumu.mumu import Mumu

# 选择索引为1的模拟器
mumu = Mumu().select(1)
# 开启Root权限
mumu.permission.root.enable()
# 启动模拟器
mumu.power.start()
```

### 注意

带`*`的类是本项目提供的`超类`，并不是MuMu模拟器的API原生提供。

## API类

本项目提供了多个操作类，可以通过这些类实现对模拟器的控制。

### 驱动类（driver）

说明：具官方文档，目前仅支持网络桥接驱动。

#### 网络桥接驱动（bride）

##### 安装桥接驱动（install）

说明：安装桥接驱动需要管理员权限

```python
Mumu().driver.bridge.install()
```

##### 卸载桥接驱动（uninstall）

说明：卸载桥接驱动需要管理员权限

```python
Mumu().driver.bridge.uninstall()
```

### 权限类（permission）

####                * ROOT权限（root）

##### 开启ROOT权限（enable）

说明：开启ROOT权限需要在模拟器关机状态下进行

```python
Mumu().select('your_index').permission.root.enable()
```

##### 关闭ROOT权限（disable）

说明：关闭ROOT权限需要在模拟器关机状态下进行

```python
Mumu().select('your_index').permission.root.disable()
```

### 电源类（power）

#### 启动模拟器（start）

```python
Mumu().select('your_index').power.start()
```

启动完成后打开指定包名的应用

```python
Mumu().select('your_index').power.start('com.tencent.mobileqq')
```

#### 关闭模拟器（shutdown|stop）

```python
Mumu().select('your_index').power.shutdown()
# or
Mumu().select('your_index').power.stop()
```

#### 重启模拟器（restart|reboot）

```python
Mumu().select('your_index').power.restart()
# or
Mumu().select('your_index').power.reboot()
```

### 窗口类（window）

#### 显示窗口（show）

```python
Mumu().select('your_index').window.show()
```

#### 隐藏窗口（hidden）

```python
Mumu().select('your_index').window.hidden()
```

#### 调整窗口大小或位置（layout）

该方法可以接受4个参数，分别是x坐标、y坐标、宽度、高度

```python
Mumu().select('your_index').window.layout(0, 0, 800, 600)
```

如果只希望调整窗口的大小

```python
Mumu().select('your_index').window.layout(None, None, 1080, 1920)
```

也可以只调整一个参数

```python
Mumu().select('your_index').window.layout(300, None, None, None)
# or
Mumu().select('your_index').window.layout(None, None, 1080, None)
```

### 应用类（app）

#### 安装一个应用（install）

该方法接受一个参数，即apk文件的路径，当apk路径无法访问时，会抛出``FileNotFoundError``异常

```python
Mumu().select('your_index').app.install(r'C:\test.apk')
```

#### 卸载一个应用（uninstall）

该方法接受一个参数，即应用的包名

```python
Mumu().select('your_index').app.uninstall('com.miHoYo.Yuanshen')
```

#### 启动模拟器里的应用（launch）

该方法接受一个参数，即应用的包名

```python
# 启动原神
Mumu().select('your_index').app.launch('com.miHoYo.Yuanshen')
```

#### 关闭模拟器里的应用（close）

该方法接受一个参数，即应用的包名

```python
# 关闭原神
Mumu().select('your_index').app.close('com.miHoYo.Yuanshen')
```

####                * 判断应用是否存在（exists）

该方法接受一个参数，即应用的包名

```python
# 判断原神是否存在
if (Mumu().select('your_index').app.exists('com.miHoYo.Yuanshen')):
    print('原神已安装')
else:
    print('原神未安装')
```

####                * 判断应用是否不存在（doesntExists）

该方法接受一个参数，即应用的包名

```python
# 判断原神是否不存在
if (Mumu().select('your_index').app.doesntExists('com.miHoYo.Yuanshen')):
    print('原神未安装')
else:
    print('原神已安装')
```

#### 获取已经安装的应用列表（get_installed）

```python
# 获取已经安装的应用列表
Mumu().select(1).app.get_installed()
```

返回一个列表，当没有安装任何应用时，返回一个空列表

```python
[
    {
        'package': 'com.miHoYo.Yuanshen',  # 包名
        'app_name': '原神',  # 应用名称
        'version': '4.1.8'  # 版本号
    },
]
```

####                * 获取应用状态（state）

该方法接受一个参数，即应用的包名，返回一个字符串，`running`表示应用正在运行，`stopped`表示应用未运行，`not_installed`表示应用未安装

```python
# 获取原神的状态
Mumu().select('your_index').app.state('com.miHoYo.Yuanshen')
```

### 核心类（core）

#### 创建模拟器（create）

该方法接受一个参数，即模拟器的名称，返回一个list包含所创建的模拟器索引

举例：创建一个模拟器

```python
Mumu().core.create()
```

举例：创建5个模拟器

```python
Mumu().core.create(5)
```

举例：创建一个索引为``10``的模拟器

```python
Mumu().select(10).core.create()
```

从索引3开始创建5个模拟器

```python
Mumu().select(3).core.create(5)
```

从索引 3,20 开始，分别创建10次模拟器，索引依次递增(即创建3-12,20-29索引的模拟器)

```python
Mumu().select(3, 20).core.create(10)
```

#### 克隆模拟器（clone）

该方法接受一个参数，即为克隆的数量，但是调用该方法前需要先选择一个模拟器，返回一个list包含所创建的模拟器索引

举例：克隆索引为2的模拟器

```python
Mumu().select(2).core.clone()
```

举例：复制索引为 2,4,6 的模拟器

```python
Mumu().select(2, 4, 6).core.clone()
```

举例：复制索引为2的模拟器，复制10次

```python
Mumu().select(2).core.clone(10)
```

举例：复制所有模拟器

```python
Mumu().all().core.clone()
```

#### 删除模拟器（delete）

该方法不需要传入参数，但是调用该方法前需要先选择一个模拟器，返回bool值，表示是否删除成功

举例：删除索引为2的模拟器

```python
if Mumu().select(2).core.delete():
    print('删除成功')
```

举例：删除索引为2,4,6的模拟器

```python
Mumu().select(2, 4, 6).core.delete()
```

举例：删除所有模拟器（危险操作）

```python
Mumu().all().core.delete()
```

#### 重命名模拟器（rename）

该方法接受一个参数，即为新的模拟器名称，但是调用该方法前需要先选择一个模拟器，返回bool值，表示是否重命名成功。

举例：重命名索引为2的模拟器为“测试”

```python
if Mumu().select(2).core.rename('测试'):
    print('重命名成功')
```

举例：重命名索引为2,4,6的模拟器为“测试”

```python
Mumu().select(2, 4, 6).core.rename('测试')
```

举例：重命名所有的模拟器为“测试”

```python
Mumu().all().core.rename('测试')
```

#### 备份模拟器（export）

该方法接受三个参数，调用该方法前需要先选择一个模拟器，返回bool值，表示是否备份成功。

| 参数   | 说明        |
|------|-----------|
| dir  | 备份的路径     |
| name | 备份的名称     |
| zip  | 是否使用zip压缩 |

举例：备份索引为2的模拟器到C盘目录 backup 下，名称为 test.mumudata，以非压缩的格式

```python
if Mumu().select(2).core.export(r'C:\backup', 'test'):
    print('备份成功')
```

举例：备份索引为2,4,6的模拟器到C盘目录 backup 下，文件名基于 test 自动加后缀，以非压缩的格式

```python
Mumu().select(2, 4, 6).core.export(r'C:\backup', 'test')
```

举例：备份所有的模拟器到C盘目录 backup 下，文件名基于 test 自动加后缀，以压缩的格式

```python
Mumu().all().core.export(r'C:\backup', 'test', True)
```

#### 导入模拟器（import_）

该方法接受一个参数，即为备份文件的路径，如果传入一个列表，则表示导入多个，调用该方法前需要先选择一个模拟器，返回bool值，表示是否导入成功。

举例：导入C盘下的 test.mumudata 并创建模拟器

```python
if Mumu().select(2).core.import_(r'C:\test.mumudata'):
    print('导入成功')
```

举例：导入C盘下的 test.mumudata 并创建模拟器，导入10次

```python
Mumu().select(2).core.import_(r'C:\test.mumudata', 10)
```

举例：导入C盘下的 test.mumudata 和D盘下的 test2.mumudata 并创建模拟器，分别导入10次

```python
Mumu().select(2).core.import_([r'C:\test.mumudata', r'D:\test2.mumudata'], 10)
```

#### 限制CPU使用率（limit_cpu）

该方法接受一个参数，即为CPU使用率，调用该方法前需要先选择一个模拟器，返回bool值，表示是否设置成功。

举例：在索引为2的模拟器中限制CPU为50%

```python
Mumu().select(2).core.limit_cpu(50)
```

举例：在索引为2,4,6的模拟器中限制CPU为50%

```python
Mumu().select(2, 4, 6).core.limit_cpu(50)
```

举例：在所有模拟器中限制CPU为50%

```python
Mumu().all().core.limit_cpu(50)
```

### 安卓事件类（androidEvent）

该类提供了安卓事件操作，可以通过该类实现对模拟器的操作。

调用类的所有方法前需要先选择一个模拟器，返回bool值，表示是否操作成功。
方法未特殊说明时，均无需传入参数。

#### 屏幕旋转（rotate）

```python
Mumu().select(1).androidEvent.rotate()
```

#### 返回主页（go_home）

```python
Mumu().select(1).androidEvent.go_home()
```

#### 返回（back）

```python
Mumu().select(1).androidEvent.go_back()
```

#### 窗口置顶（top_most）

```python
Mumu().select(1).androidEvent.top_most()
```

#### 窗口全屏（fullscreen）

```python
Mumu().select(1).androidEvent.fullscreen()
```

#### 摇一摇（shake）

```python
Mumu().select(1).androidEvent.shake()
```

#### 截图（screenshot）

```python
Mumu().select(1).androidEvent.screenshot()
```

#### 音量增加（volume_up）

```python
Mumu().select(1).androidEvent.volume_up()
```

#### 音量减少（volume_down）

```python
Mumu().select(1).androidEvent.volume_down()
```

#### 音量静音（volume_mute）

```python
Mumu().select(1).androidEvent.volume_mute()
```

#### 任务键（go_task）

```python
Mumu().select(1).androidEvent.go_task()
```

#### 修改虚拟定位（location）

该方法接受两个参数，分别是经度和纬度

举例：在索引为2的模拟器中修改虚拟定位为经度114.1，纬度-23

```python
Mumu().select(2).androidEvent.location(114.1, -23)
```

举例： 在索引为2,4,6的模拟器中修改虚拟定位为经度114.1，纬度-23

```python
Mumu().select(2, 4, 6).androidEvent.location(114.1, -23)
```

举例：在所有模拟器中修改虚拟定位为经度114.1，纬度-23

```python
Mumu().all().androidEvent.location(114.1, -23)
```

#### 修改重力感应（gyro）

该方法接受三个参数，分别是x轴、y轴、z轴

举例：在索引为2的模拟器中修改重力感应X=40，Y=20，Z=30

```python
Mumu().select(2).androidEvent.gyro(40, 20, 30)
```

举例：在索引为2,4,6的模拟器中修改重力感应X=40，Y=20，Z=30

```python
Mumu().select(2, 4, 6).androidEvent.gyro(40, 20, 30)
```

举例：在所有模拟器中修改重力感应X=40，Y=20，Z=30

```python
Mumu().all().androidEvent.gyro(40, 20, 30)
```

### 快捷方式类（shortcut）

#### 创建桌面快捷方式（create）

该方法接受三个参数，分别是快捷方式名称、快捷方式图标路径、应用包名

举例：在桌面创建索引为2的模拟器的快捷方式 test，图标用 C 盘的 test.ico，自动启动原神

```python
Mumu().select(2).shortcut.create('test', r'C:\test.ico', 'com.miHoYo.Yuanshen')
```

举例：在桌面创建索引为2,4,6的模拟器的快捷方式 test，图标用 C 盘的 test.ico，自动启动原神

```python
Mumu().select(2, 4, 6).shortcut.create('test', r'C:\test.ico', 'com.miHoYo.Yuanshen')
```

举例：在所有模拟器中创建快捷方式 test，图标用 C 盘的 test.ico，自动启动原神

```python
Mumu().all().shortcut.create('test', r'C:\test.ico', 'com.miHoYo.Yuanshen')
```

#### 删除桌面快捷方式（delete）

该方法无需传入参数，调用该方法前需要先选择一个模拟器，返回bool值，表示是否删除成功。

举例：删除索引为2的模拟器的快捷方式

```python
Mumu().select(2).shortcut.delete()
```

举例：删除索引为2,4,6的模拟器的快捷方式

```python
Mumu().select(2, 4, 6).shortcut.delete()
```

举例：删除所有模拟器的快捷方式

```python
Mumu().all().shortcut.delete()
```

### 机型类（simulation）

该类提供了模拟器机型操作。这玩意非常的鸡肋！！

#### 修改MAC地址（mac_address）

该方法接受一个参数，即为新的MAC地址，调用该方法前需要先选择一个模拟器，返回bool值，表示是否修改成功。

```python
Mumu().select(1).simulation.mac_address('00:11:22:33:44:55')
```

举例：为索引为1的模拟器随机生成一个MAC地址，两种方式均可

```python
from mumu.constant import MacAddress

# 第一种：传入一个MAC地址
Mumu().select(1).simulation.mac_address(MacAddress.random())

# 第二种：当不传入参数时，表示随机生成一个MAC地址
Mumu().select(1).simulation.mac_address() 
```

#### 修改IMEI（imei）

安卓12不允许应用获取IMEI

该方法接受一个参数，即为新的IMEI，调用该方法前需要先选择一个模拟器，返回bool值，表示是否修改成功。

```python
Mumu().select(1).simulation.imei('123456789012345')
```

举例：为索引为1的模拟器随机生成一个IMEI，两种方式均可

```python
from mumu.constant import IMEI

# 第一种：传入一个IMEI
Mumu().select(1).simulation.imei(IMEI.random())

# 第二种：当不传入参数时，表示随机生成一个IMEI
Mumu().select(1).simulation.imei() 
```

#### 修改IMSI（imsi）

安卓12不允许应用获取IMSI

该方法接受一个参数，即为新的IMSI，调用该方法前需要先选择一个模拟器，返回bool值，表示是否修改成功。

```python
Mumu().select(1).simulation.imsi('460000000000000')
```

举例：为索引为1的模拟器随机生成一个IMSI，两种方式均可

```python
from mumu.constant import IMSI

# 第一种：传入一个IMSI
Mumu().select(1).simulation.imsi(IMSI.random())

# 第二种：当不传入参数时，表示随机生成一个IMSI
Mumu().select(1).simulation.imsi() 
```

#### 修改Android ID（android_id）

该方法接受一个参数，即为新的Android ID，调用该方法前需要先选择一个模拟器，返回bool值，表示是否修改成功。

```python
Mumu().select(1).simulation.android_id('1234567890123456')
```

举例：为索引为1的模拟器随机生成一个Android ID，两种方式均可

```python
from mumu.constant import AndroidID

# 第一种：传入一个Android ID
Mumu().select(1).simulation.android_id(AndroidID.random())

# 第二种：当不传入参数时，表示随机生成一个Android ID
Mumu().select(1).simulation.android_id() 
```

#### 设置模拟器设备型号（model）

该方法接受一个参数，即为新的设备型号，调用该方法前需要先选择一个模拟器，返回bool值，表示是否修改成功。

```python
Mumu().select(1).simulation.model('MI 10')
```

#### 设置模拟器主板品牌（brand）

该方法接受一个参数，即为新的主板型号，调用该方法前需要先选择一个模拟器，返回bool值，表示是否修改成功。

```python
Mumu().select(1).simulation.brand('Xiaomi')
```

#### 设置模拟器硬件制造商（solution）

该方法接受一个参数，即为新的硬件型号，调用该方法前需要先选择一个模拟器，返回bool值，表示是否修改成功。

```python
Mumu().select(1).simulation.solution('qcom')
```

#### 设置模拟器手机号码（phone_number）

安卓12不允许应用获取手机号码

该方法接受一个参数，即为新的手机号码，调用该方法前需要先选择一个模拟器，返回bool值，表示是否修改成功。

```python
Mumu().select(1).simulation.phone_number('18888888888')
```

举例：随机设置一个手机号码，两种方式均可

```python
from mumu.constant import PhoneNumber

# 第一种：传入一个手机号码
Mumu().select(1).simulation.phone_number(PhoneNumber.random())

# 第二种：当不传入参数时，表示随机生成一个手机号码
Mumu().select(1).simulation.phone_number() 
```

#### 设置模拟器GPU型号（gpu_model）

该方法提供4个参数，选填一个即可。

举例：设置索引为1的模拟器的GPU型号为GeForce RTX 3090

```python
Mumu().select(1).simulation.gpu_model('GeForce RTX 3090')
```

举例：设置索引为1的模拟器的GPU型号为高配

```python
Mumu().select(1).simulation.gpu_model(top_model=True)
```

举例：设置索引为1的模拟器的GPU型号为低配

```python
Mumu().select(1).simulation.gpu_model(low_model=True)
```

举例：设置索引为1的模拟器的GPU型号为中配

```python
Memu().select(1).simulation.gpu_model(middle_model=True)
```

### 配置类（setting）

该类提供了模拟器配置文件操作。

在配置类中，不选择任何模拟器即操作全局配置（默认值）

#### 获取模拟器配置所有配置项（all）

该方法提供一个参数`all_writable`，当传入`True`时，表示获取所有可写的配置项，当传入`False`时，表示获取所有配置项，返回一个字典，表示所有配置项的键值对。

举例：获取所有配置项

```python
Mumu().select(1).setting.all()
```

举例：获取所有可写的配置项

```python
Mumu().select(1).setting.all(True)
```

#### 获取一个或多个配置项（get）

该方法接受一个或多个参数，表示要获取的配置项，当获取单个配置项时，返回一个字符串，当获取多个配置项时，返回一个字典，表示所有配置项的键值对。

举例：获取指定一个或多个配置（返回字符串）

```python
value = Mumu().select(1).setting.get('window_size_fixed')
```

举例：获取多个配置项（返回字典）

```python
dict_val = Mumu().select(1).setting.get('window_size_fixed', 'window_save_rect')
```

#### 修改一个或多个配置（set）

该方法接受一个或多个参数，表示要设置的配置项，返回一个bool值，表示是否设置成功。

当传入参数的值为`None`时，表示还原默认值。

如果遇到需要写的配置键包含`.`或者`-`时，将`.`替换为两个`_`，`-`替换为三个`_`。

举例：修改索引为2的模拟器的配置 window_size_fixed 的值为 true

```python
Mumu().select(2).setting.set(window_size_fixed=True)
```

举例：修改索引为2的模拟器的配置 window_size_fixed 的值为 false，配置 window_save_rect 的值为 true

```python
Mumu().select(2).setting.set(window_size_fixed=False, window_save_rect=True)
```

修改索引为2的模拟器的还原配置 window_size_fixed 的值（将使用默认值）

```python
Mumu().select(2).setting.set(window_size_fixed=None)
```

#### 根据JSON文件内容修改配置（set_by_json）

该方法接受一个参数，即为JSON文件的路径，返回一个bool值，表示是否设置成功。

举例：

一个 utf8 格式 test.json 文件在C盘下，文件内容如下：

```json
{
  "window_save_rect": "true",
  "window_size_fixed": "false"
}
```

修改索引为2的模拟器的配置，通过JSON文件方式修改。

```python
Mumu().select(2).setting.set_by_json(r'C:\test.json')
```

#### *判断某个配置是否等于某个值（equal）

该方法接受两个参数，分别是配置项和值，返回一个bool值，表示是否相等。

举例：判断索引为2的模拟器的配置 window_size_fixed 是否等于 true

```python
if Mumu().select(2).setting.equal('window_size_fixed', True):
    print('相等')
else:
    print('不相等')
```

#### *判断某个配置是否不等于某个值（not_equal）

该方法接受两个参数，分别是配置项和值，返回一个bool值，表示是否不相等。

举例：判断索引为2的模拟器的配置 window_size_fixed 是否不等于 true

```python
if Mumu().select(2).setting.not_equal('window_size_fixed', True):
    print('不相等')
else:
    print('相等')
```

#### *判断某个配置等于某个值时，修改为另一个值（equal_then_set）

该方法接受三个参数，分别是配置项、值和新值，返回一个bool值，表示是否修改成功。

举例：判断索引为2的模拟器的配置 window_size_fixed 是否等于 true，如果相等则修改为 false

```python
Mumu().select(2).setting.equal_then_set('window_size_fixed', True, False)
```

#### *判断某个配置不等于某个值时，修改为另一个值（not_equal_then_set）

该方法接受三个参数，分别是配置项、值和新值，返回一个bool值，表示是否修改成功。

当不传入新值时，将自动设置`值`

举例：判断索引为2的模拟器的配置 window_size_fixed 是否不等于 true，如果不相等则修改为 true

```python
Mumu().select(2).setting.not_equal_then_set('window_size_fixed', True, True)

# or 

Mumu().select(2).setting.not_equal_then_set('window_size_fixed', True)
```



### *屏幕类（screen）

该类提供了模拟器屏幕操作。

#### 调整模拟器分辨率（resolution）

该方法接受两个参数，分别是宽度和高度，调用该方法前需要先选择一个模拟器，返回bool值，表示是否修改成功。

举例：修改索引为2的模拟器的分辨率为 800x600

```python
Mumu().select(2).screen.resolution(800, 600)
```

#### 设置为手机分辨率（resolution_mobile）

该方法不需要传入参数，调用该方法前需要先选择一个模拟器，返回bool值，表示是否修改成功。

该方法调整的分辨率为 1080x1920 DPI 为 480

举例：设置索引为2的模拟器的分辨率为手机分辨率

```python
Mumu().select(2).screen.resolution_mobile()
```

#### 设置为平板分辨率（resolution_tablet）

该方法不需要传入参数，调用该方法前需要先选择一个模拟器，返回bool值，表示是否修改成功。

该方法调整的分辨率为 1920x1080 DPI 为 280

举例：设置索引为2的模拟器的分辨率为平板分辨率

```python
Mumu().select(2).screen.resolution_tablet()
```

#### 设置为超宽屏分辨率（resolution_ultrawide）

该方法不需要传入参数，调用该方法前需要先选择一个模拟器，返回bool值，表示是否修改成功。

该方法调整的分辨率为 3200x1440 DPI 为 400

举例：设置索引为2的模拟器的分辨率为超宽屏分辨率

```python
Mumu().select(2).screen.resolution_ultrawide()
```

#### 调整模拟器DPI（dpi）

该方法接受一个参数，即为新的DPI，调用该方法前需要先选择一个模拟器，返回bool值，表示是否修改成功。

举例：修改索引为2的模拟器的DPI为 240

```python
Mumu().select(2).screen.dpi(240)
```

#### 调整模拟器亮度（brightness）

该方法接受一个参数，即为新的亮度，调用该方法前需要先选择一个模拟器，返回bool值，表示是否修改成功。

参数范围为0-100

举例：修改索引为2的模拟器的亮度为 50

```python
Mumu().select(2).screen.brightness(50)
```

#### 调整模拟器最大帧率（max_frame_rate）

该方法接受一个参数，即为新的最大帧率，调用该方法前需要先选择一个模拟器，返回bool值，表示是否修改成功。

参数范围为1-240

举例：修改索引为2的模拟器的最大帧率为 60

```python
Mumu().select(2).screen.max_frame_rate(60)
# or
Mumu().select(2).screen.max_frame_rate()  # 缺省值为60
```

#### 设置动态调整帧率（dynamic_adjust_frame_rate）

该方法接受两个参数，分别是`enable`和`dynamic_low_frame_rate_limit`，调用该方法前需要先选择一个模拟器，返回bool值，表示是否修改成功。

----

| 参数                           | 类型   | 说明                       |
|------------------------------|------|--------------------------|
| enable                       | bool | 是否启用动态调整帧率               |
| dynamic_low_frame_rate_limit | int  | 模拟器不是操作主窗口时，降低至的帧率，默认：15 |

----

举例：启用索引为2的模拟器的动态调整帧率，降低至15帧

```python
Mumu().select(2).screen.dynamic_adjust_frame_rate(True, 15)
```

举例：禁用索引为2的模拟器的动态调整帧率

```python
Mumu().select(2).screen.dynamic_adjust_frame_rate(False)
```

#### 设置垂直同步（vertical_sync）

该方法接受一个参数，即为`enable`，调用该方法前需要先选择一个模拟器，返回bool值，表示是否修改成功。

举例：启用索引为2的模拟器的垂直同步

```python
Mumu().select(2).screen.vertical_sync(True)
```

举例：禁用索引为2的模拟器的垂直同步

```python
Mumu().select(2).screen.vertical_sync(False)
```

#### 显示帧率（show_frame_rate）

该方法接受一个参数，即为`enable`，调用该方法前需要先选择一个模拟器，返回bool值，表示是否修改成功。

举例：启用索引为2的模拟器的显示帧率

```python
Mumu().select(2).screen.show_frame_rate(True)
```

举例：禁用索引为2的模拟器的显示帧率

```python
Mumu().select(2).screen.show_frame_rate(False)
```

#### 设置窗口自动旋转（window_auto_rotate）

该方法接受一个参数，即为`enable`，调用该方法前需要先选择一个模拟器，返回bool值，表示是否修改成功。

设置后，模拟器窗口会根据运行的应用自动旋转

举例：启用索引为2的模拟器的窗口自动旋转

```python
Mumu().select(2).screen.window_auto_rotate(True)
```

举例：禁用索引为2的模拟器的窗口自动旋转

```python
Mumu().select(2).screen.window_auto_rotate(False)
```

### 性能类（performance）

该类提供了模拟器性能操作。

该类的所有操作需要重启模拟器后生效。

#### 设置CPU和内存（set）

该方法接受两个参数，分别是CPU个数和内存大小，调用该方法前需要先选择一个模拟器，返回bool值，表示是否修改成功。

CPU个数范围为1-16

内存大小范围为1-16，单位为GB，不支持小数

举例：设置索引为2的模拟器的CPU为4核，内存为4GB

```python
Mumu().select(2).performance.set(4, 4)
```

#### 设置CPU个数（cpu）

该方法接受一个参数，即为CPU个数，调用该方法前需要先选择一个模拟器，返回bool值，表示是否修改成功。

CPU个数范围为1-16

举例：设置索引为2的模拟器的CPU为4核

```python
Mumu().select(2).performance.cpu(4)
```

#### 设置内存大小（memory）

该方法接受一个参数，即为内存大小，调用该方法前需要先选择一个模拟器，返回bool值，表示是否修改成功。

内存大小范围为1-16，单位为GB，不支持小数

举例：设置索引为2的模拟器的内存为4GB

```python
Mumu().select(2).performance.memory(4)
```

#### 设置强制使用独立显卡（force_discrete_graphics）

该方法接受一个参数，即为`enable`，调用该方法前需要先选择一个模拟器，返回bool值，表示是否修改成功。

举例：启用索引为2的模拟器的强制使用独立显卡

```python
Mumu().select(2).performance.force_discrete_graphics(True)
```

举例：禁用索引为2的模拟器的强制使用独立显卡

```python
Mumu().select(2).performance.force_discrete_graphics(False)
```

#### 显存使用策略（renderer_strategy）

该方法接受三个参数，选择一个即可。

举例：设置索引为2的模拟器的显存使用策略为自动

```python
Mumu().select(2).performance.renderer_strategy(auto=True)
# or
Mumu().select(2).performance.renderer_strategy()
```

举例：设置索引为2的模拟器的显存使用策略为资源占用更小

```python
Mumu().select(2).performance.renderer_strategy(perf=True)
```

举例：设置索引为2的模拟器的显存使用策略为画面表现更好

```python
Mumu().select(2).performance.renderer_strategy(dis=True)
```

#### 设置磁盘类型（disk_readonly）

该方法接受一个参数，即为`enable`，调用该方法前需要先选择一个模拟器，返回bool值，表示是否修改成功。

`enable`缺省值为`True`，开启时，磁盘类型为（只读系统盘，官方推荐），关闭时，磁盘类型为（可写系统盘）

本方法提供一个助手方法`disk_writable`，用于设置磁盘类型为可写系统盘。

举例：设置索引为2的模拟器的磁盘类型为只读系统盘。

```python
Mumu().select(2).performance.disk_readonly(True)

# or

Mumu().select(2).performance.disk_readonly()
```

举例：设置索引为2的模拟器的磁盘类型为可写系统盘

```python
Mumu().select(2).performance.disk_readonly(False)

# or

Mumu().select(2).performance.disk_writable()
```

### *网络类（network）

该类提供了模拟器网络操作。

#### 获取所有可被桥接的网卡（get_bridge_card）

该方法返回一个列表，表示所有可被桥接的网卡。

举例：获取所有可被桥接的网卡

```python
Mumu().select(1).network.get_bridge_card()
```

示例返回：

```python
['Realtek Gaming GbE Family Controller', 'Sangfor SSL VPN CS Support System VNIC', 'Microsoft KM-TEST 环回适配器',
 'Intel(R) Wi-Fi 6E AX211 160MHz']
```

#### 设置网络桥接模式（bridge）

该方法接受两个参数，分别代表是否启用和网卡名称，调用该方法前需要先选择一个模拟器，返回bool值，表示是否修改成功。

该方法需要安装“桥接驱动”才能使用。

举例：启用索引为2的模拟器的网络桥接模式，网卡名称为`Realtek Gaming GbE Family Controller`

```python
Mumu().select(2).network.bridge(True, 'Realtek Gaming GbE Family Controller')
```

举例：禁用索引为2的模拟器的网络桥接模式

```python
Mumu().select(2).network.bridge(False)
```

#### 设置网络为NAT模式（nat）

该方法无需传入参数，调用该方法前需要先选择一个模拟器，返回bool值，表示是否修改成功。

举例：设置索引为2的模拟器的网络为NAT模式

```python
Mumu().select(2).network.nat()
```

#### 设置桥接模式IP设置方式为DHCP（bridge_dhcp）

该方法无需传入参数，调用该方法前需要先选择一个模拟器，返回bool值，表示是否修改成功。

举例：设置索引为2的模拟器的桥接模式IP设置方式为DHCP

```python
Mumu().select(2).network.bridge_dhcp()
```

#### 设置桥接模式IP设置方式为静态（bridge_static）

该方法接受5个参数，分别是IP地址、子网掩码、网关、DNS1、DNS2，调用该方法前需要先选择一个模拟器，返回bool值，表示是否修改成功。

当不填写DNS时，默认DNS1为`8.8.8.8`，DNS2为`114.114.114.114`

举例：设置索引为2的模拟器的桥接模式IP设置方式为静态，IP地址为`192.168.10.10`，子网掩码为`255.255.255.0`
，网关为`192.168.10.1`

```python
Mumu().select(2).network.bridge_static('192.168.10.10', '255.255.255.0', '192.168.10.1')
```

### ADB类（adb）

该类提供了ADB操作。

#### 获取模拟器的ADB连接信息（get_connect_info）

该无需传入参数，调用该方法前需要先选择一个模拟器，当选择一个模拟器时返回一个元组，包含IP和端口，当选择多个模拟器时返回一个字典，键为索引，值为IP和端口。

如果选择的模拟器无法获取到ADB连接信息，将返回`None,None`

举例：获取索引为2的模拟器的ADB连接信息

```python
adb_ipaddr, adb_port = Mumu().select(2).adb.get_connect_info()
```

举例：获取索引为2,4,6的模拟器的ADB连接信息

```python
adb_info = Mumu().select(2, 4, 6).adb.get_connect_info()
```

返回示例

```python
{'2': ('172.30.20.123', 16416), '4': (None, None), '6': (None, None)}
```

#### 点击屏幕（click）

该方法接受两个参数，分别是X坐标和Y坐标，调用该方法前需要先选择一个模拟器，返回bool值，表示是否点击成功。

举例：点击索引为2的模拟器的坐标为(100, 100)的位置

```python
Mumu().select(2).adb.click(100, 100)
```

举例：点击索引为2,4,6的模拟器的坐标为(100, 100)的位置

```python
Mumu().select(2, 4, 6).adb.click(100, 100)
```

#### 滑动屏幕（swipe）

该方法提供5个参数，分别是起始X坐标、起始Y坐标、结束X坐标、结束Y坐标和滑动时间，调用该方法前需要先选择一个模拟器，返回bool值，表示是否滑动成功。

举例：滑动索引为2的模拟器的坐标为(100, 100)到(200, 200)的位置，时间为500ms

```python
Mumu().select(2).adb.swipe(100, 100, 200, 200, 500)
#  or
Mumu().select(2).adb.swipe(100, 100, 200, 200)  # 缺省值为500ms
```

举例：滑动索引为2,4,6的模拟器的坐标为(100, 100)到(200, 200)的位置，时间为500ms

```python
Mumu().select(2, 4, 6).adb.swipe(100, 100, 200, 200, 500)
```

#### 文本输入（input_text）

该方法接受一个参数，即为要输入的文本，调用该方法前需要先选择一个模拟器，返回bool值，表示是否输入成功。

举例：在索引为2的模拟器中输入文本`Hello World`

```python
Mumu().select(2).adb.input_text('Hello World')
```

举例：在索引为2,4,6的模拟器中输入文本`Hello World`

```python
Mumu().select(2, 4, 6).adb.input_text('Hello World')
```

#### 模拟按键（key_event）

该方法接受一个参数，即为要模拟的按键，调用该方法前需要先选择一个模拟器，返回bool值，表示是否模拟成功。

举例：在索引为2的模拟器中模拟按键`HOME`

```python
Mumu().select(2).adb.key_event(3)
```

举例：通过本项目提供的按键常量模拟按键`HOME`

```python
from mumu.constant import AndroidKey

Mumu().select(2).adb.key_event(AndroidKey.KEYCODE_HOME)
```

举例：在索引为2,4,6的模拟器中模拟音量+

```python
from mumu.constant import AndroidKey

Mumu().select(2, 4, 6).adb.key_event(AndroidKey.KEYCODE_VOLUME_UP)
```

#### 上传文件（push）

该方法接受两个参数，分别是本地文件路径和模拟器文件路径，调用该方法前需要先选择一个模拟器，返回bool值，表示是否上传成功。

当上传失败时，会触发一个`warning`警告。

举例：上传索引为2的模拟器的本地文件`C:\test.txt`到模拟器的`/sdcard/test.txt`

```python
Mumu().select(2).adb.push(r'C:\test.txt', '/sdcard/test.txt')
```

举例：上传索引为2,4,6的模拟器的本地文件`C:\test.txt`到模拟器的`/sdcard/test.txt`

```python
Mumu().select(2, 4, 6).adb.push(r'C:\test.txt', '/sdcard/test.txt')
```

#### 上传文件到Download目录（push_download）

该方法提供两个参数，分别是本地文件路径和模拟器文件名，调用该方法前需要先选择一个模拟器，返回bool值，表示是否上传成功。

当`模拟器文件名`为`None`时，将自动使用本地文件名。

举例：上传索引为2的模拟器的本地文件`C:\test.txt`到模拟器的`Download`目录

```python
Mumu().select(2).adb.push_download(r'C:\test.txt')
```

举例：上传索引为2,4,6的模拟器的本地文件`C:\test.txt`到模拟器的`Download`目录，重命名为：`test1.txt`

```python
Mumu().select(2, 4, 6).adb.push_download(r'C:\test.txt', 'test1.txt')
```

#### 下载文件（pull）

该方法提供两个参数，分别是模拟器文件路径和本地文件路径，调用该方法前需要先选择一个模拟器，返回bool值，表示是否下载成功。

当下载失败时，会触发一个`warning`警告。

举例：下载索引为2的模拟器的模拟器文件`/sdcard/test.txt`到本地的`C:\test.txt`

```python
Mumu().select(2).adb.pull('/sdcard/test.txt', r'C:\test.txt')
```

#### 清理应用数据（clear)

该方法接受一个参数，即为应用包名，调用该方法前需要先选择一个模拟器，返回bool值，表示是否清理成功。

如果包名错误会抛出异常

举例：清理索引为2的模拟器的应用数据

```python
Mumu().select(2).adb.clear('com.miHoYo.Yuanshen')
```

### GUI自动化类（auto）

本类提供了模拟器的GUI自动化操作，例如：通过图片定位、坐标定位、文字定位实现自动化操作。

先决条件：需要安装`opencv-python`库，可以通过`pip install opencv-python`安装。

如果希望使用本项目自带的投屏功能，需要安装`scrcpy`，可以通过`pip install scrcpy-client`安装。

#### 处理模拟器实时帧（create_handle）

该方法接受一个参数`handle`，传入一个方法，用于处理模拟器的帧。

该方法基于`scrcpy`实现，如果您的应用对该软件有限制，请勿使用。

使用该方法，会自动创建`2`个子线程，一个用于接收模拟器的帧，一个用于处理帧。

`handle`方法包含两个参数`frame`和`mumu`，分别表示帧和当前模拟器对象。

`frame`为`numpy`数组，可以直接使用`opencv`的方法处理。
`mumu`为当前模拟器对象，仅选中了当前模拟器。

举例：处理索引为2的模拟器的帧

```python
def handle(frame, mumu):
    # do something
    print('接收到模拟器：', mumu.core.utils.get_vm_id(), '的帧')


Mumu().select(2).auto.create_handle(handle)
```

举例：处理索引为2,4,6的模拟器的帧

```python
def handle(frame, mumu):
    # do something
    print('接收到模拟器：', mumu.core.utils.get_vm_id(), '的帧')


Mumu().select(2, 4, 6).auto.create_handle(handle)
```

#### 保存模拟器实时帧（save）

该方法接受两个参数，分别为`frame`和`path`，用于保存模拟器的帧。

举例：保存帧到`C:\test.png`

```python
def handle(frame, mumu):
    mumu.auto.save(frame, r'C:\test.png')


Mumu().select(2).auto.create_handle(handle)
```

举例：保存索引为3的模拟器的帧到`C:\test.png`

```python
def handle(frame, mumu):
    if mumu.core.utils.get_vm_id() == '3':
        mumu.auto.save(frame, r'C:\test.png')


Mumu().select(2, 3).auto.create_handle(handle)
```

#### 在帧中查找第一个图片（locateOnScreen）

该方法接受4个参数，分别为`haystack`、`needle`、`confidence`和`grayscale`，用于在帧中查找图片。

`confidence`为相似度，范围为0-1，缺省值为0.8

`grayscale`为是否使用灰度查找，缺省值为`False

举例：在帧中查找图片`C:\test.png`

```python
def handle(frame, mumu):
    # do something
    print('接收到模拟器：', mumu.core.utils.get_vm_id(), '的帧')
    pos = mumu.auto.locateOnScreen(frame, r'C:\test.png')
    if pos:
        print('找到图片：', pos)
    else:
        print('未找到图片')
```

#### 在帧中查找第一张图片的中心点（locateCenterOnScreen）

该方法接受4个参数，分别为`haystack`、`needle`、`confidence`和`grayscale`，用于在帧中查找图片。

`confidence`为相似度，范围为0-1，缺省值为0.8

`grayscale`为是否使用灰度查找，缺省值为`False

```python
def handle(frame, mumu):
    # do something
    print('接收到模拟器：', mumu.core.utils.get_vm_id(), '的帧')
    pos = mumu.auto.locateCenterOnScreen(frame, r'C:\test.png')
    if pos:
        print('找到图片中心点：', pos)
    else:
        print('未找到图片')

```

#### 在帧中查找所有图片（locateAllOnScreen）

该方法接受4个参数，分别为`haystack`、`needle`、`confidence`和`grayscale`，用于在帧中查找图片。

`confidence`为相似度，范围为0-1，缺省值为0.8
`grayscale`为是否使用灰度查找，缺省值为`False

```python
def handle(frame, mumu):
    # do something
    print('接收到模拟器：', mumu.core.utils.get_vm_id(), '的帧')
    pos = mumu.auto.locateAllOnScreen(frame, r'C:\test.png')
    if pos:
        print('找到图片：', pos)
    else:
        print('未找到图片')

```

#### 获取Box的中心点（center）

该方法接受一个参数，即为`box`，用于获取Box的中心点，返回x和y

`box`为一个元组，包含4个元素，分别为左上角x、左上角y、右下角x、右下角y

```python
def handle(frame, mumu):
    # do something
    print('接收到模拟器：', mumu.core.utils.get_vm_id(), '的帧')
    pos = mumu.auto.locateOnScreen(frame, r'C:\test.png')
    if pos:
        print('找到图片：', pos)
        x, y = mumu.auto.center(pos)
        print('中心点：', x, y)
    else:
        print('未找到图片')

```

#### 实战举例

监听模拟器3的帧，当帧中出现`test.png`时，返回`找到了`，并返回当前时间和模拟器ID，然后返回到桌面。

```python
def handle(frame, mumu: Mumu):
    if mumu.auto.locateOnScreen(frame, './test.png', confidence=0.75, grayscale=True):
        print("找到了", time.time(), '在模拟器', mumu.core.utils.get_vm_id())
        mumu.androidEvent.go_home()


Mumu().select(3).auto.create_handle(handle)

```

## 支持本项目

作者：wlkjyy

Mail：<wlkjyy@vip.qq.com>

WeCHAT：laravel_debug