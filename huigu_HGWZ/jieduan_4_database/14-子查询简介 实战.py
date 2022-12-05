# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/28 13:52
''
#todo  from型子查询  将表名换成了新的select的语句 加别名
# select * from (select * from table where xx)B where xx;

#todo in关键词 将查询条件中的列细化查询
# select * from table where id not in (select id from table where xx);

#todo where型子查询  select * from table where a > (where avg(a) from table);

'''子查询简介
    目录
        子查询简介
        带From关键字的子查询
        带IN关键词的子查询
        带比较运算符的子查询
        with…as
    
    简介
        定义：子查询指一个查询语句嵌套在另一个查询语句内部，在SELECT子句中先计算子查询，
        子查询的结果作为外层另一个查询的过滤条件，查询可以基于一个表或者多个表。 这个特性从MySQL 4.1开始引入。
        
        子查询作为过滤条件时需要用（） 包裹

    子查询的常见分类
        From型子查询：将子查询的结果作为父查询的表来使用
        in/not in 型子查询：子查询的结果是单列多行，作为where的过滤条件
        where型子查询：查询结果作为过滤条件出现在比较运算符的一端
    
    带From关键词的子查询 
        子查询是一张多行多列的表，将子查询作为父查询的表来嵌套查询
        子查询语句必须用（）包裹且需要有别名
        计算出各部门性别为男性的员工人数
        
        select dept_name,count(emp_id) from 
        (select dept_name, emp_id,ename,gender from 
        dept inner join emp_part
         where id=dept_id and gender='男')b group by dept_name;
        
    带IN关键词的子查询
        将子查询作为where语句后的过滤条件，常用于子查询结果是单列多行的情况
        子查询语句必须用（）包裹
        in/not in
        查询出北京地区所有的员工信息
        SELECT *
        FROM emp_part
        WHERE  dept_id IN (SELECT id FROM dept WHERE dept_location = '北京')
        
    带比较运算符的子查询
        将子查询的结果作为过滤条件，放在比较运算符的一端
        常用于子查询结果为单个结果的情况
        子查询语句必须用（）包裹
        
        #查询出薪资大于公司平均薪资的员工id,姓名及薪资
        SELECT emp_id,ename,salary FROM emp_part 
        WHERE salary > (SELECT AVG(salary) FROM emp_part);
        
    with as
        如果一整句查询语句中，某个子查询的结果会被多个父查询引用，通常建议将共用的子查询用简写表示出来
        
        语法： with [表名] as （select…)
        
        # 查询出部门平均薪资大于公司平均薪资的部门名称，部门主管，所在地及部门平均薪资
        
        # 不使用 with ...as
        select dept_id,dept_name,dept_manager,dept_location,avg_salary from dept inner join 
        (select dept_id,avg(salary) avg_salary from emp_part group by dept_id)b on id=dept_id 
        and avg_salary > (select avg(avg_salary) from 
        (select dept_id,avg(salary) avg_salary from emp_part group by dept_id)b);
        
        # 使用 with ...as
        with dept_avg as
        (select dept_id,avg(salary) avg_salary from emp_part group by dept_id)select
        dept_id,dept_name,dept_manager,dept_location,avg_salary from dept inner join dept_avg 
        on id=dept_id 
        and avg_salary > (select avg(avg_salary) from dept_avg);
    
    '''
'''子查询实战
    
    目录
        某软件销售公司2022年1月销售数据分析
        项目介绍
        需求实现
    
    
    项目介绍
        A公司是一家软件产品销售公司，在北京，上海，深圳，成都，杭州都设有销售部门，其中销售部门分布如下：
        北京有3个销售部门，分别为bj001，bj002，bj003
        上海有三个销售部门为：sh001，sh002,sh003
        深圳有两个销售部门为：sz001，sz002
        成都有一个销售部门为：cd001
        杭州有一个销售部门为：hz001
        department表中记录了部门相关的信息
        sales_list表中记录了最近2周各部门的销售订单相关数据
    
    项目需求
        需求1：在mysql中创建数据库hogwarts_db1 并导入相关数据
        需求2：计算出各部门最近两周的的总销售业绩，并按业绩由高到低显示
        需求3：查询出最近两周的销售额超过全公司平均销售额的部门
    
    创建数据库并导入相关数据
        部门表字段
        dept_id 部门id
        city 所在城市
        manager 部门经理
        订单表
        dept_id 部门id
        order_id 订单号
        volume 客单价
        sales_date 销售日期
        
    
    计算销售业绩并排序
        # 计算出各部门最近两周的总业绩，并按业绩由高到低排名
        SELECT
            order_list.dept_id,
            city,
            manager,
            SUM( volume ) total_volume
        FROM
            order_list
            INNER JOIN department ON order_list.dept_id = department.dept_id 
        GROUP BY
            order_list.dept_id 
        ORDER BY
            SUM( volume ) DESC
        
    
    查询出最近两周销售额超平均销售额的部门
        WITH temp_dept AS (
            SELECT
                order_list.dept_id,
                city,
                manager,
                SUM( volume ) total_volume 
            FROM
                order_list
                INNER JOIN department ON order_list.dept_id = department.dept_id 
            GROUP BY
                order_list.dept_id 
            ORDER BY
                SUM( volume ) DESC 
            ) SELECT
            * 
        FROM
            temp_dept 
        WHERE
            total_volume >(
            SELECT
                AVG( total_volume ) 
        FROM
            temp_dept)
        
    知识扩展-视图
        定义：视图是一种虚拟的表，它并不会在你的存储空间复制一份数据，而是对原有数
        据的一种引用。可以将视图理解为一种存储起来的sql语句
        视图可以简化多表查询
        视图也可以用于控制用户权限
        使用关键词view来创建视图
        语法：CREATE VIEW [视图名称] AS SELECT…..
    
    使用视图简化练习
        CREATE VIEW temp_dept AS (
            SELECT
                order_list.dept_id,
                city,
                manager,
                SUM( volume ) total_volume 
            FROM
                order_list
                INNER JOIN department ON order_list.dept_id = department.dept_id 
            GROUP BY
                order_list.dept_id 
            ORDER BY
                SUM( volume ) DESC 
            );
            
        SELECT
            * 
        FROM
            temp_dept 
        WHERE
            total_volume >(
            SELECT
                AVG( total_volume ) 
        FROM
            temp_dept);
        
        #查询出最近两周的冠军销售部门
        
        SELECT * FROM temp_dept WHERE total_volume=(SELECT max(total_volume) FROM temp_dept);
    
    
    '''
#todo 新建视图  create view 视图名 as (select * from table whrer xx);