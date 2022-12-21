# encoding='utf8'
# file->settings->Editor->file and Code Templates -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 默认测试执行器 pytest配置 ：tools->python intergrated tools-> default test runner 为pytest
# 当前时间 2022/12/19 19:41
''
'''pytest.ini 配置
    
    pytest.ini 是什么
        pytest.ini 是pytest 的配置文件
        可以修改 pytest 的默认行为
        不能使用任何中文符号，包括汉字、空格、引号、冒号等等
    
    pytest.ini
        修改用例的命名规则
        配置日志格式，比代码配置更方便
        添加标签，防止运行过程报警告错误
        指定执行目录
        排除搜索目录
    
    pytest 配置- 改变运行规则
        ;执行check_开头和 test_开头的所有的文件，后面一定要加*
        python_files = check_* test_*
        ;执行所有的以Test和Check开头的类
        python_classes = Test*  Check*
        ;执行所有以test_和check_开头的方法
        python_functions= test_* check_*
    
    pytest 配置- 添加默认参数
        addopts = -v -s --alluredir=./results
    
    pytest 配置- 指定/忽略执行目录
        ;设置执行的路径
        ;testpaths = bilibili baidu
        ;忽略某些文件夹/目录
        norecursedirs = result logs datas test_demo*
    
    pytest 配置- 日志
        配置参考链接：https://ceshiren.com/t/topic/13105
    
    总结 pytest.ini
        修改用例的命名规则
        配置日志格式，比代码配置更方便
        指定执行目录
        排除搜索目录
        添加标签，防止运行过程报警告错误
        添加默认参数
    
    
    '''