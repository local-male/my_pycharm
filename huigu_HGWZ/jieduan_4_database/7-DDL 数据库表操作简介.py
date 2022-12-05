# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/27 12:36
''
'''DDL 数据库表操作简介
    目录
        MySQL 的数据类型
        常用数据类型
    
    MySQL 的数据类型
        数字类型
        字符串类型
        日期和时间类型
    
    数字类型
        数据类型	说明
        TINTINT	0～255 或 -128～127，1字节，最小的整数
        SMALLINT	0～65535 或 -32768～32767，2字节，小型整数
        MEDIUMINT	0～16777215 或 -8388608～8388607，3字节，中型整数
        INT	0～4294967295 或 -2147683648～2147683647，4字节，标准整数
        BIGINT	8字节，大整数
        FLOAT	单精度浮点值
        DOUBLE	双精度浮点值
        BOOLEAN	布尔值 
    
    字符串类型
        数据类型	说明
        CHAR	1～255 个字符，固定长度字符串
        VARCHAR	长度可变，最多不超过 255 个字符
        TEXT	最大长度为 64K 的变长文本
        TINYTEXT	与 TEXT 相同，但最大长度为 255 字节
        MEDIUMTEXT	与 TEXT 相同，但最大长度为 16K
        LONGTEXT	与 TEXT 相同，但最大长度为 4GB
    
    日期和时间类型
        数据类型	说明
        DATE	日期，格式 YYYY-MM-DD
        TIME	时间，格式 HH:MM:SS
        DATETIME	日期和时间，格式 YYYY-MM-DD HH:MM:SS
        TIMESTAMP	时间标签，功能和 DATETIME 相同，但范围较小
        YEAR	年份可指定两位数字和四位数字的格式
    
    常用数据类型
        INT：整型
        DOUBLE：浮点型
        VARCHAR：字符串型
        DATE：日期类型
    
    
    '''