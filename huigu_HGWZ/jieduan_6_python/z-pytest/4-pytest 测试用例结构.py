# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/12/8 12:50
''
'''pytest 用例结构
    用例结构
        三部分构成
            用例名称
            用例步骤
            用例断言
    
    测试用例示例
        def test_XXX(self):
            # 测试步骤1
            # 测试步骤2
            # 断言  实际结果 对比 预期结果
            assert ActualResult == ExpectedResult
        
    类级别的用例示例
        class TestXXX:
            def setup(self):
                # 资源准备
                pass
        
            def teardown(self):
                # 资源销毁
                pass
        
            def test_XXX(self):
                # 测试步骤1
                # 测试步骤2
                # 断言  实际结果 对比 预期结果
                assert ActualResult == ExpectedResult
    
    
    '''