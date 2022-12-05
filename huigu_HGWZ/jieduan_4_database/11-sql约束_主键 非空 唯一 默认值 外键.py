# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/28 13:50
''
'''SQL 约束 - 主键约束
    目录
        SQL 约束
        主键约束
        添加主键约束
        创建主键自增的表
        修改主键自增的起始值
        删除主键约束
        选择主键原则
    
    SQL 约束
        对表中的数据进行进一步的限制
        保证数据的正确性、有效性、完整性
        违反约束的不正确数据无法插入到表中
        常见的约束
        主键：PRIMARY KEY
        非空：NOT NULL
        唯一：UNIQUE
        默认：DEFAULT
        外键：FOREIGN KEY
    
    主键约束
        主键：一列（或一组列），其值能够唯一标识表中每一行
        特点：不可重复，唯一，非空
        语法：列名 字段类型 PRIMARY KEY
    
    添加主键约束
        -- 创建一个带主键的表
        CREATE TABLE emp1(
            -- 设置主键 唯一 非空 
            eid INT PRIMARY KEY, 
            ename VARCHAR(20), 
            sex CHAR(1)
        );
        
        -- 给存在的表添加主键
        CREATE TABLE emp2( 
            eid INT , 
            ename VARCHAR(20), 
            sex CHAR(1) 
        )
        
        -- 通过 DDL 语句进行设置 
        ALTER TABLE emp2 ADD PRIMARY KEY(eid);
    
    创建主键自增的表
        AUTO_INCREMENT：表示自动增长(字段类型必须是整数类型)
        -- 创建主键自增的表 
        CREATE TABLE emp3(
            eid INT PRIMARY KEY AUTO_INCREMENT, 
            ename VARCHAR(20), 
            sex CHAR(1) 
        );
    
    修改主键自增的起始值
        -- 创建主键自增的表,自定义自增其实值 
        CREATE TABLE emp4( 
            eid INT PRIMARY KEY AUTO_INCREMENT, 
            ename VARCHAR(20), 
            sex CHAR(1) 
        )AUTO_INCREMENT=100;
    
    删除主键约束
        -- 删除表中的主键
        ALTER TABLE 表名 DROP PRIMARY KEY;
        
        -- 使用 DDL 语句删除表中的主键 
        ALTER TABLE emp2 DROP PRIMARY KEY; 
        -- 查看表结构
        DESC emp2;
    
    选择主键原则
        针对业务设计主键，往建议每张表都设计一个主键
        主键可以没有业务意义，只需要保证不重复
'''

'''SQL 约束-非空约束
    目录
        非空约束
        添加非空约束
    
    非空约束
        非空约束特点: 某一列不予许为空
        语法：列名 字段类型 NOT NULL
    
    添加非空约束
        -- 添加非空约束
        CREATE TABLE emp5( 
            eid INT PRIMARY KEY AUTO_INCREMENT, 
            -- ename 字段不能为空 
            ename VARCHAR(20) NOT NULL, 
            sex CHAR(1) 
        );
    
    '''
'''SQL 约束 - 唯一约束
    目录
        唯一约束
        添加唯一约束
        主键约束与唯一约束的区别
    
    唯一约束
        唯一约束: 表中的某一列的值不能重复
        对 NULL 不做唯一的判断
        语法：列名 字段类型 UNIQUE
    
    添加唯一约束
        -- 创建带有唯一约束的表  
        CREATE TABLE emp6(
            eid INT PRIMARY KEY AUTO_INCREMENT,
            -- 为 ename 字段添加唯一约束
            ename VARCHAR(20) UNIQUE,
            sex CHAR(1) 
        );
    
    主键约束与唯一约束的区别
        主键约束，唯一且不能够为空
        唯一约束，唯一但是可以为空
        一个表中只能有一个主键，但是可以有多个唯一约束
    
    '''

'''SQL 约束 - 默认值
    目录
        默认值
        字段指定默认值
    
    默认值
        默认值约束：用来指定某列的默认值
        语法：列名 字段类型 DEFAULT 默认值
    
    字段指定默认值
        -- 创建带有默认值的表 
        CREATE TABLE emp7( 
            eid INT PRIMARY KEY AUTO_INCREMENT,
            ename VARCHAR(20), 
            -- 为 sex 字段添加默认值 
            sex CHAR(1) DEFAULT '女'
        );
        
    insert into table(列1,列2) values('x',default);
    insert into table(列1) values('x');
    insert into table(列1,列2) values('x','xx');
    '''
'''SQL约束-外键约束
    目录
        外键约束的定义与意义
        建立外键约束
        删除外键约束
    外键约束
        主键：可以唯一标识一条记录的列
        
        外键：从表中与主表的主键对应的字段
        主表：外键所指向的表,约束其他表的表
        
        从表：外键所在的表，被约束的表
        
        价值：建立主表与从表的关联关系，为两个表的数据建立连接，约束两个表中数据的一致性和完整性
    
    主键id   外键dept_id
    
    建立外键约束
        创建表时添加外键约束：CONSTRAINT [外键约束的名称] FOREIGN KEY (外键字段) REFERENCES [主表名称(主键字段)]
        
        添加外键约束：ALTER TABLE [表名] ADD CONSTRAINT [外键约束的名称] FOREIGN KEY [外键字段] REFERENCES [主表名称(主键字段)]
        
        
        # 创建一个关联到主表的从表
        CREATE TABLE emp_part(  
        emp_id INT PRIMARY KEY AUTO_INCREMENT,  
        ename VARCHAR(20),  
        age INT ,  
        gender VARCHAR(10),
        dept_id INT,
        -- 添加外键约束 
        CONSTRAINT emp_dept FOREIGN KEY(dept_id) REFERENCES dept(id)
        );
        # 插入一条非法数据
        INSERT INTO emp_part VALUES(1,'cindy',20,'female','4')
    
    删除外键约束
        语法：
        ALTER TABLE [表名] DROP FOREIGN KEY [外键约束名称]
        注意事项
        从表外键数据类型必须与主表的主键一致
        删除数据时，需先删除从表数据再删除主表的数据
        添加数据时先添加主表数据，再添加从表数据
        # 删除外键约束 
        
        ALTER TABLE emp_part DROP FOREIGN KEY emp_dept 
        
        # 插入一条非法数据
        INSERT INTO emp_part VALUES(1,'cindy',20,'female','4') 
        
        SELECT * FROM emp_part  
        
        # 向主表中插入一条数据
        INSERT INTO dept VALUES(2,'运营部','张三','北京') 
        # 向从表中插入一条数据
        INSERT INTO emp_part VALUES(1,'cindy',20,'female','2') 
        # 删除主表中的数据 
        DELETE FROM dept WHERE id=2
    
    级联删除
        删除主表数据的同时,也删除掉从表中相关的数据
        ON DELETE CASCADE ```sql
    
    创建员工信息表并添加级联删除的外键约束
        CREATE TABLE emp_part(
        emp_id INT PRIMARY KEY AUTO_INCREMENT,
        ename VARCHAR(20),
        age INT ,
        gender VARCHAR(10), dept_id INT, – 添加外键约束 CONSTRAINT emp_dept FOREIGN KEY(dept_id) REFERENCES dept(id) – 设置
        允许级联删除 ON DELETE CASCADE ); 
        # 向员工信息表中添加一条数据 INSERT INTO emp_part VALUES(1,‘cindy’,20,‘female’,‘2’) #删除
        主表中部门id=2的部门 DELETE FROM dept WHERE id=2 # 查看从表中的数据是否同时被删除 SELECT * FROM emp_part ```
    '''