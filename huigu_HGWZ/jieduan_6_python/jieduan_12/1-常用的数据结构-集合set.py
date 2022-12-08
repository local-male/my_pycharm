# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 当前时间 2022/10/18 19:17
''
'''常用的数据结构-集合set
    集合定义与使用
    集合常用方法
    集合推导式
    
    集合定义：无序的唯一对象集合
            用大括号{}包围，对象相互之间使用逗号分隔
            集合是动态的，可以随时添加和删除元素
            集合是异构的，可以包含不同类型的数据'''

'''集合使用：创建
    通过使用{}填充元素
    通过构造方法
    通过集合推导式'''
set1 = {1,2,3}
#print(type(set1),set1)
set2 = set('sdada')#todo 可迭代对象（可以使用for循环） list tuple dict str
#print(type(set2),set2)
set3 = {i for i in range(0,11,2)}#todo 集合推导式
#print(set3)

'''集合使用：成员检测
    in：判断元素是否在集合中存在
    not in 判断元素是否在集合中不存在'''
# print(2 not in set3)
# print('x'  in set3)

'集合方法'
set3.add('x')#todo 添加元素,位置随机
#print(set3)
set3.update('ssxf')#todo 添加可迭代对象，批量添加
#print(set3)
set3.remove('x')#todo 删除指定元素,不存在会报错，集合中元素不会重复
#print(set3)
set3.discard('k')#todo 删除指定元素，不存在不会报错
#print(set3)
set3.pop()#todo 随机删除一个元素，集合为空会报错
#print(set3)
set3.clear()#todo 情况所有元素
#print(set3)

'''集合运算
    交集运算 &  intersection()
    并集运算 |  union()
    差集运算'''
set4 = {1,2,3}
set5 = {2,3,4}
# print(set4.intersection(set5))#todo 打印交集元素
# print(set4 & set5)
# print(set4.union(set5))#todo 打印出全部元素 并集
# print(set4 | set5)
# print(set5.difference(set4)) #TODO 差集 A-B，剩下的A中的元素
#print(set4-set5)

'''集合推导式
    类似列表推导式，同样集合支持集合推导式
    语法：{x for x in xx if x == x}'''
set6 = set()
for i in 'hogwarts':
    if i in 'hello world':
        set6.add(i)# update 结果一致
#print(set6)
print({i for i in 'hogwarts' if i in 'hello world'})


