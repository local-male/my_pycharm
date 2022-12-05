# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 当前时间 2022/10/20 10:41
''
'''python类与对象
    类的定义与对象实例化
    类的属性与方法
    类的关键字：class'''

class demo:
    '''demo'''
    message = '类属性'

#访问类属性
#print(demo.message)
'''类的方法：
    实例方法：
        构造方法
    类方法：
    静态方法'''

'构造方法与实例化'
#作用：实例化对象
#语法：def __init__(self,参数列表)
#访问：类名（参数列表）

class demo1:
    #定义属性
    message = '类属性'

    #定义构造方法
    def __init__(self,name,age):
    #实例属性（变量）
        self.name = name
        self.age = age
        print('sb')
#实例化对象
#p = demo1('name',20)

#通过实例访问类属性
#print(p.message)
#通过实例访问实例属性
#print(p.name)

'''实例方法
    作用：提供每个类的实例共享方法
    语法：def 方法名（self，参数列表）
    访问：实例.方法名（参数列表）'''


class demo2:
    #定义实例方法
    def study(self,course):
        print(f'正在学习{course}')
#实例化对象
d = demo2()
#通过实例访问实例方法
#print(d.study('python'))

'''类方法
    作用：可以操作类的详细信息
    语法： @classmethod
    访问：类名.类方法（参数列表）'''

class demo3:

    #类属性
    poplation = 0
    #类方法
    @classmethod#TODO 类方法
    def born(cls):
        print('这是类方法')
        cls.poplation +=1
#
# demo3.born()
# print(demo3.poplation)

'''静态方法:@staticmethod'''
class demo4:
    #定义静态方法
    @staticmethod#TODO 静态方法
    def grow_up():
        print('这是静态方法')

#通过类名访问静态方法
demo4.grow_up()










