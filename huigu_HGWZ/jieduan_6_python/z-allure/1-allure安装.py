# encoding='utf8'
# file->settings->Editor->file and Code Templates -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 默认测试执行器 pytest配置 ：tools->python intergrated tools-> default test runner 为pytest
# 当前时间 2022/12/19 11:01
''
'''allure 安装
    
    Allure 介绍
        Allure是⼀个轻量级，灵活的，⽀持多语⾔的测试报告⼯具
        多平台的,奢华的report框架
        可以为dev/qa提供详尽的的测试报告、测试步骤、log
        也可以为管理理层提供high level统计报告
        Java语⾔开发的，⽀持python，JaveScript, PHP, ruby 等
        可以集成到Jenkins    
    
    Allure 报告展示
        官方：http://allure.qatools.ru
    
    Allure 报告展示 - 首页概览
    Allure 报告展示 - 用例详情页
    
    Allure 环境安装
        Allure 安装
            1、安装 Java (推荐 1.8 版本)，需要配置环境变量
                JDK 环境安装
                    java 官方下载地址（windows 下载 exe 安装包即可）
                    https://www.oracle.com/java/technologies/downloads/#java8
                    社区提供下载地址：
                    链接: https://pan.baidu.com/s/1R8KClEPKio5dE0PAYN1jlA
                    提取码: xwd9
                配置 JAVA 环境变量
                    java（windows 系统）：https://ceshiren.com/t/topic/13450
                    java（mac 系统）：https://ceshiren.com/t/topic/6967
            2、安装 Allure(2.13) ，需要配置环境变量
                Allure 安装
                    下载地址：https://repo1.maven.org/maven2/io/qameta/allure/allure-commandline/
                    mac/linux: 下载 tar
                    windows: 下载 zip
                    配置环境变量：解压后将 bin 目录加入PATH环境变量
                    安装贴：https://ceshiren.com/t/topic/3386
        环境验证
            allure --version
    
    Allure 常用命令
    
    使用 Allure2 生成精美报告
        命令格式：allure  [option]   [command]   [command options]
        
        在测试执行期间收集结果
        pytest  [测试文件] -s –q --alluredir=./result/ (—alluredir这个选项 用于指定存储测试结果的路径)
        示例：pytest test_1.py -s -q  --alluredir=./report/result/ 
        查看测试报告
        方式一：测试完成后查看实际报告， 在线看报告，会直接打开默认浏览器展示当前报告
          allure serve ./result/   (注意这里的serve书写)
          示例：allure serve /report/result 
        方式二：从结果生成报告，这是一个启动tomcat的服务，需要两个步骤：生成报告，打开报告
          生成报告 
            allure generate ./result/ -o ./report/ --clean  (注意：覆盖路径加--clean )
          打开报告 
            allure open -h 127.0.0.1 -p 8883 ./report/ 
        
    Allure 用法
        查看官网：https://docs.qameta.io/allure/#_pytest
        源码example:  https://github.com/allure-examples/allure-examples/
    
    Allure特性-feature/story
        场景:
        希望在报告中看到测试功能，子功能或场景
        解决:
        @Feature,  @story<br/> 步骤:
        import allure
        功能上加  @allure.feature(‘功能名称’)
        子功能上加  @allure.story(‘子功能名称’)
        运行：
        
        pytest 文件名 --allure-features=FEATURES_SET --allure-stories=STORIES_SET
    
    Allure 特性-feature/story的关系
        feature 相当于一个功能，一个大的模块，相当于testsuite
        story 相当于对应这个功能或者模块下的不同场景，分支功能
        feature 与 story 类似于父子关系
    
    Allure特性-step
        场景：
            测试过程中每个步骤，一般放在具体逻辑方法中，可以放在关键步骤中，在报告中显示
            在app, web⾃动测试当中，建议每切换到⼀个新的页⾯当做一个step
        解决 : 
            with allure.step():  可以放在测试用例方法里面，但测试步骤的代码需要被该语句包含
        
        Allure特性 - testcase/issue/link
        场景：
        测试报告中，添加用例的链接，bug 链接地址，相关的链接地址
        
        解决 ：
        @allure.link()、@allure.issue()、@allure.testcase()
        主要是为了将allure报告和测试管理系统集成（用例管理/bug 管理 ），可以更快速的跳转到公司内部地址。
        
        Allure特性 - 设置优先级
        五种级别 ：
            BLOCKER("blocker"),  阻塞缺陷（功能未实现，无法下一步）
            CRITICAL("critical"),    严重缺陷（功能点缺失）
            NORMAL("normal"),    一般缺陷（边界情况，格式错误）
            MINOR("minor"),     次要缺陷（界面错误与ui需求不符）
            TRIVIAL("trivial");    轻微缺陷（必须项无提示，或者提示不规范）
        
    Allure特性 - 设置优先级
        场景：
        通常测试有P0、冒烟测试、验证上线测试。
        按重要性级别来分别执行的，比如上线要把主流程和重要模块都跑一遍
        解决 ：
        也可以通过 allure.severity来附加标记
        实例：
        在方法,函数和类上面加
        @allure.severity(allure.severity_level.TRIVIAL)
        
        运行：
        运⾏级别为：normal,critical  的测试⽤例
        pytest -s -v 文件名 –allure-severities normal,critical –alluredir=./result        
    
    Allure 特性 - 测试报告中添加附件
        场景：
        希望在报告中看到测试用例的详细内容展示
        比如在用例中添加附件信息，可以是数据，文本，图片，视频，网页
        
        解决:
        @allure.attach显示许多不同类型的提供的附件，可以补充测试，步骤或测试结果。
        用法：
        allure.attach(body(内容), name, attachment_type, extension):Allure 特性 - 测试报告中添加附件
        场景：
        希望在报告中看到测试用例的详细内容展示
        比如在用例中添加附件信息，可以是数据，文本，图片，视频，网页
        
        解决:
        @allure.attach显示许多不同类型的提供的附件，可以补充测试，步骤或测试结果。
        用法：
        allure.attach(body(内容), name, attachment_type, extension):
    
    Allure 总结
        ⽀持多平台
        Java语⾔开发的，⽀持多语言 pytest，JaveScript, PHP, ruby 等
        可以为dev/qa提供详尽的的测试报告、测试步骤、log、标题、优先级、附件等等
        也可以为管理理层提供high level统计报告
        可以集成到Jenkins，展示项目的趋势图
    '''