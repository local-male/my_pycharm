# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/10/24 22:08
''
'''
    目录：
        任务配置组成
        常用配置项
        
    任务配置
        任务时jenkins的狠心功能，决定了jenkins怎么去执行
        
    创建任务
        路径Dashboard->新建任务
    
    jenkins切换中文
        1、Manage jenkins-》Manage Plugins，搜索locale、Localization Chinese；
        2、安装完成后选择重启；
        3、进入系统管理Manage Jenkins > Configure System,设置 Language为zh_cn
    任务配置组成
        常规general
            描述
            丢弃旧的构建
            参数构建过程
            关闭构建
            在必要的时候并发构建
            静默期
            重试次数
            该项目的上游项目正在构建时阻止构建
            该项目的下游项目正在构建时阻止构建
            事业自定义的工作空间
            显示名称
        源码管理
            无
            git
                仓库（repository）
                构建分支(branches to build)
                源码库管理器
                附加行为（additional behaviours）
        构建触发器
            触发远程构建
            其他工程构建后出发
            定时构建
            轮询scm
        构建环境
            use secret test(s) or file(s)?
        构建
            执行windows批处理命令
            执行shell
            调用顶层maven目标
        构建后动作
            归档成品
            构建其他工程
            记录文件的指纹用于追踪
            git publisher
            e-mail notification
        '''

