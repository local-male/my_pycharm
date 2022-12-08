# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/12/7 11:11



# marry = hogwarts
# print(hogwarts)
# print('*********')
# marry()


# def a(a):
#     def b(b,c):
#         print(f'{a},{b},{c}')
#     return b
# a = a(1)
# a(2,3)


# def c(func):
#     print(1)
#     func()
#     print(2)
#
#
# def cc():
#     print('ss')
# c(cc)
import datetime
import time

#
# def times(func):
#     def inner():
#         print('开始执行')
#         func()
#         print(func)
#         print('结束执行')
#     return inner
# @times
# def hogwarts():
#     print('hogwarts')
# hogwarts()


#实现一个计时器的装饰器，计算函数执行时间

# def timer(func):
#     def inner(*args, **kwargs):
#         start_time = datetime.datetime.now()
#         func(*args, **kwargs)
#         end_time = datetime.datetime.now()
#         print(start_time,end_time)
#         print(end_time-start_time)
#     return  inner
#
# @timer
# def hogwarts(name,age):
#     time.sleep(1)
#     print('hogwarts',name,age)
# hogwarts('male',26)

# class Account:
#     #普通属性
#     bank = 'BOC'
#     #保护属性
#     _username = 'male'
#     #私有属性
#     __passworld = '161531'
#
#
#     @property
#     def passworld(self):
#         return self.__passworld
#
#     @passworld.setter
#     def passworld(self, value):
#         # 增加数据的校验
#         if len(value) >= 8:
#             self.__passworld = value
#         else:
#             print("密码长度最少要有8位！")
#
# obj = Account()
#
# obj.passworld='2134444444'
# print(obj.passworld)


# if isinstance(1,int) or isinstance(0.5,float):
#     print('yes')
# else:
#     print('no')

# # 加法：数字+数字
# print(1 + 1)  # 打印 2
#
# # 拼接：字符串+字符串
# print("Hello" + "World")  # 打印 Hello World
#
# # 合并：列表+列表
# print([1, 2] + [3])  # 打印 [1, 2, 3]
#
# # 参数是字符串
# print(len("Hogwarts"))
#
# # 参数是列表
# print(len([1, 3, 5]))


# class China:
#     def speak(self):
#         print("汉语")
# class Usa:
#     def speak(self):
#         print("英语")
#     # 实例化对象
# cn = China()
# us = Usa()
# for x in (cn, us):
#     # 同一个变量在调用同名方法时，呈现不同的行为
#     # 具体呈现哪种行为，由该变量所引用的对象决定
#     x.speak()


# class Human:
#     """人类"""
#     message = "地球"
#     # 构造方法
#     def __init__(self, name, age):
#         # 实例属性
#         self.name = name
#         self.age = age
#     # 实例方法
#     def live(self):
#         print(f"{self.name}住在{self.message}上")
#
# # stu = Human('male',26)
# # stu.live()
#
# class A(Human):
#     def live(self):
#         print(f'{self.name}今年{self.age},住在{self.message}上')
# # stu = A('male_1',26)
# # stu.live()
#
# class Student(Human):
#     """学生类"""
#     # 重写父类的构造方法
#     def __init__(self, name, age, school):
#         # 访问父类的构造方法
#         super().__init__(name, age)  #第一种
#             #super(Student, self).__init__(name, age)
#         #Human.__init__(self, name, age)  #第二种
#
#         # 子类实例属性（个性）
#         self.school = school
#
#     # 重写父类的实例方法
#     def live(self):
#         print(f"{self.name}住在{self.school}")
#
# stu = Student('male_2',26,'hogwarts')
# stu.live()
# print(stu.name)