# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/27 23:50
''
#todo INSERT INTO user (id,name,address) VALUES(4,'赵六','天津'),(5,'小红','成都'),(6,'小白','杭州');
'''DML 表数据操作-插入
    目录
        表数据插入语法
        完整插入数据
        插入数据记录的一部分
        插入多条记录
        注意事项
    
    表数据插入语法
        INTO 数据表名：指定被操作的数据表
        (列名1, 列名2…)：可选项，向数据表的指定列插入数据
        VALUES(值1, 值2…)：需要插入的数据
        
        -- 插入数据
        INSERT INTO 数据表名 
        (列名1, 列名2...)
        VALUES(值1, 值2...);
    
    完整插入数据
        向数据表中插入一条完整的数据
        
        -- 选择数据库
        USE db1;
        
        -- 创建 user 表
        CREATE TABLE user( 
          id INT,
          name VARCHAR(20),
          age INT, 
          sex CHAR(1), 
          address VARCHAR(40)
        );
        
        -- 插入一条完整数据，写出全部列名
        INSERT INTO user (id,name,age,sex,address) 
        VALUES(1,'张三',20,'男','北京');
        
        -- 插入一条完整数据，不写列名
        INSERT INTO user
        VALUES(2,'李四',22,'女','上海');
    
    插入数据记录的一部分
        只插入表的一行中的某几个字段的值
        
        -- 插入表一行中的某几列的值
        INSERT INTO user (id,name,address) 
        VALUES(3,'王五','深圳');
    
    插入多条记录
        一次性插入多条数据记录
        
        -- 一次插入多条数据
        INSERT INTO user (id,name,address)
        VALUES(4,'赵六','天津'),(5,'小红','成都'),(6,'小白','杭州');
    
    注意事项
        值与字段必须要对应，个数相同并且数据类型相同
        值的数据大小，必须在字段指定的长度范围内
        VARCHAR CHAR DATE 类型的值必须使用单引号包裹
        如果要插入空值，可以忽略不写，或者插入 NULL
        如果插入指定字段的值，必须要上写列名
    '''
#todo UPDATE student SET age = 30, city = '北京' WHERE id = 2;
'''DML 表数据操作-修改
    目录
        表数据修改语法
        实例
    
    表数据修改语法
        SET 子句：必选项，用于指定表中要修改的字段名及其字段值
        WHERE 子句：可选项，用于限定表中要修改的行
        -- 修改表中数据
        UPDATE 数据表名
        SET 列名1=值1 [, 列名2=值2...]
        [WHERE 条件表达式]
    
    实例
        -- 选择 db1 为当前数据库
        USE db1;
        
        -- 创建 student 表
        CREATE TABLE student( 
          id INT,
          name VARCHAR(20),
          sex CHAR(1),
          age TINYINT,
          city VARCHAR(50)
        );
        
        -- 插入 5 条数据
        INSERT INTO student
        VALUES(1,'小李','男', 18, '北京'),
        (2,'小白','女', 20, '成都'),
        (3,'小王','男', 23, '上海'),
        (4,'小赵','女', 21, '深圳'),
        (5,'小周','男', 25, '杭州');
        
        -- 不带条件修改，将所有的性别改为女
        UPDATE student SET sex = '女';
        
        -- 带条件的修改，将 id 为 3 的学生，性别改为男
        UPDATE student SET sex = '男' WHERE id = 3;
        
        -- 一次修改多个列， 将 id 为 2 的学员，年龄改为 30，地址改为 北京
        UPDATE student SET age = 30, city = '北京' WHERE id = 2;
    '''
#todo  TRUNCATE/DELETE TABLE student;
'''DML 表数据操作-删除
    目录
        通过 DELETE 语句删除数据
        通过 TRUNCATE TABLE 语句删除数据
        实例
    
    通过 DELETE 语句删除数据
        数据表名：指定要删除的数据表的表名
        WHERE 子句：限定表中要删除的行
        -- 删除表中指定行的数据
        DELETE FROM 数据表名
        WHERE 条件表达式
    
    通过 TRUNCATE TABLE 语句删除数据
        -- 删除表中全部数据
        TRUNCATE TABLE 数据表名
    
    实例
        -- 选择 db1 为当前数据库
        USE db1;
        
        # 数据准备
        -- 创建 student 表
        CREATE TABLE student( 
          id INT,
          name VARCHAR(20),
          sex CHAR(1),
          age TINYINT,
          city VARCHAR(50)
        );
        
        -- 插入 5 条数据
        INSERT INTO student
        VALUES(1,'小李','男', 18, '北京'),(2,'小白','女', 20, '成都'),(3,'小王','男', 23, '上海'),(4,'小赵','女', 21, '深圳'),(5,'小周','男', 25, '杭州');
        
        -- 删除 id 为 1 的数据 
        DELETE FROM student WHERE id = 1;
        
        -- 删除 student 表中所有数据
        DELETE FROM student;
        
        -- 删除 student 表中所有数据
        TRUNCATE TABLE student;   

    '''