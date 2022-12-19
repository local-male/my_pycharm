# encoding='utf8'
# file->settings->Editor->file and Code Templates -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 默认测试执行器 pytest配置 ：tools->python intergrated tools-> default test runner 为pytest
# 当前时间 2022/12/19 11:03
''
'''Allure 合并报告
    
    Allure 两种执行方法
        方式一：通过 allure serve 将结果数据解析为在线报告
        方式二：通过 allure generate 命令生成最终的报告，然后通过 allure open 命令打开报告
        # 方式一
            allure serve ./result
        示例：allure serve ./report/result ./report/result2
        # 方式二
            allure generate -c -o ./allure-report ./result
            allure open ./allure-report
        # -c 在生成报告之前清空报告中的内容，默认是不清空
        # -o 生成报告的目录，默认: allure-report
        
    Allure 合并报告
        方式一：通过 allure serve 命令解析结果时合并结果展示
        方式二：通过 allure generate 命令合并报告
        # 方式一
            allure serve ./result1 ./result2 ./result3
        
        # 方式二
            allure generate -c -o ./allure-report ./result1 ./result2 ./result3
            allure open ./allure-report
    

    '''