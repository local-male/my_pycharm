# encoding='utf8'
# file->settings->Editor->file and Code Templates -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 默认测试执行器 pytest配置 ：tools->python intergrated tools-> default test runner 为pytest
# 当前时间 2022/12/19 11:04
''
'''allure pytest 报告中添加附件
    
    Allure 特性 - 测试报告中添加附件
        场景：
        希望在报告中看到测试用例的详细内容展示
        比如在用例中添加附件信息，可以是数据，文本，图片，视频，网页
        
        解决:
        @allure.attach显示许多不同类型的提供的附件，可以补充测试，步骤或测试结果。
        用法：
        allure.attach(body(内容), name, attachment_type, extension):
    
    Allure 总结
        ⽀持多平台
        Java语⾔开发的，⽀持多语言 pytest，JaveScript, PHP, ruby 等
        可以为dev/qa提供详尽的的测试报告、测试步骤、log、标题、优先级、附件等等
        也可以为管理理层提供high level统计报告
        可以集成到Jenkins，展示项目的趋势图
'''