# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 当前时间 2022/10/17 12:36
''
import random

'''python控制流-分支判断
    一条一条语句顺序指向叫做顺序结构
    分支结构就是在某个判断条件后，选择一个分支去执行
    if 条件判断'''
#achievement = random.randint(40,100)
# print(achievement)
# if 60 <= achievement <80 :
#     print('yes')
# elif 80<= achievement :
#     print('good')
#     if isinstance(achievement,int) : #TODO 判断字符类型
#         print('yyds')
# else:
#     print('no')

'''三目运算符'''
a , b = 1,2
if a>b:
    h = '变量1'
else:
    h = '变量2'
print(h)
h = '1'if a>b else '2' #todo  赋值语句放在前面，if判断条件 else赋值
print(h)


