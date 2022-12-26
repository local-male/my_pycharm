# encoding='utf8'
# file->settings->Editor->file and Code Templates -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 默认测试执行器 pytest配置 ：tools->python intergrated tools-> default test runner 为pytest
# 当前时间 2022/12/21 13:33
''
'''显式等待与隐式等待的区别
    
        考察点：是否熟练掌握了三种等待的失业方式与使用场景？何时使用显示、隐式、强制等待？    
        分别从使用方式、原理、使用场景进行总结
类型       使用方式                       原理                  使用场景
直接等待    time.sleep()                强制线程等待              临时调试
隐式等待    driver.implicitly_wait()    在时间范围内，轮询查找元素   解决找不到元素的问题
显式等待    webdriverwait.until()       设定特定的等待条件，轮询    1、元素交互 2、自定义封装
        
        '''
'''定位不到元素的问题
    元素定位：
        selenium/appium定位方法有几种，分别是？
            八种：id/name/class/css/xpath
            四种：id/text/class
        如何通过子元素定位父元素？
            xpath定位
    元素定位不到：
        定位不到元素是什么原因导致的？
            定位不准确  在console先测试定位是否准确
            页面未加载完成  添加等待
            存在动态id     定位切换xpath
            页面存在iframe 切换iframe
            页面切换windows 切换窗口
        有的元素明明加载到了，但是你却定位不到，怎么解决？
        如何动态的定位元素？
    元素操作：
        selenium中隐藏元素如何定位？
            隐藏元素可以直接定位，但是无法直接点击或交互  使用js执行交互操作
        一个元素明明定位到了，点击无效，如何解决？
            异步加载js导致点击不到  循环点击该元素，直至生效
        产品总是出现弹窗，导致原理无法执行，应该如何解决？
            添加黑名单异常处理
        如何获取app中的toast消息提示？
            toast闪过太快，不好定位   xpath结合隐式定位
    元素是否存在页面：
        如何判断一个页面上元素是否存在？
            1、查看当前页面dom
            2、打印page_source
            对应课程：自动化关键数据记录
        '''
'''app启动性能分析
    业务测试--手工测试
          --接口测试
    专项测试--端性能测试--耗电量测试--batteryhistory
                              --instruments
                    --卡顿测试  --biockcanary
                    --h5性能测试--devtool headless chrome
            端场景测试--兼容性测试--mqc mtc testin
                              --appium gird stf
                    --健壮性测试--monkey
                    --弱网测试--facebok atc
                             --proxy定制
                    --安全测试 --wvs
                              --burpsuite
    回归测试--接口自动化测试
          --ui自动化测试
          --自动化遍历回归测试
    
    主要流程
        application oncreate
            加载第三方的sdk
        activity oncreate
            加载自身的逻辑
            发送远程数据请求  xx.json
            渲染界面list 
    
    app启动性能指标
        冷启动  首次启动  完全kill掉   5s
        暖启动  刚kill掉 还有缓存      2s
        热启动  启动后关闭  未kill掉   1.5s
        首屏启动  包含广告等
        
        adb logcat
        录屏+视频拆帧
        uiautomator等自动化工具200ms巡检界面变化
        traceview
        硬埋点
    
    使用adb logcat
    package=com.xueqiu.android
    清理缓存数据：adb shell pm clean $package
    停止进程： adb shell am force-stop $package
    启动app： adb shell am start -s -w $package/.view.welcomeActivityAlias
    获取数据：adb logcat |grep -i displayed
    adb logcat结果
    starttime:记录刚准备调用start Activity A你的Wail() 的时间点；
    endTime:记录start Activity A你的Wait()函数调用返回的时间点
    WaitTime:startActivityAndWait() 调用耗时
        WaitTime = endTime - startTime
    '''
'''接口性能
    代理工具 charles  burpsuite
    抓包工具 tcpdump wireshark
    接口测试过程讲解
    '''
'''PC 浏览器的性能分析
    关键选项
        disable cache:不加载缓存，从零开始载入
        蓝色线：dom出现
        红色线：图片等资源加载完成
    '''

'''卡顿分析
        systace
            sdk/platform-tools/systrace
            需要python2.7
            安装win32con
            pip2 install ppiwin32
            pip2 install six
        使用
            启动设备
            输入命令与参数
            python systrace.py -e 192.168.181.102:5555 -i
        不加参数启动
            在命令行：python systrace.py -e 192.168.181.102:5555 -i
            在设备上进行操作
            在命令行：按下enter
        卡顿影响因素
            内存问题：内存抖动、full gc
            cpu：计算耗时
            render:布局复杂、overdraw
        帧分析
            冰冻帧：一个帧超过0.7s
            帧分析： adb -s devicesname shell dumpsys gfxinfo |less      
    '''
'''系统资源分析
    cpu与gpu的关系
    cpu与gpu无法直接通信，cpu把 display list 放入队列。gpu从队列取数据进行绘制
    参考阅读
        https://developer.android.com/topic/performance/rendering/inspect-gpu-rendering
    mem统计
        术语    全拼                解释
        vss   virtual set size  虚拟耗用内存（包含共享库占用的内存）
        vss:衡量虚拟内存大小无太大用处，无法知道分配的物理内存大小
        rss   resident set size  实际使用物理内存（包含共享库占用的内存）
        rss:各进程的rss相加，会超过系统内存使用量
        pss   proportional ser size  实际使用的物理内存（比例分配共享库占用的内存）
        pss:各进程的pss之和，就是系统的内存使用量
        uss   unique set size     进程独自占用的物理内存（不包含共享库占用的内存）
        uss：是pss中自己的部分，不包含任何共享的部分
    
    procstats
        查看3小时内的m内存使用情况
        adb shell dumpsys procstats --hours 3
    输入字段解释：
        百分比：表示在总的时间内，进程在各种状态下的消耗
            例如：100%，就指在这段时间内，这个进程是一值处于运行当中的
        total：表示了进程的综合占用情况
        imp fg:加载到前台
        service：标识了是否是服务 
        persistent：标识了是否一直驻留在内存当中，与service一样，表示内存进驻的级别
        top：标识了是否是顶层进程
        receiver:标识了是否是广播进程
    查看系统知道进程的mem：
        adb shell dumpsys meminfo com.xueqiu.android
    
    
    网络分析
        显示网络流量
            adb shell dumpsys netstats
        找到应用uid
        adb shell dumpsys package com.xueqiu.android |grep userld
        userld=10007 gids=[3003,1028,1015]
        
        参看相关应用的流量情况
        set=default 标识前台网络使用情况
        set=background 标识后台使用情况
        set=all 标识上述两类使用情况
        tag=0x0 标识与流量关联的套接字代码
        rxbytes 和 rxpackets 表示在相应时间间隔内接受的字节数和数据包数
        txbytes 和 txpackets 在相应时间间隔内发送的字节数和数据包数
        
        '''
'''
    耗电量测试
        待机时间成关注指标
        提升用户体验
        通过不同的测试场景，找出app高耗电场景并解决
        
    安装
        git clone https://github.com/google/battery-historian.git
        cd battery-historian
        go get -d -u github.com/google/batter-historian/...
        go run setup.go
        go run cmd/battery-historian/battery-historian.go
    
    测试步骤
        使用batterystats生成数据
        使用Battery historian 分析数据
    
    batterystats收集数据
        1、清理耗电量数据
            adb shell dumpsys batterystats --reset
            adb shell dumpsys batterystats --enable full-wake-history
        2、运行测试用例/手工操作
        3、收集数据
            android 7.0:adb bugreport bugreport.zip
            andriod 6.0:adb bugreport>bugreport.txt
    
    指标含义
        battery_level:电量
        plugged:充电状态及充电的时长
        screen:屏幕是否点亮
        top:显示当前手机运行的app
        status:电池状态信息，有充电、放电、未充电、已充满、未知等不同状态
        '''
'''弱网测试
        弱网问题
            封闭环境
                丢包
                数据无法加载
                消息更新不及时等
        弱网速度
            低于2G速率
            3G
        
        模拟弱网
            charles官网：https://www.charlesproxy.com/download/
        
        charles代理设置
            位置：proxy-->proxy settings
        设置本地代理
        
        
        开启节流 限制网速（快捷键在首页第四个图标 龟）
            proxy-->throttle settings-->enable throttling
            
            字段解释
                bandwidth 带宽
                    理论网速上限
                utilisation 利用
                    总带宽的百分比
                round-trip latency 请求往返延迟
                    客户端和服务器第一次往返通信的延迟、单位毫秒
                MTU 最大传输单元
                    传输的TCP数据包的最大尺寸
                Reliability 可靠性
                    衡量连接完全失败的可能性
        
        常用网速展示(参考)
            网络环境    上下行带宽（kbs）  上下行延迟（ms）
            2G          20/50           500/400
            3G          330/2000        100/100
            4G          40000/80000     15/10
            WIFI        33000/40000     1/1
            带宽有线环境
    '''
'''健壮性测试
    用于测试系统在出现故障时，是否能够自动回复或者忽略故障继续运行
    
    操作过程
        对应进行盲点
        网络不佳
        数据不通
    
    工具使用
        monkey maxim
        charles
        appcrawler
        '''
'''兼容性测试
    硬件之间、软件之间、软硬件之间的相互配合程度
    
    app兼容性测试
        移动设备型号多样
        测试app在主流设备上能否正常运行
        测试app在主流设备上奔溃卡顿现象
    
    兼容性测试作用
        进一步提高产品的质量，提高用户体验
        尽可能达到平台无关性
        保证软件存在价值，是衡量软件质量的重要指标
        使软件产品的市场更广阔
    
    测试方法
        人工测试
        借助第三方工具
            appcrawler
            指定app 指定版本 
    '''