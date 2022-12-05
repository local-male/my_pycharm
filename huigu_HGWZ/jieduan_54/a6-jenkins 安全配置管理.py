# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/10/25 14:15
''
'''
    目录
        安全配置介绍
        安全配置选项详解
    
    安全配置管理
        jenkins拥有良好的扩展性，如远程执行、接口调用等，但需要考虑到网络
        安全的因素，所有jenkins将这些功能配置化，按照设置；
    
    全局安全配置
        菜单：面板/系统管理/安全/全局安全配置
        配置项：
            认证（authentication）
                不要记住我
                安全域
                    jenkins专有用户数据库
                    servlet容器代理
                    None
                    授权策略
                        任何用户可以做任何事
                        登录用户可以做任何事
                        遗留模式
            标记格式器（纯文本、html等）
            代理
                代理的tcp端口
                    指定端口
                    随机选取
                    禁用
            跨站请求伪造保护（csrf）
                Crumb Issuer
                启用代理兼容
            隐藏的安全警告
            API Token
                为每个新创建的用户生成一个遗留的 API token （不建议）
                允许用户手动创建一个遗留的 API token （不建议）
                启用 API Token 使用统计（推荐）
            ssh server
                SSHD Port
                    指定端口
                    随机选取
                    禁用
        
        
        '''