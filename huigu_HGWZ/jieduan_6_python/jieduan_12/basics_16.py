# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 当前时间 2022/10/20 11:20
''
from builtins import staticmethod

'''python内置装饰器
    不要实例化、直接调用
    提升代码的可读性
    classmethod   类方法
    staticmethod  静态方法'''

'''普通方法：
    第一个参数为self，代表实例本身
    调用：要有实例化的过程，通过实例对象.方法名 调用'''

'''类方法：
    定义：使用@classmethod装饰器，第一个参数为类本身，
    所有通常使用cls命名做区分（非强制）
    在类内可以直接使用类方法或类变量，无法直接使用实例变量或方法
    调用：无需实例化，直接通过类.方法名调用，也可以通过实例.方法名调用'''

class MethodClass:
    CLASS_PARAM = 0 #类变量

    def demo(self):
        print('普通方法')
    @classmethod
    def class_method(cls):
        #cls.demo()#类方法内，不可以直接调用实例方法，实例变量
        #类方法内，可以直接调用类变量与类方法
        print('这是一个类方法：',cls.CLASS_PARAM)

    @classmethod
    def class_method2(cls):
        #cls.demo()#类方法内，不可以直接调用实例方法，实例变量
        print('这是一个类方法：', cls.CLASS_PARAM)


# MethodClass().class_method()
# MethodClass().demo()

'''静态方法
    定义：使用@staticmethod装饰器，没有和类本身有关的参数
    无法直接使用任何类变量、类方法或者实例方法、实例变量
    调用：无需实例化，直接通过类.方法名调用，也可以通过实例.方法名调用'''


class Staticmethod:

    def demo(self):
        print('普通方法')
    @classmethod
    def class_method(cls):
       print('这是一个类方法')

    #定义：1、要是有staticmethod 装饰器 2、没有参数
    @staticmethod
    def static_demo(param1):
        print('静态方法',param1)

#调用
# Staticmethod.static_demo('s')
# p = Staticmethod()
# p.static_demo('ss')

'''普通方法、类方法、静态方法区别
名称      定义      调用              关键字     使用场景
普通方法   self    实例名.方法名()       无     方法内部涉及到实际对象属性的操作
类方法     cls     类名.方法名() &              如果需要对类属性、即静态变量进行限制性操作
                  实例名.方法名()     @classmethod    
静态方法    无       类名.方法名() &   @staticmethod  无需类和实际参与
                  实例名.方法名()'''

'''如果现在需求变更，输入 年、月、日 没法保证格式统一，
可能是json，可能是其他格式的字符串，在不修改构造函数的前提下，
如何更改代码'''
class DateFormat:
    def __init__(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day

    def out_date(self):
        return f"输入的时间为{self.year}年，{self.month}月，{self.day}日"
    @classmethod
    def json_format(cls,json_data):
        '''
        输入一个字典格式的数据信息，返回（2022，10，21）
        :param json_data:
        :return:
        '''
        year, month, day = json_data['year'], json_data['month'], json_data['day']
        #print(year, month, day)
        return cls(year, month, day)
#常规处理方法
# def json_format(json_data):
#     year, month, day = json_data['year'],json_data['month'],json_data['day']
#     return year, month, day
#
# year, month, day = json_format({'year':2022,'month':10,'day':21})
# #year, month, day = 2017, 7, 1
# demo = DateFormat(year, month, day)
# print(demo.out_date())

# DateFormat.json_format({'year':2022,'month':10,'day':21})
# print(DateFormat().out_date())

json_data = {'year':2022,'month':10,'day':21}
#使用json格式化，生成想要的日期格式，返回DateFormat实例
demo = DateFormat.json_format(json_data) #todo 类方法
#print(demo.out_date())
#print(DateFormat.json_format(json_data).out_date())



'''此方法没有任何和实例、类相关的部分，可以作为一个独立函数使用
某些场景下，从业务逻辑来说又属于类的一部分
例子：简单工厂方法'''
# static 使用场景
class HeroFactory:
    # staticmethod 使用场景，
    # 方法所有涉及到的逻辑都没有使用实例方法或者实例变量的时候
    # 伪代码
    @staticmethod
    def create_hero(hero):
        if hero == "ez":
            return EZ()
        elif hero == "jinx":
            return Jinx()
        elif hero == "timo":
            return Timo()
        else:
            raise Exception("此英雄不在英雄工厂当中")



'''多轮比赛，每轮由2个不同的英雄对打'''

class Game:
    def __init__(self,A,B):
        self.A = A
        self.B = B

    #fight 由和实例对象交互的部分，所有需要动议为一个普通方法
    def fight(self):
        print(f'游戏开始，由{self.A} VS {self.B}')

    #start 无需和实例变量交互，可以使用静态方法
    @staticmethod
    def start():
        print('action')

Game.start()#todo 静态方法
Game1 = Game('A','B')
Game2 = Game('C','D')
Game1.fight()
Game2.fight()


