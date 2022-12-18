# encoding='utf8'
# file->settings->Editor->file and Code Templates -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 默认测试执行器 pytest配置 ：tools->python intergrated tools-> default test runner 为pytest
# 当前时间 2022/12/18 16:09
''
import pytest
from lianxi.Data_driven.file_json.func.test_json import my_add, get_json
class TestWithJSON:
    @pytest.mark.parametrize('x,y,expected', get_json())
    def test_add(self, x, y, expected):
        assert my_add(int(x), int(y)) == int(expected)
