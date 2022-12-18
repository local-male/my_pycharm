# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/12/8 12:50
''
'''Pytest 测试框架结构（setup/teardown）
    
    测试装置介绍
        类型	                                规则
        setup_module/teardown_module	    全局模块级
        setup_class/teardown_class	        类级，只在类中前后运行一次
        setup_function/teardown_function	函数级，在类外
        setup_method/teardown_methond	    方法级，类中的每个方法执行前后
        setup/teardown	                    在类中，运行在调用方法的前后（重点）
    
    
    '''