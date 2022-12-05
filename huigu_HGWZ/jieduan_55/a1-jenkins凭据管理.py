# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/10/26 23:21
''
'''jenkins凭据管理
    凭据管理的作用：管理ssh、邮箱、git等认证信息
    
    凭据管理入口
        Dashboard -> 系统管理（Manage Jenkins） ->（安全） Manage Credentials
        
    凭据的新增
    Dashboard -> 系统管理（Manage Jenkins） -> Manage Credentials -> Stores scoped to Jenkins ->添加凭据
各种配置页面上的 Credentials 添加
    
    用户名和密码方式的凭据配置
        类型选择Username with password - 用户名 - 密码
    SSH密钥方式的凭据配置
        类型选择SSH Username with private key - Username - Private Key -> Enter directly
        
    凭据的更新和删除
    Dashboard -> 系统管理（Manage Jenkins） -> Manage Credentials -> Stores scoped to Jenkins 点击工具符号
    Dashboard -> 系统管理（Manage Jenkins） -> Manage Credentials 点击凭据    
    
    '''