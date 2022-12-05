# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/19 17:59
''
'''三剑客实战之 nginx日志分析实战
    
    编写一个函数 find_error_log()找出log中的404 500的报错 考察严谨性
    格式：find_error_log() {}
    find_error_log（）
{
grep 'HTTP/1.1" 404' nginx.log
grep 'HTTP/1.1" 500' nginx.log
}



    '''