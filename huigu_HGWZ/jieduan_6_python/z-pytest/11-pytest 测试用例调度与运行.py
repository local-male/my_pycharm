# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/12/8 12:51
''
'''pytest 测试用例调度与运行
    
    命令行参数-使用缓存状态
        --lf（--last-failed） 只重新运行故障。
        --ff（--failed-first） 先运行故障然后再运行其余的测试
    
    先正常执行pytest,结束后用例有执行失败、成功等；在执行下面的
    pytest --lf
    pytest --ff

'''