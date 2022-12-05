# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 当前时间 2022/10/8 13:22:08
import allure
from keytop.common import *

# 内部车查询 2.2.2
@allure.title('内部车查询')
def test_demo_1():
    url_request = '/api/wec/GetCarCardInfo'
    body = {"appId": 10031, "parkId": parkId['male'], "reqId": reqId,
                "serviceCode": "getCarCardInfo", "ts": ts, "cardId": 13022, "state": 0}
    demo(url_request,body,header)

# 内部车新增2.2.lianxi
@allure.title('新增内部车')
def test_demo_2():
    url_request = '/api/wec/AddCarCardNo'
    body = {
        "appId": 10031,
        "parkId": parkId['male'],
        "reqId": reqId,
        "serviceCode": "addCarCardNo",
        "ts": ts,
        "userId": "0",
        "userName": "male",
        "cardInfo": "{\"cardName\":\"卡片3\",\"remak\":\"备注3\",\"roomId\":\"房间3\",\"tel\":\"phone\",\"useName\":\"车主名称\"}",
        "plateNoInfo": "[{\"etcNo\":\"161531\",\"plateNo\":\"沪ABC101\"}]",
        "carLotList": "[{\"areaId\":[\"-lianxi\"],\"areaName\":\"所有区域\",\"carType\":2,\"lotCount\":lianxi,\"lotName\":\"车位3\",\"sequence\":lianxi}]"
    }
    demo(url_request,body,header)

# 远程开闸
@allure.story('开闸')
@allure.title('远程开闸')
def test_demo_3():
    url_request = '/api/control/RemoteOpen'
    body = {"appId": 10031, "parkId": parkId['male'], "reqId": reqId,
            "serviceCode": "remoteOpen", "ts": ts, "nodeId": 139, "type": 0}
    demo(url_request, body, header)


#内部车充值
def test_demo_4():
    url_request = '/api/carCard/RechargeByUser'
    body = {
    "appId":10031,
    "parkId":parkId['male'],
    "serviceCode":"rechargeByUser",
    "ts":ts,
    "reqId":reqId,
    "beginTime":"2022-01-01",
    "endTime":"2022-12-06",
    "cardId":13024,
    "cardType":2,
    "cardTypeName":"月租车",
    "rechargeUnit":1,
    "chargeAmount":1,
    "chargeNumber":1,
    "freeNumber":0,
    "freeUnit":1,
    "orderNum":"P2100371590020220629140556165000078",
    "payMethod":1001,
    "remark":"备注"
}
    demo(url_request,body,header)



