# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 当前时间 2022/10/17 15:12
''
import random

'''python控制流-循环
    循环语句允许我们执行一个语句或语句组多次
    python提供了for循环和while循环
    
    封装重复操作
    python最重要的基础语法之一'''
'''for in 循环
    使用场景：
        明确知道循环执行的次数或者哟啊对一个容器进行迭代
    range函数
        range（101）可以产生一个0-100的整数序列
        range(1,100,2)可以产生一个1-99的奇数序列
    '''
# for i in range(1,10,3):
#     print(i)

'''while 循环
    满足条件，进入循环
    需要设定好循环结束条件'''
# count = 0
# while count<5:
#     count += 1
#     if count ==3:
#         continue
#     if count ==4:
#         break
#     print(count)

#todo break 跳出整个循环体
#todo continue  跳出当前当次循环

# for i in range(8):
#     if i == 4:
#         continue
#     elif i == 6:
#         break
#     print(i)

'''pass
    没有实际意义，占位符
    不影响代码执行'''
'1-100求和'
# a = 0
# for i in range(0,101,2):#使用步长
#     a = a + i
# print(a)
# b = 0
# for i in range(1,101):#使用分支结构
#     if i %2 == 0:
#         b = b + i
# print(b)

'1-100的随机数字'
# sum1 = random.randint(1,101)
# while True:
#     sum = int(input('请输入数字：'))
#     if sum > sum1:
#         print('小一点')
#     elif sum < sum1:
#         print('大一点')
#     else:
#         print(sum)
#         print('猜对了')
#         break
