# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/19 17:58
''
'''linux 三剑客与管道使用
    程序运行环境输入与输出
        标准输入0
            read a; echo $a
        标准输出1
            echo ceshiren.com
        错误输出
            ls not_exist_dir
    
    管道执行的撒谎给你下文控制
        使用{command;}注意花括号与内部命令之间的空格与分号
        使用控制逻辑while read 组合
        使用$()''    
    
    grep 基于正则表达式查找满足条件的行
    awf  定位到的数据行处理其中的分段
    sed  根据定位的数据行修改数据   
            
    与sql的对比
        linux三剑客                sql
        grep数据查询定位             select * from table
        awk 数据切片                select field from table
        sed 数据修改                update table set a=new where a=old
    
    
    '''