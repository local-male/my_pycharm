# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/12/8 12:50
''
'''pytest 用例断言
    pytest 测试用例断言
        什么是断言
        断言的用法
    
    什么是断言
        断言(assert)，是一种在程序中的一阶逻辑(如：一个结果为真或假的逻辑判断式)，
        目的为了表示与验证软件开发者预期的结果。当程序执行到断言的位置时，对应的断言应该为真。
        若断言不为真时，程序会中止执行，并给出错误信息。
    
    断言的用法
        断言写法
        assert <表达式>
        assert <表达式>,<描述>
        assert <bool expression>;       
        assert <bool expression> : <message>; 
    
    示例 1
        第一种：assert <表达式>
        第二种：assert <表达式>,<描述>
        def test_a():
            assert True
        
        def test_b():
            a = 1
            b = 1
            c = 2
            assert a + b == c, f"{a}+{b}=={c}, 结果为真"
    
    示例 2
        assert <表达式>
        def test_c():
            a = 1
            b = 1
            c = 2
            assert 'abc' in "abcd"
        
        import sys
        def test_plat():
            assert ('linux' in sys.platform), "该代码只能在 Linux 下执行"
    '''