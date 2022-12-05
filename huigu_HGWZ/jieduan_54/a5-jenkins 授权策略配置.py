# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/10/25 14:15
''
'''目录
    授权策略插件
    管理角色
    分配角色
    
    授权策略配置
        不同用户对系统功能的需求不同
        处于安全等考虑，关键的、重要的系统功能需要限制部分用户的使用
        处于方面性考虑，系统功能需要根据不同的用户而制定
    
    安装插件
        插件：role-based authorization strategy
        
        dashboard->configure global security->授权策略->role-based
        主目录--->jenkins系统配置-->全局配置（security）->授权策略对应选择->保存
        
        对应系统配置下，有 Manage and Assign Roles模块，可配置角色；
    
    授权策略
        选择  role-based strategy
    
    
    管理角色
        项目角色 item roles
        节点角色 node roles
        
    分配角色
        全局角色 global roles
        项目角色 item roles
        节点角色 node roles
    
    '''