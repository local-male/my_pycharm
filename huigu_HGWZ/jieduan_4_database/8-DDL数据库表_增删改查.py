# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/27 14:27
''
#todo create  table 表名 （列名 属性）

'''DDL 数据库表操作-创建
    目录
        创建表语法
        列属性
        创建学员表
        复制结构相同的表
    
    创建表语法
        -- 创建表
        CREATE TABLE 数据表名 (
          列名1 属性,
          列名2 属性…
        );
    
    列属性
        NOT NULL | NULL：该列是否允许是空值
        DEFAULT：表示默认值
        AUTO_INCREMENT：表示是否是自动编号
        PRIMARY KEY：表示是否为主键
        
        列名 数据类型 [NOT NULL | NULL] [DEFAULT 默认值] [AUTO_INCREMENT]
        [PRIMARY KEY ] [注释]
    
    创建学员表
        创建在 db1 数据库中
        表名为 student
        包含两个字段
        学员 id
        学员姓名
        -- 切换到数据库 db1 
        USE db1;
        
        -- 创建学员表 
        CREATE TABLE student( 
          id INT,
          name VARCHAR(20) 
        );
    
    复制表语法
        数据表名：表示新创建的数据表的名
        LIKE 源数据表名：必选项，指定依照哪个数据表来创建新表
        -- 复制表
        CREATE TABLE数据表名
        {LIKE 源数据表名 | (LIKE 源数据表名)}
    
    复制结构相同的表
        -- 创建一个表结构与 student 相同的 s2 表 
        CREATE TABLE s2 LIKE student;
    
    
    '''
#todo desc 数据库表名  列名；
'''DDL 数据库表操作 - 查看
    目录
        查看表名语法
        查看表结构语法
        实例
    
    查看表名语法
        -- 查看当前数据库中所有的表名
        SHOW TABLES;
    
    查看表结构语法
        -- 查看表结构
        DESCRIBE 数据表名;
        DESCRIBE 数据表名 列名;
        
        -- 查看表结构简写
        DESC 数据表名;
        DESC 数据表名 列名;
    
    实例
        -- 选择数据库
        USE db1;
        -- 查看数据库中的表
        SHOW TABLES;
        -- 查看学员表的表结构
        DESC student;
        -- 查看学员表中 name 列的信息
        DESC student name;
    '''
#todo  alter table 表名  add/modify/charge/drop 列名  属性；
'''DDL 数据库表操作 - 修改
    目录
        添加新列
        修改列定义
        修改列名
        删除列
        修改表名
    
    添加新列
        -- 添加新列
        ALTER TABLE 表名 ADD 列名 列属性;
        
        # 实例
        -- 选择数据库 db1
        USE db1;
        -- 添加新列
        ALTER TABLE student ADD email varchar(50) NOT NULL;
        -- 查看表结构
        DESC student;
    
    修改列定义
        -- 修改列定义
        ALTER TABLE 表名 MODIFY 列名 列属性;
        
        # 实例
        -- 添加分数列，先定义为字符类型
        ALTER TABLE student ADD score varchar(10);
        -- 修改字段类型
        ALTER TABLE student modify score int;
        -- 查看表结构
        DESC student; 
    
    修改列名
        -- 修改列名
        ALTER TABLE 表名 CHANGE 旧列名 新列名 类型;
        
        # 实例
        -- 修改列名并指定列的默认值
        ALTER TABLE student
        CHANGE COLUMN name stu_name VARCHAR(30) DEFAULT NULL;
        -- 查看表结构
        DESC student;
    
    删除列
        -- 删除列
        ALTER TABLE 表名 DROP 列名;
        
        # 实例
        -- 将数据表 student 中的列 score 删除
        ALTER TABLE student DROP score;
        -- 查看表结构
        DESC student;
    
    修改表名
        -- 修改表名方式一
        ALTER TABLE 旧表名 RENAME AS 新表名;
        
        -- 修改表名方式二
        RENAME TABLE 旧表名 To 新表名;
        
        # 实例
        -- 将数据表 student 更名为 stu
        ALTER TABLE student RENAME AS stu;
        -- 将数据表 stu 更名为 stu_table
        RENAME TABLE stu TO stu_table;
        -- 查看表名
        SHOW TABLES;
    '''
#todo drop table 表名；
'''DDL 数据库表操作 - 删除
    目录
        删除表语法
        实例
    
    删除表语法
        IF EXISTS：可选项，先判断是否存在要删除的表，存在时才执行删除操作
        数据表名：用于指定要删除的数据表名
        DROP TABLE [IF EXISTS] 数据表名;
    
    实例
        -- 切换到数据库 db1 
        USE db1;
        
        -- 创建 student 表
        CREATE TABLE student( 
          id INT,
          name VARCHAR(20) 
        );
        
        -- 直接删除 student 表 
        DROP TABLE student;
        
        -- 先判断再删除 student 表 
        DROP TABLE IF EXISTS student;
    '''
