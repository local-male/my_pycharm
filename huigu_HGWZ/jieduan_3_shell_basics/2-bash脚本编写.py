# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/22 21:44
''
#todo  指定文件为bash  #!/bin/bash
'''bash脚本编写
    
    read命令 
        read命令是用于从终端或者文件中读取输入的内部命令
        读取整行输入
        每行末尾的换行符不被读入
    
    read命令使用
        从标准输入读取输入并赋值给变量
        read var
        从标准输入读取多个内容
        read var1 var2 var3
        不指定变量（默认赋值给REPLY）
        read
        
            使用：read a b c 
                 1 2 3
                echo $a$b$c  结果：123
                read
                sss
                echo $REPLY 结果：sss
        
    脚本参数传递
        $0 脚本文件名称
        $1~$n 获取参数
        $# 传递到脚本的参数个数
        $$ 脚本运行的当前进程ID号
        $* 以一个单字符传显示所有向脚本传递的参数
        $? 显示最后命令的退出状态。 0表示没有错误，其他任何表面都有错误
    
    基本运算   符号为1左边的符号
    + 加法 ’expr $a + $b‘  
    - 减法 ’expr $a - $b‘  expr $a - $b
    * 乘法 ’expr $a \* $b‘
    / 除法 ’expr $a / $b‘
    % 取余 `expr $a % $b`
    = 赋值 a = $b 将把变量b的值赋值给a
    == 等于 相同结果返回true，【$a = $b】 返回flase  [ $a == $b ]
    ！= 不等于 不相同则返回true【$a != $b】 返回true
    
    -eq 检测相等 [ $a -eq $b ] 返回flase
    -ne 检测不相等 [ $a -ne $b ] 返回true
    -gt 检测左边是否大于右边 [ $a -gt $b ] 返回flase
    -lt 检测左边是否小于右边 [ %a -lt %b ] 返回true
    -ge 检测左边是否大于等于右边 [ $a -ge $b ] 返回flase
    -le 检测左边是否小于等于右边 [ $a -le $b ] 返回true
    
    bash与linux的命令组合
        创建目录并生成文件
        mkdir test
        cd test
        echo 'hello' > tets.txt
        ls
    
    bash与内存
        统计内存使用
        for i in ’ps aux |awk '{print $6}'|grep -v 'RSS'‘
            count=$[$count+$i]
        echo "$count/kb"
    
    
    
        '''