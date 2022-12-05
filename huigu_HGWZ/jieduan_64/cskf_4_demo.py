# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/16 15:03
''


from flask import Flask,request
from keytop.log_utils import logger

app = Flask(__name__)
@app.route('/login/',methods=['get'])
def login():
    logger.info(f'请求参数为：{request.args}')
    result = request.args
    a = result.get('a')
    b = result.get('b')
    print(f'a = {a},b = {b}')#todo 获取字典中的值
    return {'codo':0,'msg':'get success'}

#post——json 格式
@app.route('/regist/',methods=['post'])
def post_regist():
    logger.info(request.json)
    return {'code':0,"msg":'post success'}


#post--form 格式
@app.route('/regist1',methods=['post'])
def post_regist1():
    logger.info(request.form) #需改动位置
    return {'code':0,"msg":'post form success'}

@app.route('/regist2',methods=['put'])
def post_regist2():
    logger.info(request.form)
    return {'code':0,"msg":'post form success'}

#处理前端发来的form表单
@app.route('/regist3',methods=['put'])
def post_regist3():
    logger.info(request.form)
    username = request.form.get('username')
    password = request.form.get('password')
    logger.info(f'username:{username},password:{password}')
    return {'code':0,"msg":'put success'}


#post  文件保存   处理前端发来的文件请求
@app.route('/regist4/',methods=['post'])
def post_regist4():
    file_object = request.files.get('file')
    logger.info(file_object)
    logger.info(f'文件名为：{file_object.filename}')
    file_object.save('./pictures/logo.jpg')
    return {'code':0,"msg":'post file success'}

if __name__ == '__main__':
    app.run()