# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/14 19:34

# 1. 导入 Flask 模块
from flask import Flask

# 2. 创建Flask应用程序实例对象
app = Flask(__name__)#__name__ == __main__

# 3. 定义路由及视图函数
@app.route("/")#静态路由
def hello_world():
    return "<p>Hello, World!</p>/"

@app.route("/demo/")#路径的切换
def demo():
    return "demo"

@app.route("/userinfo/<int:username>/")#todo 动态路由
def user(username):
    return f'这是{username}同学，访问地址：http://127.0.0.1:5000/userinfo/{username}'

#todo cmd切换路径：CD /D D:\python-project
'''
bash执行：
    export FLASK_APP=文件名
    flask run
cmd执行：
    切换到文件对应的路径
    set FLASK_APP=文件名
    flask run
powershell执行：
    切换到文件对应的路径
    $env:FLASK_APP = "文件名"
    flask run
'''#todo 启动的三种方式
# 4. 启动程序
if __name__ == '__main__':
    app.run()
    #flask 服务启动
    #轮询等待，浏览器发起请求
    #一直等到结束服务


