# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 当前时间 2022/10/18 10:35
''
'''python常用的数据结构
    list    列表
    tuple   元组
    dict    字典
    set     集合'''

'''list 列表
    列表定义与使用
    列表常用方法
    列表嵌套
    列表推导式'''

'''列表定义：
    列表是有序的可变元素的集合，使用[]包围
    元素之间用逗号分隔
    列表是动态的，可以随时收缩和扩展
    列表是异构的，可以同事存放不同类型的对象
    列表中允许出现重复元素'''
'''列表使用：创建
    通过构造函数创建
    []创建并填充
    列表推导式'''
li = list()
#print(type(li),li)
li1 = 'hogwarts'
#print(list(li1),type(list(li1)))

li2 = []
li2.append(1)
li2.append('a')
li2.append(['v','f'])
#print(li2)

li3 = [i for i in range(1,11) if i %2 == 0]#TODO  列表推导式
#print(li3)

'''列表使用：索引
    默认正向索引，编号从0开始
    支持反向索引，编号从-1开始'''

# print(li3[2])
# print(li3[-3])

'''列表使用：切片
    start:开始索引值，默认0
    stop:结束索引值，不包括该值，默认最大值
    step:步长，默认1
    均可选，非必填'''

li4 = ['h','o','g','w','a','r','t','s']
# print(li4[0:5:2])
# print(li4[2:4])
# print(li4[:4])
# print(li4[2:])
# print(li4[::2])
# print(li4[::-1])

'''列表事业：运算符
    重复：使用* 运算符 可以重复生成列表元素
    合并：使用+ 运算符 可以将2个列表合二为一'''
li5 = [1]
# print(li5*3)
# print(li5 + li4)

'''列表使用：成员检测
    in:检测一个元素是否在列表中，在返回True
    not in: 检测一个元素不在列表中，不在返回True'''
#print('1' not in li4)

li5.append({'a':'b'}) #todo 列表添加元素，末尾，返回None
li5.extend('hello')#todo 将一个可迭代对象添加到末尾，返回None
li5.insert(0,'male')#todo 指定位置插入,索引值 ，插入值
li5.pop() #todo 默认删除最后一个，参数：索引值
li5.remove(1)#todo 参数为：具体值，从左到右第一个开始删除


li5.sort(key=len)#todo 排序
#todo sort(key=none,reverse=False)
#todo 对列表进行原地排序，只是要《来进行各项比较
#todo key：指定带有一个参数的函数，用于从每个列表元素中提取比较值
#todo reverse:默认False表示升序 ，True为降序
#print(li5)
li5.reverse()#todo 元素顺序反转
#print(li5)
'''嵌套列表
    列表这存放列表，方法共用'''
li6 = [[1,2,3],['a','b','c'],[{'a':'c','b':'d'},'asss',22]]
#print(li6[2][0])

'''列表推导式
    循环创建列表，相当于for循环创建列表的简化版
    语法：[x for x in li if x > 1]'''
'例：将1-10中的所有偶数平方后组成新的列表'
li7 = [x**2 for x in range(1,11) if x%2==0] #todo 列表推导式
#print(li7)

result = []
for i in range(1,11):
    if i %2 ==0:
        result.append(i**2)
#print(result)

