# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/12/8 12:51
''
''' 使用 Mark 标记测试用例
    场景:只执行符合要求的某一部分用例 可以把一个web项目划分多个模块，然后指定模块名称执行。
    解决: 在测试用例方法上加 @pytest.mark.标签名
    执行: -m 执行自定义标记的相关用例
        pytest -s test_mark_zi_09.py -m=webtest
        pytest -s test_mark_zi_09.py -m apptest
        pytest -s test_mark_zi_09.py -m "not ios"

    #todo 标记参数用例
    @pytest.mark.order0
    def test_0():
        print('0')
    
    @pytest.mark.order1
    def test_1():
        print('1')
    
    @pytest.mark.order2
    def test_2():
        print('2')
    if __name__ == '__main__':
        pytest.main(['-vs','-m','order0'])  待验证
    
    
    
    '''