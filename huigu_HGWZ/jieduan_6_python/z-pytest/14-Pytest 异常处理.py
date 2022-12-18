# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/12/8 12:52
''
'''常用的异常处理方法
        try…except
        pytest.raises()
    
    异常处理方法 try …except
        try:
            可能产生异常的代码块
        except [ (Error1, Error2, ... ) [as e] ]:
            处理异常的代码块1
        except [ (Error3, Error4, ... ) [as e] ]:
            处理异常的代码块2
        except  [Exception]:
            处理其它异常
    
    异常处理方法pytest.raise()
        可以捕获特定的异常
        获取捕获的异常的细节（异常类型，异常信息）
        发生异常，后面的代码将不会被执行
    
    异常处理方法pytest.raise()
        def test_raise():
            with pytest.raises(ValueError, match='must be 0 or None'):
                raise ValueError("value must be 0 or None")
         
        def test_raise1():
            with pytest.raises(ValueError) as exc_info:
                raise ValueError("value must be 42")
            assert exc_info.type is ValueError
            assert exc_info.value.args[0] == "value must be 42"
'''