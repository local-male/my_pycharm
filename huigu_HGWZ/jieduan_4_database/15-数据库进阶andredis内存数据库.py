# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/12/1 20:14
''
'''数据库进阶
    目录
        mysql中sql执行原理
            sql执行过程
                客户端--》mysql server --》存储引擎
            server 组件
                连接器：连接管理，权限验证
                查询缓存：命中直接返回结果
                分析器：语法分析
                优化器：生成执行计划，选择索引
                执行器：操作引擎，返回结果
            
        索引
            索引定义：
                索引是存储的表中一个特定列的值数据结构
                索引包含一个表中列的值，并且这次谢志存储在一个数据结构中
            索引分类：
                单列索引
                    普通索引
                    唯一索引：允许null值
                    主键索引：不允许null值
                组合索引
                全文索引
            索引优势：
                提高数据检索的效率，降低数据库的io成本
                通过索引对数据进行排序，降低数据排序的成本，降低了cpu的消耗
            索引劣势
                占用空间
                降低更新表的速度
                需要花时间研究建立最优秀的索引，或者优化
            索引适合的场景
                主键自动建立唯一索引
                频繁作为查询条件的字段应该建立索引
                查询中与其他表关联的字段，外键关系建立索引
                查询中排序的字段
            
        explain
            执行计划
                模拟优化器执行sql查询语句
                分析查询语句或是表结构的性能瓶颈
            explain的使用
                explain +sql语句
                    id select_type table type possible_keys key key_len ref rows extra
            explain作用
                表的读取顺序
                数据读取操作的操作类型
                那些索引可以引用
                那些索引被实际使用
                表之间的引用
                每张表有多少行被优化器查询   
              
        事务
            事务概念
                数据库事务是访问并可能操作各种数据项的一个数据库操作序列，
                这些操作要么全部执行，要么全部不执行，是一个不可分割的工作单位。
                事务由事务开始与事务结束之间执行的全部数据库操作组成；
            事务特点-acid
                原子性：Atomicity
                一致性：Consistency
                隔离性：Lsolation
                持久性：Durability
            事务操作
                begin 开始一个事务
                rollback 事务回滚
                commit 事务提交
            
        日志
            统计日志
                slow log:慢查询日志，超出预设的long_query_time 阙值的sql记录
                general log:全局查询日志，所有sql查询的记录
            查看慢查询日志
                查看日志开关：show variables like '%query%';
                打开日志开关：set global slow_query_log='ON';
                设置阙值：set long_query_time=0.01;
                执行sql语句
                查看日志内容
            在表中查看日志
                修改日志存放方式：set global log_output='table';
                擦可能表中内容：select * from mysql.slow_log;
            查看全局查询日志
                查看变量信息：show variables like '%general%';
                打开日志开关： set global general_log='ON';
                执行sql语句
                查看表中日志内容： select * from mysql.general_log;
        
    '''


'''redis内存数据库
    redis简介：完全开源免费的高性能的key-value数据库
        支持数据的持久化，可以将内存中的数据保存到磁盘中，重启的时候可以再次加载进行使用；
        不仅仅支持简单的key-value类型的数据，同时还提供list、set、zset、hash等数据结构的存储；
        支持数据的备份，即master-slave模式的数据备份；
        性能极高，redis能读的速度是110000次/s，写的速度是81000次/s；
        redis的所有操作都是原子性的，意思就是要么执行成功要么执行失败完全不执行。单个
        操作是原子性的，多个操作也支持事务，即原子性，通过multi和exec指令包起来；
        支持publish/subscribe，通知，key过期等等特性；
    
    redis下载地址（windows）：https://github.com/microsoftarchive/redis/releases
    下载完成为压缩包，选择路径压缩；
    管理员启动cmd，切换到redis路径 执行： redis-server.exe redis.windows.conf
    redis基本数据结构
        string:是二进制安全的，意思是redis的string可以包含任何数据。最大存储512MB;
        Hash:一个string类型的key和value的映射表，hash特别适合用于存储对象，存储232 -1键值对；
        list：按照插入顺序排序，可以添加一个元素到列表的头部（左边）或者尾部（右边）
        set:无序集合，通过哈希表实现，所以添加 删除，查找的复杂度都是0（1）；
        sorted set:有序集合每个元素都会关联一个double类型的分数，redis正式通过分数来为集合中的成员进行
        从小到大的排序，zest的成员是唯一的，但分数却可以重复；
    
    基本使用
        string : SET key member/GET key       字符串
        Hash:HMSET key field1 'hello' field2 'world'/HGET/HGETALL key field1  字典
        List: 1push key member/1range key 0 10  列表
        Set: asdd key member/smembers key    无序集合
        Sorted Set: zadd key score member/ZRANGEBYSCORE key 0 1000  有序集合
    
    另行打开cmd：切换到redis路径 执行：redis-cli.exe -h 127.0.0.1 -p 6379  连接服务器
        set key value 添加/编辑键值对
        get key 访问键值对
        hmset 'user' name 'value' 'ss'   age 3  新增hash
        hget user name   访问hash
        hgetall user 查看key对应全部信息
        lpush name 'male' 'sss' 新增list
        lrange name 0 10 查询list
        sadd key_set value1 value2 value3 新增set
        smembers key_set  查询set
        zadd key_zset 1 value_1 2 value_2 2 value_3  新增zset
        ZRANGEBYSCORE key_zset 0 1000  查询zset
        

            '''
