# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 当前时间 2022/10/18 19:53
''
'''常用的数据结构-字典 dict
    字典是无序的键值对集合
    字典用大括号{}包围
    各个键/值之间用一个逗号分隔
    各个键与值之间用冒号分隔
    字典是动态的'''
'''字典使用：创建
    使用大括号填充键值对
    通过构造方法dict()
    使用字典推导式'''
dict_1 = {'one':'马云','two':'马化腾','there':'马斯克'}
#print(dict(),type(dict()))
dict_2 = dict([('one','马云'),('two','马化腾')])#todo 格式有要求
#print(dict_2,type(dict_2))
dict_3 = {key:value for key,value in [('one','马云'),('two','马化腾')] }#todo 字典推导式
#print(dict_3,type(dict_3))

'''字典使用：访问元素
    字典支持中括号记号[key]
    字典使用键来访问其关联的值
    访问时对应的key必须要关联'''
#print(dict_1['one'])

'''字典使用：操作元素
    语法：dict[key] = value
    添加元素：键不存在
    修改元素：键以及存在'''
dict_1['four'] = 'male'
#print(dict_1)

'''字典使用：嵌套字典
    字典的值可以是字典对象'''
dict_4 = {'one':{'on':'1','in':'2'}}
#print(dict_4['one']['in'])

#print(dict_1.keys())#todo 返回由字典键组成的一个新视图对象
#print(dict_1.values())#todo 支持成员检测  in  ，not in
#print(dict_1.items())#todo
#print(list(dict_1.items()))#todo 可以转换list
#print(dict_1.get('on1e'))#todo 获取key对应的值，不存在不会报错
#print(dict_1)
dict_1.update({'one':'s','two':'22'})#todo  存在key 为编辑，不存在则新增
#print(dict_1)
dict_1.pop('four')#todo 删除指定key
#print(dict_1)

'''字典推导式
    可以从任何已键值对作为元素的可迭代对象中构建出字典
    例：{'a':1,'b':2,'c':3} ,找出其中所有大于1的键值对，
    同时value值进行平方运算'''

dict_5 = {k:v**2 for k,v in [('a',1),('b',2)]  }
#print(dict_5)

dict_6 = {'a':1,'b':2,'c':3}
# for k,v in dict_6.items():
#     if v > 1:
#         dict_6[k] = v**2
#print(dict_6)

dict_7 = {k:v for k,v in dict_6.items() if v >1}#TODO 字典推导式
#print(dict_7)

'''给定一个字典对象，请使用字典推导式，
将key和value分别进行交换'''
dict_8 = {v:k for k,v in dict_7.items()}
#print(dict_8,type(dict_8))


