# encoding='utf8'
# file->settings->Editor->file and Code Templates -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 默认测试执行器 pytest配置 ：tools->python intergrated tools-> default test runner 为pytest
# 当前时间 2022/12/18 15:52
''
import json


# def test_json():
#     with open('../data/demo.json', 'r', encoding='utf-8') as f:
#         data = json.loads(f.read())
#         print(data,type(data))   #字典  下面转译
#         print(json.dumps(data,ensure_ascii=False),type(json.dumps(data))) # 字符串


# 读取json文件
def get_json():
    """
    获取json数据
    :return: 返回数据的结构：[[1, 1, 2], [3, 6, 9], [100, 200, 300]]
    """
    with open('../data/demo.json', 'r',encoding='utf-8') as f:
        data = json.loads(f.read())
        print(list(data.values()))
        return list(data.values())

def my_add(a,b):
    return  a+b
