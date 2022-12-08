# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/12/5 17:09
''
'''python封装与property装饰器
    目录
        封装的概念
        封装的实现
    
    封装的概念
        封装（Encapsulation）
        隐藏：属性和实现细节，不允许外部直接访问
        暴露：公开方法，实现对内部信息的操作和访问
    
    封装的作用
        限制安全的访问和操作，提高数据安全性
        可进行数据检查，从而有利于保证对象信息的完整性
    
    封装的实现：隐藏
        保护属性：_属性名
        私有属性：__属性名
            被视作 _类名__属性名
    
    class Account:

        # 普通属性
        bank = "BOC"
        # 内部属性
        _username = "Hogwarts"
        # 私有属性
        __password = "888"


    # 通过类名访问类属性
        print(Account.bank)  # 将会打印 BOC
        print(Account._username)  # 将会打印 Hogwarts
        print(Account.__password)  # 将会引发 AttributeError
        
        print(Account.__dict__)   查看所有属性
    
    # 实例化
        obj = Account()
    
    # 实例访问类属性
        print(obj.bank)  # 将会打印 BOC
        print(obj._username)  # 将会打印 Hogwarts
        print(obj.__username)  # 将会引发AttributeError
    
    封装的实现：暴露
        提供数据访问功能（getter）
        计算属性
        语法：使用@property装饰器
        调用：实例.方法名
    
    class Account:
        # 普通属性
        bank = "BOC"
        # 内部属性
        _username = "Hogwarts"
        # 私有属性
        __password = "888"
    
        @property
        def password(self):
            return self.__password

    # 实例化对象
        obj = Account()
        
        # 访问实例的私有属性
        print(obj.password)  # 将会打印 888
    
    
    
    封装的实现：暴露
        提供数据操作功能（setter）
        语法：使用@计算属性名.setter装饰器
        调用：实例.方法名
    
    class Account:
        # 普通属性
        bank = "BOC"
        # 内部属性
        _username = "Hogwarts"
        # 私有属性
        __password = "888"
    
        @property
        def password(self):
            return self.__password
    
        @password.setter
        def password(self, value):
            # 增加数据的校验
            if len(value) >= 8:
                self.__password = value
            else:
                print("密码长度最少要有8位！")


        # 实例化对象
        obj = Account()
        
        # 修改私有属性（满足校验条件）
        obj.password = "hogwarts666"  # 修改成功
        print(obj.password)  # 将会打印 hogwarts666
        
        # 修改私有属性（不满足校验条件）
        obj.password = "123"  # 修改不会生效
        print(obj.password)  # 将会打印 888
    
    
    
    '''