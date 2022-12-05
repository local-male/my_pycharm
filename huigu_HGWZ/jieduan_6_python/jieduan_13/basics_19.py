# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/10/21 12:15

''
'''python 错误与异常
    语法错误与定位
    异常捕获、异常处理
    自定义异常
    错误：语法错误 逻辑错误 系统错误'''
#todo 语法错误 SyntaxError
num = 'a'
# if num > 1
#     print(num)


#todo 逻辑错误
# if num >= 1:
#     print('num < 1')
# else:
#     print('sb')

'''异常
    程序执行过程中出现的位置错误
    语法和逻辑都是正常的
    程序业务逻辑不完善引起的程序漏洞'''

'''异常与错误区别
    异常可以被捕获和处理
    错误一般是编码、逻辑、系统错误'''


def div(a,b):
    # try:
    return a / b
    # except(ZeroDivisionError) as e:
    #     print(f'异常为：{e}')
#div(1,0)#todo ZeroDivisionError  除零异常

'异常链接：https://docs.python.org/3/library/exceptions.html#bltin-exceptions'
#常见异常类型：除零异常、名称异常、索引异常、键异常、值异常、属性异常等

dict1 = {'name':'male'}
#print(dict1['key'])#todo keyerror 键异常
list1 = [1,2,3]
#print(list1[4])#todo IndexError  索引异常
#print(int(num))#todo ValueError 值异常

#print(ab)#todo NameError  名称异常

def div1(a,b):
    try:
        print(a/b)
        return a / b
    except Exception(ZeroDivisionError) as e:#todo 捕获异常
        print(f'异常为：{e}')
    except Exception(TypeError) as f:
        print(f'异常为：{f}')
    else: #没有发生异常执行的代码
        print('没有异常')
    finally:#一般执行关闭文件
        print('操作完成')
#div1('a',0)
#div1(2,3)

'''自定义异常'''#todo
class MYError(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)




