# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/28 13:49
''
#todo windows cmd 切换路径  cd /d D:\
'''DQL 表查询操作-简介
    目录
        数据准备
        单表查询
        字段查询
        起别名
        去重
        
    数据准备
        测试数据库：
        https://github.com/datacharmer/test_db
        网盘下载：
        网盘下载地址
        提取码：gxow
        cd 数据所在目录
        mysql -h 127.0.0.1 -uroot -p < employees.sql
    
    单表查询
        单表查询：从一张表中查询所需要的数据，所有查询操作都比较简单
        语法：SELECT * FROM 表名;
        * 代表所有的列
        -- 查询部门表中的信息
        SELECT * FROM departments;
    
    字段查询
        查询多个字段（列），可以使用 , 对字段进行分隔
        语法：SELECT 列名 FROM 表名;
        -- 查询部门的名称
        SELECT dept_name FROM departments;
    
    起别名
        为表起别名：
        SELECT 列名  FROM 表名 表别名;
        为字段起别名：
        SELECT 列名 AS 别名 FROM 表名;
        -- 查询员工信息，并将列名改为中文
        SELECT 
            emp_no AS '编号',
            first_name AS '名',
            last_name AS '姓',
            gender AS '性别',
            hire_date AS '入职时间'
        FROM
            employees emp; 
        
    去重
        DISTINCT 关键字：去掉重复信息
        语法：SELECT DISTINCT 列名 FROM 表名;
        -- 去掉重复职级信息 
        SELECT DISTINCT title FROM titles;
    
    运算查询
        查询结果参与运算
        SELECT (列名 运算表达式) FROM 表名;
        -- 所有员工的工资 +1000 元进行显示
        SELECT emp_no , salary + 1000 FROM salaries;
    
'''
'''DQL 表查询-条件查询
    目录
        条件查询语法
        比较运算符
        逻辑运算符
        通配符
    
    条件查询语法
        -- 条件查询
        SELECT 列名 FROM 表名 WHERE 条件表达式
    
    比较运算符
        运算符	            说明
        > < <= >= = <> !=	大于、小于、小于等于、大于等于、等于、不等于
        BETWEEN...AND...	范围限定
        IN	                子集限定
        LIKE '%or%'	        模糊查询
        IS NULL	            为空
    
    比较大小
        语法：WHERE <列名> [> < <= >= = <> !=] <值>
        -- 查询出生日期晚于 1965-01-01 的员工编号、姓名和生日
        SELECT 
            emp_no, first_name, last_name, birth_date
        FROM
            employees
        WHERE
            birth_date > '1965-01-01';
        
    使用 BETWEEN 进行模糊查询
        语法：WHERE <列名> [NOT] BETWEEN <起始表达式> AND <结束表达式>
        <起始表达式> 和 <结束表达式> 的顺序不能颠倒
        -- 查询年薪介于 70000 到 70003 之间的员工编号和年薪
        SELECT 
            emp_no, salary
        FROM
            salaries
        WHERE
            salary BETWEEN 70000 AND 70003;
    
    使用 IN 进行模糊查询
        语法：WHERE <列名> IN <(常量列表)>
        (常量列表) 中各常量值用逗号隔开
        -- 查询入职日期为 1995-01-27 和 1995-03-20 日的员工信息
        SELECT 
            *
        FROM
            employees
        WHERE
            hire_date IN ('1995-01-27', '1995-03-20');
    
    判断是否为空
        语法：WHERE <列名> IS [NOT] NULL
        -- 选择 hog_demo 为当前数据库
        USE hog_demo;
        
        -- 更新 student 表中 id 为 2 的 age 值为 NULL
        UPDATE student SET age = NULL WHERE id = 2;
        
        -- 查询学生表中年龄为 NULL 的学生信息
        SELECT 
            *
        FROM
            student
        WHERE
            age IS NULL;
    
    逻辑运算符
        运算符	    说明
        AND &&	    多个条件同时成立
        OR ｜｜	    多个条件任一成立
        NOT	        不成立
    
    -- 查询名字为 Lillian 并且姓氏为 Haddadi 的员工信息
    SELECT 
        *
    FROM
        employees
    WHERE
        first_name = 'Lillian'
            AND last_name = 'Haddadi';
    
    -- 查询名字为 Lillian 或者姓氏为 Terkki 的员工信息
    SELECT 
        *
    FROM
        employees
    WHERE
        first_name = 'Lillian'
            OR last_name = 'Terkki';
    
    -- 查询名字为 Lillian 并且性别不是女的员工信息
    SELECT 
        *
    FROM
        employees
    WHERE
       first_name = 'Lillian'
       and not gender='F';
    
    通配符
        运算符	    说明
        %	        匹配任意多个字符
        -	        匹配一个字符
        -- 查询名字中包含 fai 的员工的信息
        SELECT 
            *
        FROM
            employees
        WHERE
            first_name LIKE '%fai%';
        
        -- 查询名字中 fa 开头的名字长度为 3 位的员工信息
        SELECT 
            *
        FROM
            employees
        WHERE
            first_name LIKE 'fa_';
'''
'''DQL 表查询操作-排序
    目录
        排序语法
        单列排序
        组合排序
    
    排序语法
        ASC 表示升序排序（默认）
        DESC 表示降序排序
        -- 对查询结果进行排序
        SELECT 列名 FROM 表名 
        [WHERE 条件表达式] 
        ORDER BY 列名1 [ASC / DESC],
        列名2 [ASC / DESC] 
    
    单列排序
        只按照某一个列进行排序, 就是单列排序
        -- 使用 salary 字段,对 salaries 表数据进行升序排序
        SELECT * FROM salaries ORDER BY salary;
        
        -- 使用 salary 字段,对 salaries 表数据进行降序排序
        SELECT * FROM salaries ORDER BY salary DESC;
        
        -- 查询员工的编号和入职日期，按照员工入职日期从晚到早排序
        SELECT 
            emp_no, hire_date
        FROM
            employees
        ORDER BY hire_date DESC;
    
    
    组合排序
        同时对多个字段进行排序
        如果第一个字段相同，就按照第二个字段进行排序
        -- 在入职时间排序的基础上，再使用 emp_no 进行排序
        -- 组合排序 
        SELECT 
            emp_no, hire_date
        FROM
            employees
        ORDER BY hire_date DESC, emp_no DESC;
'''
'''DQL 表查询操作-聚合函数
    目录
        聚合函数
        聚合查询
    
    聚合函数
        COUNT()：统计指定列不为 NULL 的记录行数
        MAX()：计算指定列的最大值
        MIN()：计算指定列的最小值
        SUM()：计算指定列的数值和
        AVG()：计算指定列的平均值
    
    聚合查询
        语法：SELECT 聚合函数(列名) FROM 表名;
        -- 查询职级名称为 Senior Engineer 的员工数量
        SELECT 
            COUNT(*)
        FROM
            titles
        WHERE
            title = 'Senior Engineer';
        
        -- 查询员工编号为 10002 的员工的最高年薪
        SELECT 
            MAX(salary)
        FROM
            salaries
        WHERE
            emp_no = 10002;
        
        -- 查询员工编号为 10002 的员工的最低年薪
        SELECT 
            MIN(salary)
        FROM
            salaries
        WHERE
            emp_no = 10002;
        
        -- 查询员工编号为 10002 的员工的薪水总和
        SELECT 
            SUM(salary)
        FROM
            salaries
        WHERE
            emp_no = 10002;
        
        -- 查询员工编号为 10002 的员工的平均年薪
        SELECT 
            AVG(salary)
        FROM
            salaries
        WHERE
            emp_no = 10002;
    
    '''
'''DQL 表查询操作 - 分组
    目录
        分组查询语法
        实例
        子句区别
    
    分组查询语法
        分组列：按哪些列进行分组
        HAVING：对分组结果再次过滤
        -- 分组查询
        SELECT 分组列/聚合函数 FROM 表名 
        GROUP BY 分组列 
        [HAVING 条件];
    
    实例
        -- 查询每个员工的薪资和
        SELECT 
            emp_no, SUM(salary)
        FROM
            salaries
        GROUP BY emp_no;
        
        -- 查询员工编号小于 10010 的，薪资和小于 400000 的员工的薪资和
        SELECT 
            emp_no, SUM(salary)
        FROM
            salaries
        WHERE
            emp_no < 10010
        GROUP BY emp_no
        HAVING SUM(salary) < 400000;
    
    子句区别
        WHERE 子句：从数据源中去掉不符合其搜索条件的数据
        GROUP BY 子句：搜集数据行到各个组中，统计函数为各个组计算统计值
        HAVING 子句：去掉不符合其组搜索条件的各行数据行
    
    '''
'''DQL 表查询操作 - LIMIT 关键字 只支持mysql
    目录
        LIMIT 关键字
        实例
        单表查询总结
        SQL 语句执行顺序
    
    LIMIT 关键字
        限制查询结果的数量
        开始的行数：从 0 开始记数, 如果省略则默认为 0
        查询记录的条数：返回的行数
        -- 限制查询结果行数
        SELECT 列名1, 列名2... 
        FROM 表名 
        LIMIT [开始的行数], <查询记录的条数>
        
        -- 使用 OFFSET 关键字指定开始的行数
        SELECT 列名1, 列名2... 
        FROM 表名 
        LIMIT <查询记录的条数> OFFSET <开始的行数>
    
    实例
        -- 展示前 10 条员工信息
        SELECT * FROM employees LIMIT 10;
        SELECT * FROM employees LIMIT 0, 10;
        SELECT * FROM employees LIMIT 10 OFFSET 0;
        
        -- 显示年薪从高到低排序，第 15 位到第 20 位员工的编号和年薪
        SELECT 
            emp_no, salary
        FROM
            salaries
        ORDER BY salary DESC
        LIMIT 14, 6;
    
    单表查询总结
        -- 基础查询语法
        SELECT DISTINCT <列名>
        FROM <表名>
        WHERE <查询条件表达式>
        GROUP BY <分组的列名>
        HAVING <分组后的查询条件表达式>
        ORDER BY <排序的列名> [ASC / DESC]
        LIMIT [开始的行数], <查询记录的条数>
    
    SQL 语句执行顺序
    from->where->group by->having->select->distinct->order by->limit
    '''