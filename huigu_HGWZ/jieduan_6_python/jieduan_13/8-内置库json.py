# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/10/22 23:14
''
import os

'''内置库json
    json是用于存储和交换数据的语法，是一种轻量级的数据交换格式
    使用场景：
        接口数据传输
        序列化
        配置文件'''

'''json结构
    键值对形式
    数组形式'''
x = {
    "language": [
        {
            "name": "python",
            "url": "https://www.python.org/"
        },
        {
            "name": "java",
            "url": "https://www.java.com/zh-CN/"
        }
    ]
}

'''json 库
可以从字符串或文件中解析 JSON
该库解析 JSON 后将其转为 Python 字典或者列表'''


'''常用方法
    dumps()：将 Python 对象编码成 JSON 字符串
    loads()：解码 JSON 数据，该函数返回 Python 对象
            与字符串之间的一个交互
    dump()： Python 对象编码，并将数据写入 json 文件中
    load()：从 json 文件中读取数据并解码为 Python 对象
            与文件之间的交互
    '''#todo json
import json

# 定义 python 结构
data = {'a': 1, 'b': '胡是', 'c': True, 'd': False, 'e': None }

# 将 python 对象编码为 JSON 字符串
                            #编码                缩进
json_data = json.dumps(data,ensure_ascii=False,indent=4)#todo
print(json_data,type(json_data))
# 将 JSON 字符串解码为 python 对象
python_data = json.loads(json_data)#todo
#print(python_data,type(python_data))
# 写入 JSON 数据，在代码当前目录生成一个 data.json 的文件
dirpath = os.path.dirname(__file__)
newpath = os.path.join(dirpath, 'files', 'data.json')
# with open(newpath, 'w') as f:
#      json.dump(data, f)#todo
# 读取数据，读取 json 文件并解码成 python 对象
# with open('files/data.json', 'r') as f:
#     data = json.load(f)#todo
#     print(data,type(data))


#todo indent：根据数据格式缩进显示，默认为 None，没有缩进
#todo ensure_ascii：对中文使用 ASCII 编码，默认为 True


