# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/19 16:54
''
'''linux三剑客之grep
    
    获取行 grep 查询值   查询文件
    获取内容 grep -o 查询值   查询文件
    获取上下文 grep -A -B -C 查询值   查询文件
    
    文件检索
        递归搜索 grep 查询值 -r  查询文件
        展示匹配文件名 grep -H 匹配值 查询文件
        只展示匹配文件名 grep -l 匹配值  查询文件
    
    范围约束
        忽略大小写  grep -i 查询值  查询文件
        不显示匹配的行  grep -v 查询值  查询文件
        使用扩展正则表达式  grep -E 查询值  查询文件
        文件范围和目录范围约束 grep 查询值  -r 路径 --include "11*"
    
    进程检索
        进程过滤场景比较特殊，需要注意
        grep 本身会开启新进程，所有需要单独过滤掉grep进程
        ps -ef|grep ssh
        结果会显示ssh、grep2个进程
        ps -ef|grep ssh |grep -v grep 
        只显示ssh一个进程
    
    
    '''