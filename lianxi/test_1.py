# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/12/6 12:29
''
import json
import urllib3

# def test_HTTP():
#     # 创建连接池对象，默认会校验证书
#     pm = urllib3.PoolManager()
#     # 发送HTTP请求
#     resp = pm.request(method='GET', url="http://httpbin.org/robots.txt")
#
#     # print(type(resp))
#     # print(resp.status)  # 查看响应状态状态码
#     # print(resp.headers)  # 查看响应头信息
#     # print(resp.data)  # 查看响应原始二进制信息
#
#     abc = resp.data
#     #print(type(abc),abc)
#     content = abc.decode('utf-8')
#     #print(type(content),content)
#     json_content = json.dumps(content)
#     #print(type(json_content),json_content)
#     json_content_1 = json.loads(json_content)
#     #print(type(json_content_1),json_content_1)

def test_hogwarts():
    print('hogwarts')

mary = test_hogwarts
mary()