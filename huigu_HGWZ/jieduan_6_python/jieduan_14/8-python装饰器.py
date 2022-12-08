# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/12/5 17:09
''
'''Python 装饰器
    闭包函数
        
        函数引用
            函数可以被引用
            函数可以被赋值给一个变量
            def hogwarts():
                print("hogwarts")
            
            harry = hogwarts
            harry()
        
    闭包函数
        闭包的内部函数中，对外部作用域的变量进行引用
        闭包无法修改外部函数的局部变量
        闭包可以保存当前的运行环境
        def output_student(grade):
            def inner(name, gender):
                print(f"霍格沃兹测试学社开学啦！\
                学生的名称是{name}，性别是{gender}，
                \年级是{grade}")
            return inner
        
        student = output_student(1)
        student("罗恩", "男")
        student("哈利", "男")
        student("赫敏", "女")    
    
    Python 装饰器
        为什么要学习装饰器
        行业需求： 涉及 Python 技术栈，面试常见题
        使用需求： 优化代码的可读性，可维护性
        
        装饰器示例
            函数体开始执行与结束执行的时候分别添加打印信息
            # 不使用装饰器的代码
            def timer(func):
                print("计时开始")
                func()
                print("计时结束")
            
            def hogwarts():
                print("霍格沃兹测试学院")
            
            timer(hogwarts)
        
        装饰器
            # 使用装饰器的代码
            def timer(func):
                def inner():
                    print("计时开始")
                    func()
                    print("计时结束")
                return inner
            
            @timer
            def hogwarts():
                print("霍格沃兹测试学院")
            
            hogwarts()
            
    装饰器练习
实现一个计时器的装饰器，计算函数执行时间   
        装饰带参数函数
            import datetime
            def timer(func):
                def inner(*args, **kwargs):
                    # 获取当前时间
                    start_time = datetime.datetime.now()
                    func(*args, **kwargs)
                    end_time = datetime.datetime.now()
                    print(f"函数的执行时间{end_time-start_time}")
                return inner
            
            @timer
            def hogwarts(name):
                print("霍格沃兹测试学社", name) 
    '''