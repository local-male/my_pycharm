# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/12/5 17:10
''
'''python多态与super
    目录
        多态的概念
        多态的表现
        多态与继承
    
    多态的概念
        多态（Polymorphism）
        同名方法呈现多种行为
    
    
    运算符的多态表现
        +号
        加法：数字+数字
        拼接：字符串+字符串
        合并：列表+列表
        
        # 加法：数字+数字
        print(1 + 1)  # 打印 2
    
        # 拼接：字符串+字符串
        print("Hello" + "World")  # 打印 Hello World
        
        # 合并：列表+列表
        print([1, 2] + [3])  # 打印 [1, 2, 3]
    
    函数的多态表现
        len()函数
        可以接收字符串
        可以接收列表
        
        # 参数是字符串
        print(len("Hogwarts"))
        
        # 参数是列表
        print(len([1, 3, 5]))
    
    方法的多态表现
        同名变量调用同名方法呈现多种行为
        # poly_method.py
        
        class China:
            def speak(self):
                print("汉语")
        
        class Usa:
            def speak(self):
                print("英语")
        
        # 实例化对象
        cn = China()
        us = Usa()
        
        for x in (cn, us):
            # 同一个变量在调用同名方法时，呈现不同的行为
            # 具体呈现哪种行为，由该变量所引用的对象决定
            x.speak()
    
    多态与继承
        方法重写（Override）：子类的方法名称与父类的相同
        重写构造方法
        super().__init__()
        父类名.__init__(self)
        
    # override_demo.py
    class Human:
        """人类"""
    
        message = "这是Human的类属性"
    
        # 构造方法
        def __init__(self, name, age):
            # 实例属性
            self.name = name
            self.age = age
    
        # 实例方法
        def live(self):
            print(f"住在地球上")
    
    
    class Student(Human):
        """学生类"""
    
        # 重写父类的构造方法
        def __init__(self, name, age, school):
            # 访问父类的构造方法
            super().__init__(name, age)
            # super(Student, self).__init__(name, age)
            # Human.__init__(self, name, age)
            # 子类实例属性（个性）
            self.school = school
    
        # 重写父类的实例方法
        def live(self):
            print(f"住在{self.school}")
    
    
    # 实例化子类对象
    stu = Student("哈利波特", 12, "Hogwarts")
    
    # 访问实例方法
    stu.live()  # 将会打印 住在Hogwarts
    
    
    '''