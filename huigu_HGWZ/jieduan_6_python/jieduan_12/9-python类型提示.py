# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 当前时间 2022/10/21 1:07
''
from typing import List

'''python类型提示  3.5版本后支持
    链接：https://docs.python.org/zh-cn/3/library/typing.html
    1、增强代码的可读性
    2、ide中代码提示
    3、静态代码检查'''

def greeting(name:str)->str:#todo 括号中的str 代表 传参的类型
                        #todo -> str 代表返回值的类型
    print(name.split(','))
    return 'hello:'+ name.split(',')[0]
#print(greeting('python'))

# name = ',python,'
# print(name.split(','))
#结果：['', 'python', '']

vector = List[float] #todo 列表中全是浮点数
def scale(scalar:float,vector:vector)->vector:
    return [scalar * num for num in vector]

#print(scale(1.2, [0.5, 0.4, 2.1, 4.5]))

'自定义类型'
class student:
    name:str
    age:int

def get_stu(name:str)->student:
    return student()

#print(get_stu('name'))

'安装 mypy:pip install mypy' #todo 检查代码中的问题
#执行：mypy 文件名.py
#  mypy .\9-python类型提示.py
# Success: no issues found in 1 source file

