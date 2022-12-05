# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 当前时间 2022/10/19 11:57
''
'''python函数
    函数的作用
    函数定义
    函数定义
    函数传递
    函数返回值'''
'''函数的作用：函数是组织好的，可以重复使用的，
用来实现单一活相关联功能的代码段
    函数能提高应用的模块性和代码的重复利用率
    python内置函数：https://docs.python.org/zh-cn/
    3.8/library/functions.html'''#TODO

'''函数定义：
    def：函数关键词
    ():参数列表放置的位置，可以为空
    parameter_list：可选，指定函数中传递的类型
    function_body：可选，指定函数体'''
# def func():
#     '''函数demo'''
#     print('函数')
#print(func.__doc__)#TODO 打印函数的comments 函数注释
#help(func) #TODO 作用一致

def demo():
    pass
'''函数调用
    function_name :函数名称
    parameter_value :可选，指定各个参数的值'''

'''为参数设置默认值
    定义函数时可以指定形式参数的默认值
    指定默认值的形式参数必须放在所有参数的最后，否则会产生语法错误
    param = default_value：可选，指定参数并且为该参数设置默认值
    默认值采用不可变的对象'''

'函数返回值：可选，指定返回的值 关键字：return'

def sun_1(a,b):
    result = a + b
    return result,a,b
r = sun_1(2,3)
#print(r) #TODO 返回为元组

