#coding=utf-8
import pprint,json,requests




#获取token
def token():
    url = "https://ts.keytop.cn/unity/service/open/app/login"
    header = {"Content-Type":"application/json"}
    data = {"phone":"13892115849","mobileCode":"0592","loginWay":"PC_WEB","expireDay":""}
    res = requests.post(url,json=data,headers=header)
    token = res.json()["data"]["ktToken"]
    return token

#获取token
def unit_login(phone):
    url='https://ts.keytop.cn/unity/service/open/app/login'
    # token = json.loads(response2.text)['data']['token']
    kt_header=Unit_login.kt_header#请求头
    data={
      "phone": phone,
      "mobileCode": "0592",
       "loginWay": "PC_WEB"
     }
    response2 = requests.post(url=url,data=json.dumps(data), headers=kt_header)
    token = json.loads(response2.text)['data']['ktToken']
    return token

#获取请求头
def setLotCache(phone):
    url='https://ts.keytop.cn/unity/user/setLotCache'
    kt_token=unit_login(phone)
    kt_header=Unit_login.kt_header
    kt_header['kt-token']=kt_token
    data={"lotId": ktdn.lotId}
    response2 = requests.post(url=url, data=json.dumps(data), headers=kt_header)
    #print(response2.text)
    return  kt_header


#排序并且拼接字符串
def sort(datas):
    data = json.dumps(datas)
    d= json.loads(data)                #字典转换列表后的第一个元素排序
    dat = sorted(d.items(), key=lambda item: item[0],reverse=False)#匿名函数  默认正序排序 reverse=False
    a = dict(dat)
    dt = ""
    for key, value in a.items():#拼接
        if isinstance(value, list) or isinstance(value,dict) or (value==None) or isinstance (value,int):
        # if isinstance(value, list):
            continue
        dt = dt + key + "=" + str(value) + "&"

    dt = dt[:-1]
    return dt


def get_sign(datas):
    data = sort(datas)
    print(data)
    sign = data + "&" + str(appSecret)  #unit.appSecret
    #logger.info(sign)
    return sign


def GetParkingPaymentInfo():
    url = 'http://tsktapps.keytop.cn/unite-api/api/wec/GetParkingPaymentInfo'
    kt_header=setLotCache(Unit_login.phone)
    kt_header['kt-appId'] = ktdn.kt_appid
    kt_header['kt-lotcodes'] = ktdn.lotId
    data = { "parkId": "{}".format(ktdn.kt_lotcodes),'plateNo':'闽ABC211','appId':'{}'.format(ktdn.kt_appid)}
    response = requests.post(url=url, headers=kt_header,data=json.dumps(data))
    return response

if __name__ == '__main__':
    # data = {"appId": "10038",
    #         "key": "{{key}}",
    #         "parkId": "210037159",
    #         "serviceCode": "getParkingFlowReport",
    #         "ts": "{{ts}}",
    #         "reqId": "{{reqId}}",
    #         "startTime": "2022-03-02 00:00:00",
    #         "endTime": "2022-03-29 23:59:59"
    #         }
    # res = sort(data)
    # print(res)
    # res = get_sign(data)
    # print(res)
    # res = GetParkingPaymentInfo()
    # print(res)
    appSecret = 1615316921
    datas = {"appId": "appSercert","key": "{{key}}","parkId": "210037159","reqId": "{{reqId}}",
             "serviceCode": "getCarCardInfo","ts": "{{ts}}","cardId":1,"state":0}
    sort_1 = sort(datas)
    print(sort_1)
    pinjie_1 = get_sign(datas)
    print(pinjie_1)