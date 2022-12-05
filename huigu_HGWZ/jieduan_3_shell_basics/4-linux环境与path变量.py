# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/24 16:53
''
#todo linux安装 python、node.js、java、android-sdk、maven
'''linux环境与path变量
    bash环境
        linux自带
        mac自带
        windows 使用git bash https://gitforwindows.org/
    
    bash自启动文件startup
        系统级初始化文件 /etc/profile
        登录用户特定初始化文件 ~/.bash_profile
        bash初始化文件 ~/.bashrc
    
    zsh自启动文件startup
        系统级初始化文件 /etc/zprofile
        登录用户特定初始化文件 ~/.zprofile
        bash 初始化文件 ~/.zshrc
    
    PATH 变量
        PATH 变量是一个路径列表，以:隔开
        如果可执行程序所在的目录在 PATH 变量的路径列表里，那么输入命令时可省略路径
        路径列表前面的路径为优先匹配路径，可以用来实现新老版本程序的命令更换
        echo $PATH 可以查看
        
    常见的 PATH 变量问题
        python2 与 python3 指定问题
            while python 查看路径，然后替换
        安装过的命令找不到问题 
    
    PATH 变量使用示例
        export CHROMEDRIVER_HOME=$HOME/projects/chromedriver/91
        export PATH=$CHROMEDRIVER_HOME:$PATH
        
        export VSCODE_HOME=/Applications/Visual\ Studio\ Code.app/Contents/Resources/app/bin
        export PATH=$VSCODE_HOME:$PATH
        
        export SONAR_HOME=/usr/local/Cellar/sonar-scanner/4.2.0.1873
        export PATH=$SONAR_HOME/bin/:$PATH
        export SONARQUBE_TOKEN=c7a93fb6bb1e3268f7099b0f26672ba43c117bb9
        
        export ANDROID_HOME=$HOME/Library/Android/sdk/
        export PATH=$ANDROID_HOME/emulator/:$ANDROID_HOME/platform-tools:$ANDROID_HOME/tools:$ANDROID_HOME/tools/bin:~/bin/:$PATH
    
    应用安装
        平台自带的 app store：
        yum @centos/redhat
        apt-get @ubuntu debian
        scoop winget @windows
        特定平台版本管理工具 pyenv nvm
        安装包安装 pkg dmg
        源码编译安装 make ; make install
    
    redhat/centos 平台示例
        yum search $package   查找
        yum install $package  下载
        yum remove $package   删除
    
    ubuntu/debian 平台
        apt-cache search $package
        apt-get install $package
        apt-get uninstall $package 
    
    开源镜像站
        华为：https://mirrors.huaweicloud.com/
        阿里云：https://developer.aliyun.com/mirror/
    
    Python 版本选择 推荐 Python3.7+
        下载：https://www.python.org/downloads/
        入门：https://docs.python.org/3/tutorial/index.html
        Python3 已经成为行业标准，推荐使用 Python3.x 版本
        Python3.6 增加了类型注解，推荐使用这个版本以上
        
    利用系统自带包管理工具
        yum search python3
        yum install -y python3
    
    安装包安装方式
        windows .exe
        mac .dmg .pkg
        centos .rpm
    
    
    源码安装
        #提前安装对应的各种开发库依赖，每个版本的要求可能都不同
        curl -O https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tgz
        tar -zxvf Python-3.10.0.tgz
        cd Python-3.10.0
        ./configure && make 
        sudo make install
        #DESTDIR=/tmp/python3 make install
    
        在python的目录下执行：export PATH=/home/xxx/Python-3.10.0:$PATH
    检查环境
        python -V
        which python
        echo $PATH
    
    Python 知识点
        pip
        virtualenv
        pycharm
    
    nodejs 生态
        nodejs：https://nodejs.org/zh-cn/
        npm：node 的包管理工具
        cnpm：国内镜像版客户端
    
    npm 包管理工具
        npm install -g $package
        npm uninstall $package
        npm install
    
    nodejs 项目的编译
        appium https://github.com/appium/appium
        stf https://github.com/DeviceFarmer/stf
    
    java 环境配置
        java 下载地址
            java https://www.java.com/zh-CN/
            oracle jdk http://www.oracle.com/technetwork/java/javase/downloads/index.html
            openjdk https://openjdk.java.net/
        
        centos java 安装
            yum search jdk
            yum install -y java-11-openjdk
        
        centos java 多版本配置
            sudo alternatives --list
            sudo alternatives --config java
        
    maven 环境配置
        maven 安装
            unzip apache-maven-3.8.3-bin.zip
            export PATH=/opt/apache-maven-3.8.3/bin:$PATH
            which mvn    
        
        mvn 常用命令
            mvn clean test
            mvn package install
            mvn test -DskipTests
            mvn clean \
              org.jacoco:jacoco-maven-plugin:0.8.5:prepare-agent \
              test \
              org.jacoco:jacoco-maven-plugin:0.8.5:report \
              -Dmaven.test.failure.ignore=true \
              -Dmaven.test.skip=false
        
        编译项目
            git clone https://github.com/spring-guides/gs-spring-boot.git
            cd gs-spring-boot/complete
            mvn package
            java -Dserver.port=8888 -jar target/spring-boot-complete-0.0.1-SNAPSHOT.jar
            #SERVER_PORT=8888 mvn spring-boot:run
        
        maven 的配置
            The Maven install: ${maven.home}/conf/settings.xml
            A user’s install: ${user.home}/.m2/settings.xml
        
    Android SDK 环境配置   
        Android SDK 下载地址
            Android Studio
            Android SDK   
            
        Android SDK 维护
        
        Android SDK 命令行工具
            ceshiren.com: ~ seveniruby$ ls /Users/seveniruby/Library/Android/sdk/tools/bin/
            apkanalyzer     jobb            screenshot2
            archquery       lint            sdkmanager
            avdmanager      monkeyrunner        uiautomatorviewer
        
        Android SDK 构建工具
            ceshiren.com: ~ seveniruby$ ls /Users/seveniruby/Library/Android/sdk/build-tools/29.0.3/
            NOTICE.txt          dexdump             mipsel-linux-android-ld
            aapt                dx              package.xml
            aapt2               i686-linux-android-ld       renderscript
            aarch64-linux-android-ld    lib             runtime.properties
            aidl                lib64               source.properties
            apksigner           lld             split-select
            arm-linux-androideabi-ld    llvm-rs-cc          x86_64-linux-android-ld
            bcc_compat          mainDexClasses          zipalign
            core-lambda-stubs.jar       mainDexClasses.rules
            d8              mainDexClassesNoAapt.rules
        
        Android SDK 平台工具
            ceshiren.com: ~ seveniruby$ ls /Users/seveniruby/Library/Android/sdk/platform-tools/
            NOTICE.txt      etc1tool        make_f2fs_casefold  source.properties
            adb         fastboot        mke2fs          sqlite3
            api         hprof-conv      mke2fs.conf     systrace
            dmtracedump     lib64           package.xml
            e2fsdroid       make_f2fs       sload_f2fs
        
        Android SDK 模拟器工具
            ceshiren.com: ~ seveniruby$ ls /Users/seveniruby/Library/Android/sdk/emulator/
            LICENSE                 lib64
            NOTICE.csv              mksdcard
            NOTICE.txt              package.xml
            android-info.txt            perfetto-protozero-protoc-plugin
            bin64                   qemu
            darwin-aarch64-replace.sh       qemu-img
            emulator                qsn
            emulator-check              resources
            emulator64-crash-service        source.properties
            lib
        
        Android SDK 路径配置
            #*unix，长期使用放入到~/.bash_profile中
            
            #ANDROID_HOME官方不推荐使用，但是仍然生效
            #export ANDROID_HOME=/Users/seveniruby/Library/Android/sdk
            export ANDROID_SDK_ROOT=/Users/seveniruby/Library/Android/sdk
            export PATH=$ANDROID_SDK_ROOT/emulator:$ANDROID_SDK_ROOT/platform-tools:$ANDROID_SDK_ROOT/tools:$ANDROID_SDK_ROOT/tools/bin:$PATH
            
            #windows 长期使用放入到系统属性里
            set ANDROID_SDK_ROOT=E:\Android\sdk\
        
        创建模拟器并通过 shell 运行与执行测试
            创建模拟器
            avdmanager create avd -n 'ceshiren.com.29' -k 'system-images;android-29;google_apis;x86_64' 
            emulator -list-avds  查看所有的模拟器
            emulator @ceshiren.com.29  启动xx模拟器
            adb devices  查看链接设备
            adb -s 设备名称 logcat  日志
            adb shell monkey -p com.google.android.apps.messaging 500 随机点击某个包500次
            avdmanager delete avd -n ceshiren.com.29  删除
        
        
    
    '''