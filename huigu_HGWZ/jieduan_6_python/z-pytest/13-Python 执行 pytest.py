# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/12/8 12:52
''
'''Python 代码执行 pytest
        使用 main 函数
        使用python -m pytest调用 pytest（jenkins持续集成用到）
    
    Python 代码执行 pytest - main 函数
        if __name__ == '__main__':
            # 1、运行当前目录下所有符合规则的用例，包括子目录（test_*.py 和 *_test.py）
            pytest.main()
            # 2、运行test_mark1.py::test_dkej模块中的某一条用例
            pytest.main(['test_mark1.py::test_dkej','-vs'])
            # 3、运行某个 标签
            pytest.main(['test_mark1.py','-vs','-m','dkej'])
         
        运行方式(在terminal中执行)
          `python test_*.py `
'''