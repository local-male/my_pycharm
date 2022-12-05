# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/24 17:10
''
#todo linux_bash 试题
''''
一、（单选,Linux与Bash课程）如何查看当前用户运行的所有进程信息？
         选项A：ps -a
         选项B：ps -u 【正确答案】 Linux常用命令(文件/网络/性能)
         选项C：ls - l
         选项D：ls -x
         
二、 （单选,Linux与Bash课程）如何查看文本文件的第二列内容?（指定空格为分隔符）
         选项A：awk -F ":" '{print $2}'
         选项B：awk -F "" '{print $0}'
         选项C：awk '{print $1}'
         选项D：awk -F "" '{print $2}' 【正确答案】      
    
三、 （多选,Linux与Bash课程）如何替换一个文本文件内root关键字为大写的ROOT，
    不管root关键字出现多少次都替换它并写入原文件，下面哪些命令是正确的？
         选项A：sed -i "s/root/ROOT/" file.txt
         选项B：sed -i "s/root/ROOT/g" file.txt 【正确答案】
         选项C：awk '{gsub(/root/,"ROOT"); print $0 }' file.txt > file.txt 【正确答案】
         选项D：awk '{sub(/root/,"ROOT"); print $0 }' file.txt < file.txt
         
四、 （单选,Linux与Bash课程）查看文件/etc/passwd 中包含 root 的行
         选项A：grep root /etc/passwd 【正确答案】 grep 的用法，知识点：查找某个数据包含某个字符
         选项B：grep ^root /etc/passwd
         选项C：grep root$ /etc/passwd
         选项D：grep ^root$ /etc/passwd
         
         
五、（多选,Linux与Bash课程）找出文件/etc/passwd 文件中所有以 `nologin` 结尾的用户
         选项A：cat /etc/passwd|grep nologin$ 【正确答案】
         选项B：grep ^nologin$ /etc/passwd
         选项C：grep nologin$ /etc/passwd 【正确答案】 grep 的用法，知识点：$以某个字符结尾，正则表达式
         选项D：以上写法都不正确
 
六、 多选,Linux与Bash课程）下面前于sed的说法正确的是
         选项A：sed 是Linux下一款功能强大的非交互流式文本编辑器 【正确答案】
         选项B：一次能处理多个文件
         选项C：sed 特别适合于大文件的编辑 【正确答案】
         选项D：sed 可以对文本文件进行增、删、改、查等操作 【正确答案】   
         sed 知识点，概念：sed 是Linux下一款功能强大的非交互流式文本编辑器，
         一次能处理一行内容，可以对文本文件进行增、删、改、查等操作，特别适合于大文件的编辑    
    
七、（单选,Linux与Bash课程）在文件 test.txt 第四行后面新增一条数据`newline` ，下面写法正确的是：
         选项A：sed -e '4 a newline' test.txt 【正确答案】
         选项B：sed -e '4 c newline' test.txt
         选项C：sed -e '4 i newline' test.txt
         选项D：sed -e '4 d newline' test.txt
         
         sed 知识点，概念：a 在后面新增， i 在前面新增一行，c取代，d删除
    
八、（多选,Linux与Bash课程）如何关闭一个指定的进程，例如：“java”？
         选项A：ps -ef|grep java|awk '{print $2}'|xargs kill -9 【正确答案】
         选项B：ps aux|sed -o '/java/p'|awk '{print $2}|xargs kill
         选项C：ps aux|sed -n '/java/p'|awk '{print $2}|xargs kill 【正确答案】
         选项D：ps -ef|grep -v java|awk '{print $1}'|xargs kill -9 
         
         Linux常用命令(文件/网络/性能) 
         
九、（单选,Linux与Bash课程）如何统计服务器网络，当前tcp连接状态？
         选项A：netstat -n | awk '/^tcp/ {++status[$NF]} END {for(num in status) print num, 
                status[num]}' 【正确答案】
         选项B：netstat -n | awk '/udp/ {++s[$NF]} END {for(n in s) print n, s[n]}'
         选项C：netstat -n | awk '/tcp/ {++statu[$NF]} END {for(num in status) print num, 
                status[num]}'
         选项D：netstat -n | awk '/udp$/ {++s[$NF]} END {for(n in s) print n, s[n]}'    

十、（多选,Linux与Bash课程）如何显示hogwarts.txt的3-5行与15行？
         选项A：sed -n "3,5p;15p" hogwarts.txt 【正确答案】
         选项B：awk 'NR==3||NR<5||NR=15{print $0}' hogwarts.txt
         选项C：sed -n "3-5p;15p" hogwarts.txt
         选项D：awk 'NR==3||NR==4||NR==5||NR==15{print $0}' hogwarts.txt 【正确答案】
    
         
         
           
    '''