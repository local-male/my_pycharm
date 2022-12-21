# encoding='utf8'
# file->settings->Editor->file and Code Templates -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 默认测试执行器 pytest配置 ：tools->python intergrated tools-> default test runner 为pytest
# 当前时间 2022/12/21 12:05
''
#todo 固定名称
#优先从conftest中查找对应文件
import pytest
@pytest.fixture(scope='session',autouse=True)#module session function class
def login():
    print('登录成功')
    token = '1615316921'
    yield token
    print('退出登录')

