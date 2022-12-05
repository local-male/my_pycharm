# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 当前时间 2022/8/4 17:54:09
from bottle import *
import json

@route('/all',method='POST')
def receive():
    data =request.body.readlines()
    print("私有化上报")
    for i in range(len(data)):
        string = str(data[i], 'utf-8')
        print(string)

    pay_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(pay_time)
    data={"data":"PostCarInInfo"}
#根据第三方被用户扫接口，要求的返回参数格式，构造返回值
    dt = {"resCode": 0, "data": str(data), "resMsg": 'string'}
    dt = json.dumps(dt)
    return dt

run(host='10.lianxi.6.198', port='9898', reloader=True)