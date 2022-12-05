# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/15 10:47

from flask import Flask
app = Flask(__name__)

# get 请求   methods 是list
@app.route("/testcase", methods=["get"])
def select_case():
    return {"code": 0, "msg": "get success"}


# post 请求
@app.route("/testcase",methods=["post"])
def post_case():
    return {"code": 0, "msg":"post success"}

# put 请求
@app.route("/testcase",methods=["put"])
def put_case():
    return {"code": 0, "msg":"put success"}

# delete 请求
@app.route("/testcase",methods=["delete"])
def delete_case():
    return {"code": 0, "msg":"delete success"}


if __name__ == '__main__':
    app.run()