# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/15 10:40
''
'''HTTP 请求方法
    
    常用的配置方法
    请求	说明
        GET	获取服务器资源
        POST	新增服务器资源
        PUT	更新服务器资源（客户端提供改变后的完整资源）
        DELETE	删除服务器资源

    接口设计
        查询：get
        新增：post
        修改：put
        删除：delete
    
    get 请求
        # get 请求
        @app.route("/testcase",methods=["get"])
        def select_case():
            return {"code": 0, "msg":"get success"}
    
    post 请求
        # post 请求
        @app.route("/testcase",methods=["post"])
        def post_case():
            return {"code": 0, "msg":"post success"}
    
    put 请求
        # put 请求
        @app.route("/testcase",methods=["put"])
        def put_case():
            return {"code": 0, "msg":"put success"}
    
    delete 请求
        # delete 请求
        @app.route("/testcase",methods=["delete"])
        def delete_case():
            return {"code": 0, "msg":"delete success"}
    
    '''