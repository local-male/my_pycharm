# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/12/6 12:29
''
import json
import sys

import allure
import pytest
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

# def test_hogwarts():
#     print('hogwarts')
#
# mary = test_hogwarts
# mary()


#pip install allure-pytest


@allure.feature('模块一') #todo @allure.feature 模块
class Test_Allure:
    @allure.story('名称一') #todo @allure.story 名称
    @allure.title("标题一") #todo @allure.title 标题
    @allure.description('描述一') #todo @allure.description 描述
    def test_success(self):
        with allure.step('第一步:one'): #todo with allure.step  操作步骤
            print('第一步')
            allure.attach.file("E:\me\图片\me.jpg",name='图片',attachment_type=allure.attachment_type.PNG)
        with allure.step('第二步:two'):
            print('第二步')
        with allure.step('第三步:there'):
            print('第三步')
            assert True
    @allure.link('https://www.baidu.com',name='报告管理地址') #todo @allure.link 报告地址
    def test_failure(self):
        assert False
    @allure.issue('https://douban.com','缺陷连接')#todo @allure.issue  缺陷地址
    def test_skip(self):
        pytest.skip('跳过')
    @allure.testcase('https://taobao.com','用例链接')#todo @allure.testcase 用例地址
    def test_broken(self):
        raise Exception('异常')

@allure.feature('模块二')
@allure.severity(allure.severity_level.NORMAL) #todo @allure.severity(allure.severity_level.'级别' )  用例级别
class Test_x:
    @allure.severity(allure.severity_level.BLOCKER)
    def test_1(self):
        assert True
    @allure.severity(allure.severity_level.CRITICAL)
    def test_2(self):
        assert False
    @allure.severity(allure.severity_level.MINOR)
    def test_3(self):
        assert True
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_4(self):
        assert False



