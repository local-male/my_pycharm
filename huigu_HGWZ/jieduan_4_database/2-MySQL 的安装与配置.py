# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/26 14:39
''
'''MySQL 的安装与配置
    目录
        Mac 系统安装 MySQL
        Mac 系统环境变量配置
        Mac 系统启动与关闭 MySQL 服务
        Windows 系统安装 MySQL
        Windows 系统环境变量配置
        Windows 系统启动与关闭 MySQL 服务
        数据库的命令行操作
    
    Mac 系统安装 MySQL
        官方下载：https://dev.mysql.com/downloads/mysql/
        网盘下载：
        https://pan.baidu.com/s/1VtEXIogo_GS7iGh3f0nklw
        提取码：gxow
        安装步骤：https://ceshiren.com/t/topic/16070/4
    
    Mac 系统环境变量配置
        进入 .bash_profile 文件
        添加内容
        export PATH=$PATH:/usr/local/mysql/bin
        export PATH=$PATH:/usr/local/mysql/support-files
    
    Mac 系统启动与关闭 MySQL 服务
        系统偏好设置
        点击 MySQL 图标
        点击 Start MySQL Server 启动服务
        点击 Stop MySQL Server 关闭服务
    
    Windows 系统安装 MySQL
        官方下载：https://dev.mysql.com/downloads/cluster/
        网盘下载：
        https://pan.baidu.com/s/1VtEXIogo_GS7iGh3f0nklw
        提取码：gxow
        安装步骤：https://ceshiren.com/t/topic/16070
        
    Windows 系统环境变量配置
        新建系统变量 mysql，值为 mysql 安装路径
        path 变量中添加 %mysql%\bin
    
    Windows 系统启动与关闭 MySQL 服务
        右键此电脑选择管理
        选择服务
        找到MySQL 服务
        鼠标右键选择启动或者停止
    
    数据库的命令行操作
        开启 mysql 服务：net start mysql
        登录：mysql -h主机IP -u用户名 -p密码
        修改密码：alter user 'root'@'localhost' identified by '密码';
        退出：exit
        关闭 mysql 服务：net stop mysql
    
    
    '''