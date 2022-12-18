# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/12/8 12:51
''
'''pytest 命令行常用参数
    
    命令行参数 - 常用命令行参数
        —help 
        -x   用例一旦失败(fail/error)，就立刻停止执行
        --maxfail=num 用例达到 
        -m  标记用例
        -k  执行包含某个关键字的测试用例
        -v 打印详细日志
        -s 打印输出日志（一般-vs一块儿使用）
        --collect-only（测试平台，pytest 自动导入功能 ）
    
    
    '''
#todo pytest 参数验证
#todo -x   用例一旦失败(fail/error)，就立刻停止执行   pytest test_2.py::Test_x -xvs
#todo --maxfail=num 用例达到    pytest test_2.py::Test_x -vs --maxfail=2
#todo -k  执行包含某个关键字的测试用例 （用例名称）   pytest test_2.py -k 'not order'
#todo -m  标记用例 一般指装饰器标记
#todo  --collect-only（测试平台，pytest 自动导入功能 ）
# class Test_x:
#     def test_a(self):
#         assert True
#
#     def test_b(self):
#         assert False
#
#     def test_c(self):
#         assert False
#
#     def test_d(self):
#         assert True
#
#     def test_sss(self):
#         assert False