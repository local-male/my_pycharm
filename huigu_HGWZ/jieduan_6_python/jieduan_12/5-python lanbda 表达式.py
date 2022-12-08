# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 当前时间 2022/10/19 21:30
''
import math

'''python lanbda 表达式
    匿名函数：没有名字的函数
    用lambda表达式创建匿名函数'''

'''使用场景：需要一个函数，但是又不想去命名
    通常在这个函数只使用一次的场景下
    可以指定短小的回调函数'''

'''语法：
    result:调用lambda表达式
    参数可选，指定要传递的参数列表
    expression:必选，指定一个实现具体功能的表达式
    result = lambda [arg1[,arg2,……,argn]]:expression'''
#常规写法
def circle_area(r):
    '''
    计算圆的面积
    r:半径
    :param r:
    :return:
    '''
    result = math.pi*r**2
    return result
#print(circle_area(4))
result = lambda r:math.pi*r**2 #TODO lambda 表达式
#print(result(4)) # 函数存在的内存地址

#对获取到的信息进行排序
book_info = [('西游戏',20),('python',30),('java',32)]
book_dict = dict(book_info)
print(book_info,type(book_info))
book_info.sort(key=lambda x: (x[1]))#todo lambda
print(book_info)
a = sorted(book_dict.items(),key= lambda x :x[0],reverse=True)#todo lambda
print(a)