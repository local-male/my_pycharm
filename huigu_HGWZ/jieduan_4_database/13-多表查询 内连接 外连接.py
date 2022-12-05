# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/28 13:52
''

'''多表查询之笛卡尔积
    目录
        多表查询与数据准备
        笛卡尔积简介
        
    多表查询的定义
        定义：通过查询
    '''

'''多表查询-内连接查询
    目录
        内连接的定义
        隐式内连接
        显式内链接

    内连接
        内连接（INNER JOIN）：使用比较运算符进行表间某（些）列数据的比较操作，
        并列出这些表中与连接条件相匹配的数据行，组合成新的记录。匹配上显示，匹配不上不显示。
        例子： 比如使用外键=主键这个条件过滤掉无效数据
        按语法结构分为： 隐式内连接和显式内连接

    隐式内连接
        在笛卡尔积的的基础上，使用where条件过滤无用的数据，这种连接方式是隐式内连接.

        语法：select [字段名称] from 表1，表2 where [条件]

        例1： 筛选出运营部的员工的id，姓名以及所在城市


        SELECT emp_id,ename,dept_location 
        FROM emp_part,dept 
        WHERE dept_id=id and dept_name="运营部";

    显式内连接
        显式内连接： 使用 select [字段名称] from [表1]inner join [表2] on [条件] 这种方式
        列子： 用显式内连接查询运营部的员工的id，姓名以及所在城市
        SELECT emp_id,dept_location,ename 
        FROM emp_part 
        INNER JOIN dept ON dept_id=id AND dept_name="运营部"

    
    select * from A,B where A.a = B.a and  查询条件；
    select * from A inner join B on 查询条件；
    '''
'''多表查询-外连接查询
    目录
        外连接介绍
        左连接
        内连接

    外连接
        外连接查询：查询多个表中相关联的行，有时候需要包含没有关联的行中数据，
        即返回查询结果集合中不仅包含符合连接条件的行，还包括左表（左连接）、右表（右连接）中的所有数据行。

        左外连接 , 使用 LEFT OUTER JOIN , OUTER 可以省略

        右外连接 , 使用 RIGHT OUTER JOIN , OUTER 可以省略

    示例

    左连接
        左连接：以左表为基准匹配右表的数据，右表中没有的项，显示为空

        语法：SELECT [字段] FROM [左表] LEFT JOIN [右表] ON [条件]

        例子：公司新成立人力资源部，还未招聘员工，请使用左连接查询方式查询出公司所有部门员工的员工号，
        姓名，性别以及他们所在的部门名称和城市

        #向部门表中插入人力资源部
        INSERT INTO dept VALUES(4,'人力资源部','甄嬛','北京');
        #查询出需要的数据
        SELECT emp_id,ename,gender,dept_name,dept_location 
        FROM dept LEFT JOIN emp_part ON dept.id=emp_part.dept_id

    右连接
        右连接：以右表为基准匹配左表的数据，左表中没有的项，显示为空

        语法：SELECT [字段] FROM [左表] RIGHT JOIN [右表] ON [条件]

        使用右连接的方式查询出所有员工信息以及他们所在的部门名称和城市

    总结
        内连接: inner join
        左连接: left join
        右连接: right join
        内连接和左连接使用居多
    '''