# encoding='utf8'
# file->settings->Editor->file and Code Templates -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 默认测试执行器 pytest配置 ：tools->python intergrated tools-> default test runner 为pytest
# 当前时间 2022/12/19 19:41
''
import pytest

'''Pytest 测试用例声明周期管理-自动注册
    
    Fixture 在自动化中的应用 - 数据共享
        场景：
        你与其他测试⼯程师合作⼀起开发时，公共的模块要在不同⽂件中，要在⼤家都访问到的地⽅。
        
        解决：
        使⽤ conftest.py 这个⽂件进⾏数据共享，并且他可以放在不同位置起着不同的范围共享作⽤。
        
        前提：
        conftest ⽂件名是不能换的
        放在项⽬下是全局的数据共享的地⽅
        执⾏：
        系统执⾏到参数 login 时先从本模块中查找是否有这个名字的变量什么的，
        之后在 conftest.py 中找是否有。
        步骤：
        将登陆模块带@pytest.fixture 写在 conftest.py

    Fixture 在自动化中的应用 - 自动应用
        场景：
        不想原测试⽅法有任何改动，或全部都⾃动实现⾃动应⽤，
        没特例，也都不需要返回值时可以选择⾃动应⽤
        解决：
        使⽤ fixture 中参数 autouse=True 实现
        步骤：
        在⽅法上⾯加 @pytest.fixture(autouse=True)
        
    Fixture 在自动化中的应用 -参数化
        场景：
        测试离不开数据，为了数据灵活，⼀般数据都是通过参数传的
        解决：
        fixture 通过固定参数 request 传递
        步骤：
        在 fixture 中增加@pytest.fixture(params=[1, 2, 3, ‘linda’])
        在⽅法参数写 request，方法体里面使用 request.param 接收参数
    
    Fixture的用法总结
        模拟setup，teardown（一个用例可以引用多个fixture）
        yield 的用法
        作用域（ session，module, 类级别，方法级别 ）
        自动执行 （autouse 参数）
        conftest.py用法，一般会把fixture写在conftest.py 文件中（这个文件名字是固定的，不能改）
        实现参数化
    
'''
#todo 固定名称
#优先从conftest中查找对应文件
# import pytest
# @pytest.fixture(scope='function')#module session function class
# def login():
#     print('登录成功')
#     token = '1615316921'
#     yield token
#     print('退出登录')
              #作用域           #是否自动应用    #参数化
pytest.fixture(scope='function',autouse=True,params='',ids='',name='')

#todo 参数化
# @pytest.fixture(params=['male','tom','yily'])
# def search(request):
#     print(request.param)
#     yield request.param
# def test_cart(search):
#     print(f'命名：{search}')
# def test_order(login):
#     print('下单')


