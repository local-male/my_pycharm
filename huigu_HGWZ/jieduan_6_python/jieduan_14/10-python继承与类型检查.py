# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/12/5 17:10
''
'''python继承与类型检查
    目录
        继承的概念
        继承的实现
    
    继承的概念
        继承（Inheritance）
        复用父类的公开属性和方法
        拓展出新的属性和方法
    
    继承的实现
        语法：class 类名(父类列表)
        默认父类是 object
        Python 支持多继承
    # inheritance_demo.py

    class Human:
        """人类"""
    
        # 类属性
        message = "这是Human的类属性"
    
        # 构造方法
        def __init__(self, name, age):
            # 实例属性
            self.name = name
            self.age = age
    
        # 实例方法
        def live(self):
            print("住在地球上")
    

    class Student(Human):
        """学生类"""
    
        def study(self):
            print("正在学习")


    # 实例化子类对象
    stu = Student("哈利波特", 12)
    # 访问类属性（继承）
    print(stu.message)
    # 访问实例属性（继承）
    print(stu.name, stu.age)
    # 访问实例方法（继承）
    stu.live()
    # 访问实例方法（扩展）
    stu.study()

    
    类型检查
        isinstance(实例, 类名)
        检查对象是否是某个类及其派生类的实例
        issubclass(类名1, 类名2)
        检查类名 1 是否是类名 2 的子类
    
        # relation_demo.py

        # 人类
        class Human:
            pass
        
        # 学生类
        class Student(Human):
            pass
        
        # 老师类
        class Teacher(Human):
            pass
        
        # 检查实例与类的关系
        stu = Student()
        print(isinstance(stu, Human))  # 将会打印 True
        
        # 检查类与类的关系
        print(issubclass(Student, Human))  # 将会打印 True
        print(issubclass(Student, Teacher))  # 将会打印 False
    
    '''
#Python 中的isinstance()函数，isinstance()是Python中的一个内建函数。是用来判断一个对象的变量类型
#todo isinstance(object, classinfo)
#如果参数object是classinfo的实例，或者object是classinfo类的子类的一个实例，
# 返回True。如果object不是一个给定类型的的对象， 则返回结果总是False
# todo isinstance() 与 type() 区别：
# type() 不会认为子类是一种父类类型，不考虑继承关系。
# isinstance() 会认为子类是一种父类类型，考虑继承关系。
# todo 如果要判断两个类型是否相同推荐使用 isinstance()。

#todo issubclass() 方法用于判断参数 class 是否是类型参数 classinfo 的子类
#todo issubclass(class, classinfo)
#todo 如果 class 是 classinfo 的子类返回 True，否则返回 False。

