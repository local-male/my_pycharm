# encoding='utf8'
# file->settings->Editor->file and Code Templates -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 默认测试执行器 pytest配置 ：tools->python intergrated tools-> default test runner 为pytest
# 当前时间 2022/12/20 10:47
''
import logging
import pytest


# @pytest.fixture(scope='function')#module session function class
# def login():
#     print('登录成功')
#     token = '1615316921'
#     yield token
#     print('退出登录')



@pytest.fixture(params=['male','tom','yily'])
def search(request):
    logging.info(request.param)
    yield request.param
def test_cart(search):
    logging.info(f'命名：{search}')
def test_order(login):
    logging.info('下单')

class TestDemo:
    def test_case_1(self,login):
        logging.info(f'token:{login}')
        logging.info('case_1')
    def test_case_2(self):
        logging.info('case_2')

