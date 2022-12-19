# encoding='utf8'
# file->settings->Editor->file and Code Templates -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 默认测试执行器 pytest配置 ：tools->python intergrated tools-> default test runner 为pytest
# 当前时间 2022/12/19 11:03
''
'''allure报告生成
    Allure 常用命令
    
    使用 Allure2 生成精美报告
        命令格式：allure  [option]   [command]   [command options]
        
        在测试执行期间收集结果
        pytest  [测试文件] -s –q --alluredir=./result/ (—alluredir这个选项 用于指定存储测试结果的路径)
        示例：pytest test_1.py -s -q  --alluredir=./report/result/ 
        查看测试报告
        方式一：测试完成后查看实际报告， 在线看报告，会直接打开默认浏览器展示当前报告
          allure serve ./result/   (注意这里的serve书写)
          示例：allure serve /report/result 
        方式二：从结果生成报告，这是一个启动tomcat的服务，需要两个步骤：生成报告，打开报告
          生成报告 
            allure generate ./result/ -o ./report/ --clean  (注意：覆盖路径加--clean )
          打开报告 
            allure open -h 127.0.0.1 -p 8883 ./report/ 
    
    '''