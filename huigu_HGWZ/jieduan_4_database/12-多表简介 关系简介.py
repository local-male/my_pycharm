# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/28 13:52
''
'''多表简介
    目录
        多表及使用场景介绍
        多表设计案例
        使用多表的优点
    
    多表及应用场景介绍
        多表顾名思义就是在数据库设计中使用多张表格来实现数据存储的要求
        在实际的项目开发中，数据量大而且复杂，需要分库分表
        分表：按照一定的规则，对原有的数据库和表进行拆分
        表与表之间可以通过外键建立连接
    
    多表设计案例
        假定我们现在需要创建一张员工信息表，包含字段：
        eid 员工ID (自增主键)
        ename 员工姓名
        age 年龄
        gender 性别
        dept_name 所在部门
        dept_id 部门ID
        dept_manager 部门主管
        dept_location 所在地点
    
    以单表的形式完成建表
        创建员工信息表
        CREATE TABLE emp(  
        emp_id INT PRIMARY KEY AUTO_INCREMENT,  
        ename VARCHAR(20),  
        age INT ,  
        gender VARCHAR(10),  
        dept_name VARCHAR(20),  
        dept_id INT,  
        dept_manager VARCHAR(20),  
        dept_location VARCHAR(20)  
        );  
    
    插入数据
        INSERT INTO emp VALUES (1,'张三', 20, '男','研发部',1,'张无忌','北京');
        INSERT INTO emp(ename, age,gender,dept_name,dept_id,dept_manager, dept_location)
        VALUES ('李四', 25, '男','研发部',1,'张无忌','北京');
        INSERT INTO emp(ename, age,gender,dept_name,dept_id,dept_manager, dept_location) 
        VALUES ('宋江', 40, '男','研发部',1,'张无忌','北京');
        INSERT INTO emp(ename, age,gender,dept_name,dept_id,dept_manager, dept_location) 
        VALUES ('林冲', 25, '男','研发部',1,'张无忌','北京');
        INSERT INTO emp(ename, age,gender,dept_name,dept_id,dept_manager, dept_location) 
        VALUES ('林徽因', 25, '女','研发部',1,'张无忌','北京');
        INSERT INTO emp(ename, age,gender,dept_name,dept_id,dept_manager, dept_location) 
        VALUES ('周芷若', 25, '女','运营部',2,'赵敏','深圳');
        INSERT INTO emp(ename, age,gender,dept_name,dept_id,dept_manager, dept_location) 
        VALUES ('任盈盈', 25, '女','运营部',2,'赵敏','深圳');
    
    单表数据冗余
        emp_id   ename  age  gender  dept_name  dept_id  dept_manager  dept_location
        1       张三      20    男       研发部      1          张无忌         北京
        2       李四      25    男       研发部      1          张无忌         北京
        3       宋江      40    男       研发部      1          张无忌         北京
        4       林冲      20    男       研发部      1          张无忌         北京
        5       林徽因     25    女       研发部      1          张无忌         北京
        6       任盈盈     25    女       运营部      2          赵敏           深圳
        7       周芷若     25    女       运营部      2          赵敏           深圳

    多表设计模式
        将数据拆分为员工信息表employee和部门信息表dept
        两个表之间通过部门id：dept_id字段连接
        # 创建员工信息表
        CREATE TABLE emp_part(  
        emp_id INT PRIMARY KEY AUTO_INCREMENT,  
        ename VARCHAR(20),  
        age INT ,  
        gender VARCHAR(10),
        dept_id INT
        );
        
        # 创建部门表
        CREATE TABLE dept(  
        id INT PRIMARY KEY AUTO_INCREMENT,  
        dept_name VARCHAR(20),  
        dept_manager VARCHAR(20),  
        dept_location VARCHAR(20)  
        ); 
    
    插入数据
        # 向部门表插入数据
        INSERT INTO dept(dept_name,dept_manager,dept_location) VALUES('研发部','张无忌','北京');
        INSERT INTO dept(dept_name,dept_manager,dept_location) VALUES('运营部','赵敏','深圳');
        
        # 向员工信息表插入数据
        INSERT INTO emp_part(ename,age,gender,dept_id) VALUES ('李四', 25, '男',1);
        INSERT INTO emp_part(ename,age,gender,dept_id) VALUES ('宋江', 40, '男',1);
        INSERT INTO emp_part(ename,age,gender,dept_id) VALUES ('张三', 20, '男',1);
        INSERT INTO emp_part(ename,age,gender,dept_id) VALUES ('林冲', 25, '男',1);
        INSERT INTO emp_part(ename,age,gender,dept_id) VALUES ('林徽因', 25,'女',1);
        INSERT INTO emp_part(ename,age,gender,dept_id) VALUES ('周芷若', 25,'女',2);
        INSERT INTO emp_part(ename,age,gender,dept_id) VALUES ('任盈盈', 25, '女',2);
    
    多表关系
        emp_id  ename  age  gerder  dept_id   
        1       李四     25   男       1                 
        2       宋江     40   男       1
        3       张三     20   男       1
        4       林冲     25   男       1
        5       林徽因    25  女       1
        6       任盈盈    25  女       2
    
        id  dept_name  dept_manager  dept_location
        1      研发部      张无忌         北京
        2      运营部     赵敏           深圳
        
        dept_id（外键）  id（主键）   一一对应
    
    多表的优点
        简化数据
        提高复用性
        方便权限控制
        提高系统的稳定性和负载能力
        '''
'''多表关系简介
    目录
        一对多
        多对多
        一对一
        
    一对多
        定义： 主表的一条记录可以对应从表的多条记录
        例子： 部门表，员工表
        建表原则：在一对多关系中，多的表定位从表，设置外键指向主表
    
    多对多
        定义：主表的多条记录可以对应从表的多条记录
        例子：商品信息表，客户表，订单表
        建表原则：需要创建第三张表作为中间表，中间表需要包含两张表的主键。
    
    一对一
        定义：从表的一条记录对应主表的一条记录
        例子：员工信息表与身份证表,联系方式
        建表原则： 这种对应关系的数据，通常放在单表里
    
    '''
