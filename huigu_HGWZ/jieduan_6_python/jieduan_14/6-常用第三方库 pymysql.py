# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/14 7:18
''
'''常用第三方库 pymysql
    pymysql 概述
        Python 的数据库接口标准是 Python DB-API
        PyMySQL 是从 Python 连接到 MySQL 数据库服务器的接口
        PyMySQL 的目标是成为 MySQLdb 的替代品
        官方文档：http://pymysql.readthedocs.io/
    
    pymysql 安装
        使用 pip 安装
        使用 Pycharm 界面安装
        pip install pymysql
    
    pymysql 连接数据库 
        host：MySQL 服务器地址
        user：用户名
        password：密码
        database：数据库名称
        charset：编码方式，推荐使用 utf8mb4
        # 1.导入库
        import pymysql
        
        # 2.建立连接
        conn = pymysql.connect(host='服务器地址',
                             user='用户名',
                             password='密码',
                             database='数据库名',
                             charset="utf8mb4")
        # 3.关闭连接
        conn.close()
    
    pymysql 连接数据库
        封装获取连接的函数
        import pymysql
        
        # 1.封装建立连接的对象
        def get_conn():
            conn = pymysql.connect(
                host="服务器地址",
                user="root",
                password="123456",
                database="数据库名",
                charset="utf8mb4"
            )
        
            return conn
        
    pymysql 入门实例
        获取连接对象
        打开
        关闭
        获取游标对象
        执行 SQL
        查询记录
        from . import get_conn
        
        def test_demo():
            # 1.获取连接对象
            conn = get_conn()
            # 2.获取游标对象
            cursor = conn.cursor()
            # 3.执行SQL
            cursor.execute("SELECT VERSION()")
            # 4.查询结果
            version = cursor.fetchone()
            print(f"数据库的版本是：{version}")
            # 5.关闭连接
            conn.close()
        
    pymysql 数据库操作
        CRUD 操作
        创建表
        插入记录
        查询记录
        更新记录
        删除记录
        执行事务
        提交：commit
        回滚：rollback
    
    pymysql 创建表
        创建表 testcase
        from . import get_conn
        
        def test_create():
            conn = get_conn()  # 获取连接
            cursor = conn.cursor()  # 获取游标
        
            sql = """
            CREATE TABLE `testcase` (
            `id` int(11) NOT NULL AUTO_INCREMENT,
            `title` varchar(255) COLLATE utf8_bin NOT NULL,
            `expect` varchar(255) COLLATE utf8_bin NOT NULL,
            `owner` varchar(255) COLLATE utf8_bin NOT NULL,
            PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
            """
            cursor.execute(sql)  # 执行SQL
            conn.close()  # 关闭连接
        
    pymysql 插入操作
        插入记录
        from . import get_conn
        
            def test_insert():
            
                conn = get_conn()  # 获取连接
                cursor = conn.cursor()  # 获取游标
            
                sql = """INSERT INTO testcase
                (id, title, expect, owner)
                values (1, 'S11总决赛', '冠军', 'EDG');
                """
            
                cursor.execute(sql)  # 执行SQL
                conn.commit()  # 提交
    
    执行事务
        提交操作：commit()
        回滚操作：rollback()
        try-catch-finally
        from . import get_conn
        
            def test_insert():
                conn = get_conn()  # 获取连接
                cursor = conn.cursor()  # 获取游标
            
                sql = """INSERT INTO testcase
                (id, title, expect, owner)
                values (2, 'S11全球总决赛', '冠军', 'EDG');
                """
                try:
                    cursor.execute(sql)  # 执行SQL
                    conn.commit()  # 提交事务
                except:
                    conn.rollback()  # 回滚事务
                finally:
                    conn.close()  # 关闭连接
    
        pymysql 查询操作
            查询操作
            fetchone()：获取单条记录
            fetchmany(n)：获取 n 条记录
            fetchall()：获取所有结果记录
            import sys
            from . import get_conn
            
                def test_retrieve():
                    conn = get_conn()  # 获取连接
                    cursor = conn.cursor()  # 获取游标
                    sql = "SELECT * FROM testcase;"
                    # 捕获异常
                    try:
                        cursor.execute(sql)  # 执行SQL
                        record = cursor.fetchone()  # 查询记录
                        print(record)
                    except Exception as e:
                        print(sys.exc_info())  # 打印错误信息
                    finally:
                        conn.close()  # 关闭连接
        
    pymysql 更新操作
        更新数据表的数据
        from . import get_conn
        
            def test_update():
                conn = get_conn()
                cursor = conn.cursor()
                sql = "UPDATE testcase SET owner='hogwarts' WHERE id=2;"
                try:
                    cursor.execute(sql)  # 执行SQL
                    conn.commit()  # 提交事务
                except:
                    conn.rollback()  # 回滚事务
                finally:
                    conn.close()  # 关闭连接
    
    pymysql 删除操作
        删除数据表的数据
        from . import get_conn
        
        def test_delete():
            conn = get_conn()  # 获取连接
            cursor = conn.cursor()  # 获取游标
            sql = "DELETE FROM testcase WHERE id=3;"
            try:
                cursor.execute(sql)  # 执行SQL
                conn.commit()  # 提交事务
            except:
                conn.rollback()  # 回滚事务
            finally:
                conn.close()  # 关闭连接
    
    
            '''
