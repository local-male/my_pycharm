# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/19 10:17
''
'''linux 常用命令文件处理
    连接服务器
        mac/linux 系统，终端执行
            ssh -p22 用户名@地址，最后输入密码
            ck245849@shell.ceshiren.com ~]$    ~ 家目录  $当前用户的身份 普通用户
        帮助命令  ls --help  ; man ls
    文件
        第一个字母文件类型： d目录 -文件  ;rwx 421
        屏幕输出：echo
        输出重定向：>
        操作：echo  文本内容  > 文件名
        
    网络
        ping -c次数 3 -i(时间s) 3 ip
        netstat -t(列出所有tcp) -n(以数字形式显示地址和端口号)  -p(显示进程的pid和名字)
        exit 退出
    '''