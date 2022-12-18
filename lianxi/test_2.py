# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/12/15 16:42
from _pytest import python


def inc(x):
    return x + 1


def test_answer():
    assert inc(4) == 5


def test_c():
    a = 1
    b = 1
    c = 2
    assert 'abc' in "abcd"
import sys
def test_plat():
    assert ('linux' in sys.platform), "该代码只能在 Linux 下执行"


def test_b():
    a = 1
    b = 1.2
    c = 2
    assert a + b == c, f"{a}+{b}=={c}, 结果为真"
import pytest


def setup_module():
    print('模块级别的前置输入-->文件全局第一层')
def teardown_module():
    print('模块级别的后置结束-->文件全局最后一层')

def test_a():
    print('类外函数a')
def test_d():
    print('类外函数d')
def setup_function():
    print('类外函数的前置输入-->类外开始第二层')
def teardown_function():
    print('类外函数的后置结束-->类外倒数第二层')

class Test_X:
    def setup_class(self):
        print('X类内类的前置输入-->类内开始第二层')
    def teardown_class(self):
        print('X类内类的后置结束-->类内结束最后一层')
    def test_1(self):
        print('X类内函数1')
    def test_2(self):
        print('X类内函数2')
    def setup(self):
        print('X类内函数的前置输入')
    def teardown(self):
        print('X类内函数的后置结束')
class Test_Y:
    def setup_class(self):
        print('Y类内类的前置输入-->类内开始第二层')
    def teardown_class(self):
        print('Y类内类的后置结束-->类内结束最后一层')
    def test_1(self):
        print('Y类内函数1')
    def test_2(self):
        print('Y类内函数2')
    def setup(self):
        print('Y类内函数的前置输入')
    def teardown(self):
        print('Y类内函数的后置结束')


search_list = ['appium', 'selenium', 'pytest']

#todo 单参数
@pytest.mark.parametrize('name', search_list)
def test_search(name):
    assert name in search_list

#todo 多参数  值：列表中嵌套元组
@pytest.mark.parametrize("test_input,expected",[("3+5",8),("2+5",7),("7+5",12)])
def test_mark_more(test_input,expected):
    assert eval(test_input) == expected

#todo 多参数 重新命名 注意一一对应
@pytest.mark.parametrize("test_input,expected",[
            ("3+5",8),("2+5",7),("7+5",12)
        ],ids=['add_3+5=8','add_2+5=7','add_3+5=12'])
def test_mark_more(test_input,expected):
            assert eval(test_input) == expected

#todo 笛卡尔积 全量匹配 类似穷举
@pytest.mark.parametrize("wd",['a','b','c'])
@pytest.mark.parametrize("code",['1','2','3'])
def test_dhej(wd,code):
    print(f"wd:{wd},code:{code}")


#todo 标记参数用例
@pytest.mark.skip(reason='代码未实现')
@pytest.mark.order0
def test_0():
    print('0')

print(sys.platform)
@pytest.mark.skipif(sys.platform=='win32',reason='系统版本不一致')
@pytest.mark.order1
def test_1():
    print('1')

@pytest.mark.order2
def test_2():
    print('2')
# if __name__ == '__main__':
#     pytest.main(['-vs','-m','order0'])


def login():
    return True
@pytest.mark.xfail
def test_login():
    print('start')
    if not login():
        pytest.skip('原因：代码未实现；用例未输出')
    print('结束')

class Test_AS:
    @pytest.mark.xfail(reason='bug')
    def test_sa(self):
        assert 1 == 2

    @pytest.mark.xfail(reason='bug')
    def test_sb(self):
        assert 2 == 2


#todo pytest 参数验证
#todo -x   用例一旦失败(fail/error)，就立刻停止执行   pytest test_2.py::Test_x -xvs
#todo --maxfail=num 用例达到    pytest test_2.py::Test_x -vs --maxfail=2
#todo -k  执行包含某个关键字的测试用例 （用例名称）   pytest test_2.py -k 'not order'
#todo -m  标记用例 一般指装饰器标记
#todo  --collect-only（测试平台，pytest 自动导入功能 ）
class Test_x:
    def test_a(self):
        assert True

    def test_b(self):
        assert False

    def test_c(self):
        assert False

    def test_d(self):
        assert True

    def test_sss(self):
        assert False


# if __name__ == '__main__':
#     python.main(['test_2.py::Test_x','-vs','-k','sss'])


