# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 当前时间 2022/10/19 16:50
''
'''python函数进阶与参数处理
    可变参数：不定长参数
    常见形式： *args  **kwargs'''

'''*args ：接收任意多个实际参数，并将其放到一个元组中
    使用以及存在的列表或元组作为函数的可变参数，可以在列表前加*'''
# def demo(*args):
#     print(args,type(args))
# demo('python','java','js','php','go')#TODO 不定长参数 返回元组
#
# lan = ['pythton','go','java']
# demo(*lan) # TODO 解包操作

'''**kwargs
    接收任意多个类似关键字参数一样显示赋值的是参数
    并将其放到一个字典中
    使用以及存在字典作为函数的可变参数，可以在字典前加**'''

def demo_1(**kwargs):
    print(kwargs)
demo_1(a=1,b=2)
data = {'tom':18,'lily':12,'jim':20}
demo_1(**data) #TODO 可变参数  关键字  返回字典
