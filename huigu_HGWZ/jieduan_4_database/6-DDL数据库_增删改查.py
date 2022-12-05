# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/26 16:20
''
'''DDL 数据库操作-创建
    目录
        创建数据库语法
        创建数据库注意事项
        创建基本数据库
        创建指定字符集的数据库
        创建数据库前判断是否存在同名数据库
        
    创建数据库语法
        IF NOT EXISTS：可选项，创建前先判断，未存在时才执行创建语句
        数据库名：必须指定的
        CHARACTER SET =字符集：可选项，用于指定数据库的字符集
        -- 创建数据库
        CREATE {DATABASE|SCHEMA} [IF NOT EXISTS] 数据库名
        CHARACTER SET [=]  字符集
    
    创建数据库注意事项
        不能与其他数据库重名
        名称可以由任意字母、阿拉伯数字、下划线（_）和“$”组成，但不能使用单独的数字
        名称最长可为 64 个字符，别名最长为 256 个字符。
        不能使用 MySQL 关键字作为数据库名
        建议采用小写来定义数据库名
    
    创建基本数据库
        -- 创建名为 test_db 的数据库
        CREATE DATABASE test_db;
        
    创建指定字符集的数据库
        -- 创建名为 test_db2 的数据库，并指定字符集为 utf8
        CREATE DATABASE test_db2 CHARACTER SET utf8; 
    
    创建数据库前判断是否存在同名数据库
        -- 如果数据库 test_db3 不存在，则创建名为 test_db3 的数据库
        CREATE DATABASE IF NOT EXISTS test_db3 CHARACTER SET utf8;
    '''

'''DDL数据库操作-查看
    目录
        选择数据库语法
        查看数据库语法
        查看数据库的定义信息语法
        实例
    
    查看数据库语法
        DATABASES：必选项，用于列出当前用户权限范围内所能查看到的所有数据库名称
        -- 查看所有数据库
        SHOW DATABASES;
        
    选择数据库语法
        -- 选择数据库为当前数据库
        USE 数据库名;
    
    查看数据库的定义信息语法
        -- 查看数据库定义信息
        SHOW CREATE DATABASE 数据库名;
        
    实例
        -- 查看当前所有数据库
        SHOW DATABASES;
        -- 选择数据库 test_db
        USE test_db;
        -- 查看 test_db 数据库的定义信息
        SHOW CREATE DATABASE 数据库名;
    
    '''
'''DDL 数据库操作 - 修改
    目录
        修改数据库语法
        修改数据库字符集
    
    修改数据库语法
        DATABASE：必选项
        数据库名：可选项，如果不指定要修改的数据库，那么将表示修改当前（默认）的数据库
        CHARACTER SET = 字符集：可选项，用于指定数据库的字符集
        
        -- 修改数据库相关参数
        ALTER {DATABASE} [数据库名]
        CHARACTER SET [=] 字符集 
    
    修改数据库字符集
        -- 创建数据库 db1，指定字符集为 GBK
        CREATE DATABASE db1 CHARACTER SET GBK;
        -- 将数据库 db1 的字符集修改为 utf8 
        ALTER DATABASE db1 CHARACTER SET utf8;
    
    '''

'''DDL 数据库操作 - 删除
    目录
        删除数据库语法
        删除某个数据库
    
    删除数据库语法
        DATABASES：必选项
        IF EXISTS：用于指定在删除数据前，先判断该数据库是否已经存在，可以避免删除不存在的数据库时产生异常
    -- 删除数据库
    DROP DATABASE [IF EXISTS] 数据库名;

    删除某个数据库
        -- 查看当前所有数据库
        SHOW DATABASES;
        -- 删除某个数据库 
        DROP DATABASE test_db;
        -- 如果某个数据库存在，则删除这个数据库
        DROP DATABASE IF EXISTS test_db2; 
    
    '''
