# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/12/8 12:51
''
'''Mark：跳过(Skip)及预期失败(xFail)
        这是pytest 的内置标签，可以处理一些特殊的测试用例，不能成功的测试用例
        skip - 始终跳过该测试用例
        skipif - 遇到特定情况跳过该测试用例
        xfail - 遇到特定情况,产生一个“期望失败”输出
    
    Skip 使用场景
    调试时不想运行这个用例
    标记无法在某些平台上运行的测试功能
    在某些版本中执行，其他版本中跳过
    比如：当前的外部资源不可用时跳过
        如果测试数据是从数据库中取到的，
        连接数据库的功能如果返回结果未成功就跳过，因为执行也都报错
    解决1：添加装饰器
        @pytest.mark.skip
        @pytest.mark.skipif
        
    @pytest.mark.skip(reason='代码未实现')
    def test_0():
        print('0')
    
    @pytest.mark.skipif('判断条件','备注') 条件为真则不执行，否则执行用例
    def test_1():
        print('1')
    
    解决2：代码中添加跳过代码
        pytest.skip(reason=‘代码未实现’)
    
    def login():
        return False
    def test_login():
        print('start')
        if not login():
            pytest.skip('原因：代码未实现；用例未输出')
        print('结束')
    
    
       
    xfail 使用场景
        与skip 类似 ，预期结果为fail ，标记用例为fail
        用法：添加装饰器@pytest.mark.xfail
    
    class Test_AS:
        @pytest.mark.xfail(reason='bug')
        def test_sa(self):
            assert 1 == 2
        
        @pytest.mark.xfail(reason='bug')
        def test_sb(self):
            assert 2 == 2
            
    '''