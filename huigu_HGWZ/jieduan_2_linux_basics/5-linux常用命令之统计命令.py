# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/19 16:04
''
'''linux常用命令之统计命令
    排序：sort  对文本内容进行排序
        具体连接：https://wangchujiang.com/linux-command/c/sort.html
        使用方法：cat 文件名|sort -hnrt
    去除重复：uniq
        -c:统计重复出现的次数
        -d:所有临近的重复行只被打印一次，重复次数≥2
        -D:所有临近的重复行将全部打印
        -f:跳过对前n个列的比较
        -s:跳过对前n个字符的比较
        -w:只对每行前n个字符进行比较
        使用方法：cat 文件名|sort | uniq -c 
    字符统计：wc
        -c:统计字节数：chars
        -l:统计行数
        -w:统计单词数
        -L:打印最长行的长度
        使用方法：cat 文件名|wc （默认参数clw）
    
    
    '''