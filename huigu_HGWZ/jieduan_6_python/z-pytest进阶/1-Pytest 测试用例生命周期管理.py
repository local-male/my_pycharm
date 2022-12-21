# encoding='utf8'
# file->settings->Editor->file and Code Templates -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 默认测试执行器 pytest配置 ：tools->python intergrated tools-> default test runner 为pytest
# 当前时间 2022/12/19 19:40
''
'''Pytest 测试用例生命周期管理（一）
    Fixture 用法
        Fixture 特点及优势
            1､命令灵活：对于 setup,teardown,可以不起这两个名字
            2､数据共享：在 conftest.py 配置⾥写⽅法可以实现数据共享，不需要 import 导⼊。可以跨⽂件共享
            3､scope 的层次及神奇的 yield 组合相当于各种 setup 和 teardown
            4、实现参数化
    
        Fixture 在自动化中的应用- 基本用法
            场景：
            测试⽤例执⾏时，有的⽤例需要登陆才能执⾏，有些⽤例不需要登陆。
            setup 和 teardown ⽆法满⾜。fixture 可以。默认 scope（范围）function
            
            步骤：
            1.导⼊ pytest
            2.在登陆的函数上⾯加@pytest.fixture()
            3.在要使⽤的测试⽅法中传⼊（登陆函数名称），就先登陆
            4.不传⼊的就不登陆直接执⾏测试⽅法。
        
        Fixture 在自动化中的应用 - 作用域
            取值	        范围	    说明
            function	函数级	每一个函数或方法都会调用
            class	    类级别	每个测试类只运行一次
            module	    模块级	每一个.py文件调用一次
            package	    包级	    每一个python包只调用一次(暂不支持)
            session	    会话级	每次会话只需要运行一次，会话内所有方法及类，模块都共享这个方法
    
        Fixture 在自动化中的应用 - yield 关键字
            场景：
            你已经可以将测试⽅法【前要执⾏的或依赖的】解决了，
            测试⽅法后销毁清除数据的要如何进⾏呢？
            
            解决：
            通过在fixture 函数中加⼊ yield 关键字，yield 是调⽤第⼀次返回结果，
            第⼆次执⾏它下⾯的语句返回。
            
            步骤：
            在@pytest.fixture(scope=module)。
            在登陆的⽅法中加 yield，之后加销毁清除的步骤
        
        
        '''