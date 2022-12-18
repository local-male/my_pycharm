# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/12/8 12:51
''
'''运行用例
    运行多条用例
        运行 某个/多个 用例包
        运行 某个/多个 用例模块
        运行 某个/多个 用例类
        运行 某个/多个 用例方法
    
    运行多条用例方式
        执行包下所有的用例：pytest/py.test [包名]
        执行单独一个pytest模块：pytest 文件名.py
        运行某个模块里面某个类：pytest 文件名.py::类名
        运行某个模块里面某个类里面的方法：pytest 文件名.py::类名::方法名 ：
    
    运行结果分析
        常用的：fail/error/pass   失败/报错/通过
        特殊的结果：warning/deselect（后面会讲）  警告/跳过，未被选中
    
    
    '''