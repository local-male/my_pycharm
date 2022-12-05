# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/10/24 20:44
''
'''
    jenkins的安装
        jenkins包的获取
        jenkins的启动
        
    jenkins安装
        下载站点：Https://jenkins.io/download/下载.war包
        下载站点：https://jenkins.io/download/下载对应的dmg或exe文件
        国内镜像下载方式：https://mirrors.tuna.tsinghua.edu.cn/jenkins/
        docker pull jenkins/jenkins:lts
        
    jenkins启动-war包启动
        java -jar jenkins.war  (默认存储C盘，修改环境变量：jenkins_home)
        将jenkins.war放到tomcat webapps下，启动tomcat，访问localhost:8080/jenkins
            1、安装tomcat 9.0，链接：https://tomcat.apache.org/download-90.cgi
            2、安装jenkins.war 链接：Https://jenkins.io/download
            3、新建环境变量：key：JENKINS_HOME,value:路径；
            4、密码路径：F:\cache\虚拟机\tomcat\jenkins_cache\secrets\initialAdminPassword
            
        jenkins启动-docker 启动
            需要找一台装好docker 的机器
            创建volume docker volume create jenkins_1
            启动jenkins容器:docker run -d --name jenkins_1 -v jenkins_1/var/jenkins_home -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts
            jenkins 服务地址http://<linux_ip>:8080/
            进入docker容器内部找到密码，参考命令：docker exec -it jenkins_1 bash
            
    '''

'''
    linux 安装tomact
    依赖java,直接yum install -y java 安装
    1、cd /usr/local/
    2、mkdir tomcat
    3、cd tomcat
    4、xftp 将文件放至tomcat目录下
    5、解压tar -zxvf apache-tomcat-9.0.68.tar.gz，并修改名称
    6、将jenkins.war 包放到webapps下
    7、./bin/startup.sh 启动tomcat
    8、正常访问http://localhost:8080/jenkins
    
    停掉tomcat：
        1、cd /usr/local/tomcat/bin
        2、./shutdown.sh
    
    cd usr/local/tomcat/tomcat8/conf

    vi server.xml
    /8005 修改为9905
    /8080 修改为9090
    /8009 修改为9909
    
    启动停止防火墙
    service iptables stop --停止
    service iptables start --启动
    '''