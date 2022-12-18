# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/10/24 8:24
''
'''file_yaml
    一种数据序列化格式
    用于人类的可读性和与脚本语言的交互
    一种被认为可以超越 XML、JSON 的配置文件
    
    YAML 基本语法规则
    大小写敏感
    使用缩进表示层级关系
    缩进时不允许使用 Tab 键，只允许使用空格
    缩进的空格数目不重要，只要相同层级的元素左侧对齐即可
    # 表示注释，从这个字符一直到行尾，都会被解析器忽略
    
    YAML 支持的数据结构
    对象：键值对的集合，用冒号 “:” 表示
    数组：一组按次序排列的值，前加 “-”
    纯量：单个的、不可再分的值
    字符串
    布尔值
    整数
    浮点数
    Null
    时间
    日期
# 编程语言
languages:
  - PHP
  - Java
  - Python 
book:
  Python入门: # 书籍名称
    price: 55.5
    author: Lily
    available: True
    repertory: 20
    date: 2018-02-17
  Java入门:
    price: 60
    author: Lily
    available: False
    repertory: Null
    date: 2018-05-11
    
    PyYAML
    Python 的 YAML 解析器和生成器
    官网：https://pypi.org/project/PyYAML/
    安装：pip install pyyaml
    
    
    创建 file_yaml 文件
import file_yaml
data = {
    "client": {"default-character-set": "utf8"},
    "mysql": {"user": 'root', "password": 123},
    "custom": {
        "user1": {"user": "张三", "pwd": 666},
        "user2": {"user": "李四", "pwd": 999},
    }
}
# 直接 dump 可以把对象转为 YAML 文档
with open('./my.file_yaml', 'w', encoding='utf-8') as f:
    file_yaml.dump(data, f, allow_unicode=True)
    
    
    读取 file_yaml 文件
import file_yaml
file_path = './my.file_yaml'
with open(file_path, 'r', encoding='utf-8') as f:
    data = file_yaml.safe_load(f)
print(data)

    '''