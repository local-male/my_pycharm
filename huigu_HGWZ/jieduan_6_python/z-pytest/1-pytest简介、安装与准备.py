# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/12/8 12:46
''
'''pytest 简介、安装与准备
    前言
        自动化测试前，需要提前准备好数据，测试完成后，需要自动清理脏数据，有没有更好用的框架？
        自动化测试中，需要使用多套测试数据实现用例的参数化，有没有更便捷的方式？
        自动化测试后，需要自动生成优雅、简洁的测试报告，有没有更好的生成方法

    Pytest 背景与优势
        
        Pytest 是什么？
            pytest 能够支持简单的单元测试和复杂的功能测试；
            pytest 可以结合 Requests 实现接口测试； 结合 Selenium、Appium 实现自动化功能测试；
            使用 pytest 结合 Allure 集成到 Jenkins 中可以实现持续集成。
            pytest 支持 315 种以上的插件；
        
        为什么要选择 Pytest
            丰富的第三方插件
            报告
            多线程
            顺序控制
        
        为什么要选择 Pytest
            简单灵活
        
        # content of test_sample.py
        def inc(x):
            return x + 1
         
        def test_answer():
            assert inc(3) == 5
    
        为什么要选择 Pytest
            兼容 unittest
            定制化插件开发
        
    Pytest 环境安装
        前提：本地已配置完成Python环境
        第一种方式 pip install  -U pytest  -U 更新
        第二种方式 PyCharm 直接安装 
    
        运行第一个脚本
            # content of test_sample.py
            def inc(x):
                return x + 1
             
             
            def test_answer():
                assert inc(3) == 5
        
        实操
            1、创建目录 Desktop(桌面)/pytestdemo1
            2、创建文件 test_first.py
            3、打开【terminal】 /【命令提示行cmd】
            4、运行 pytest 回车
        
        '''