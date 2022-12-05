# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 当前时间 2022/10/18 18:48
''
'''python常用的数据结构-元组tuple
    元组定义于使用
    元组常用方法
    元组与列表
    
    定义：元组是有序的不可变对象集合
        元组使用小括号包围，各个对象之间使用逗号分隔
        元组是异构的，可以包含多种数据类型
    元组使用：创建
        使用逗号分隔
        通过小括号填充元素
        通过构造方法tuple(iterable)
    '''
tuple_1 = 1,
#print(type(tuple_1),tuple_1)
tuple_2 = (1,2,3,4)
#print(type(tuple_2),tuple_2)
tuple_3 = tuple('ssda')#todo 字符串或者列表转换为元组
#print(type(tuple_3),tuple_3)

'''元组使用：索引
    可以通过索引来访问对应的元素
    正向索引：从0开始
    反向索引：从-1开始'''

'''元组使用：切片
    三个值均可u西安，非必填
    start:开始值，默认0
    stop：结束值，默认最大值
    step: 步长，默认为1'''

tuple4 = (1,2,3)
#print(tuple4[0:3:1])

#print(tuple4.index('7f'))#todo 返回与目标元素匹配的首个元素的索引
#todo 不存在会报错
#print(tuple4.count(2))#todo 参数为元素值，返回元素出现的次数

'''元组解包
    把一个可迭代对象的元素，一并赋值到对应的变量组成的元组中'''
a,b,c = tuple4#TODO
#print(a,b,c)
#a,b,c = [1,2,3]
#print(a,b,c)

'''元组与列表
    相同点：  都是有序的
            都是异构的，能够包含不同类型的对象
            都支持索引和切片
    不同点：  申明方式不同，元组使用(),列表使用[]
            列表是可变的，元组是不可变的'''

