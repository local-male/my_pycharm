# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 当前时间 2022/9/20 15:42:50
import allure
import requests
from keytop import get_conn
from keytop.log_utils import logger

    #测试内部车demo
class TestDemo:
    # 获取token
    def setup_class(self):
        url = 'https://ts.keytop.cn/unity/service/open/app/login'
        body = {"phone": "13892115849", "mobileCode": "0592"}
        res = requests.post(url=url, json=body)
        self.token = res.json()['data']['ktToken']
        return self.token

    # 禁用内部车
    @allure.story('内部车')
    @allure.title('禁用内部车')
    def test_cancle(self):
        self.lotcodes = '210037159'
        self.headers = {'kt-token': self.token, 'kt-appId': '16bbf366b49a48fab362b7f163d96c63',
                        'kt-lotcodes': self.lotcodes}
        url = 'https://ipark-test.keytop.cn/nkc/card/cancel'
        body = {"id": "12996", "lotCode": self.lotcodes}
        res = requests.post(url=url, json=body, headers=self.headers)
        logger.info(res.json())
        logger.info(res.status_code)

    # 启用内部车
    @allure.story('内部车')
    @allure.title('启用内部车')
    def test_recover(self):
        headers = {'kt-token': self.token, 'kt-appId': '16bbf366b49a48fab362b7f163d96c63',
                   'kt-lotcodes': '210037159', "authCode": "inside/inside-manage/cancel"}
        self.ID = '210037159'
        url = 'https://ipark-test.keytop.cn/nkc/card/recover'
        body = {"id": "12996", "lotCode": self.ID}
        res = requests.post(url=url, json=body, headers=headers)
        logger.info(res.json())
        logger.info(res.status_code)

    # 2.2.1固定车新增接口
    @allure.title('新增内部车')
    @allure.story('内部车')
    def test_add(self):
        url = 'https://ipark-test.keytop.cn/nkc/card/addCard'
        body = {"cardInfo":{
            "cardNo":"","del":"","deleted":"0","lotCode":"592012419","name":"车主名称","overLotCount":0,"remark":"",
            "tel":"手机号","address":"","effectiveTime":""},"cardCarInfo":[{
            "edit":True,"carNoFull":"闽XYZ211","province":"闽","cardNo":"","lotCode":"","remark":"","deleted":"0",
            "carNo":"XYZ210"}],"cardLotInfo":[{
            "edit":True,"cardType":"2","lotCode":"592012419","area":"","lotCount":1,"lotName":"","areaId":["-lianxi"],
            "allArea":False,"ruleId":""}]}
        self.headers = {'kt-token': self.token, 'kt-appId': '16bbf366b49a48fab362b7f163d96c63',
                        'kt-lotcodes': '210037159','authCode':'inside/inside-manage/add'}
        res = requests.post(url=url, json=body, headers=self.headers)
        logger.info(res.json())

        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT A.id, A.name, B.carNo,C.lotCount from t_210037159_card A "
                       "INNER JOIN t_210037159_card_car B ON A.id = B.cardId INNER JOIN t_210037159_card_lot C "
                       "ON A.id = C.cardId AND B.carNo = 'XYZ210';")
        record = cursor.fetchone()
        logger.debug('************')
        logger.debug(f'数据库打印出来的类型为：{type(record)}')
        logger.info(f'数据库取到的数据为：{record}')
        list_record = list(record) #将元组转换为列表
        assert list_record[1] == '车主名称'
        assert list_record[2] == 'XYZ210'
        assert list_record[3] == 1
        logger.info(f'获取到的内部车cardId为：{list_record[0]}')
        return list_record[0]


    # 禁用套餐类型
    @allure.story('套餐类型')
    @allure.title('禁用A套餐类型')
    def test_status(self):
        headers = {'kt-token': self.token, 'kt-appId': '16bbf366b49a48fab362b7f163d96c63',
                   'kt-lotcodes': '210037159', "authCode": "inside/inside-config/enable"}
        url = 'https://ipark-test.keytop.cn/nkc/cardConfig/saveStatus'
        body = {"lotCode": "210037159", "id": 1000896, "status": 0}
        res = requests.post(url=url, json=body, headers=headers)
        logger.info(res.json())
        logger.info(res.headers)

    #2.2.2固定车查询接口
    @allure.title('查询内部车')
    @allure.story('内部车')
    def test_getcarcardinfo(self):
        headers = {'kt-token': self.token, 'kt-appId': '16bbf366b49a48fab362b7f163d96c63',
                   'kt-lotcodes': '210037159'}
        url = 'https://ipark-test.keytop.cn/nkc/card/queryCardList'
        body = {"lotCode":"210037159","carNo":"闽XYZ211","name":"","tel":"","lotName":"","address":"",
                "cardType":"","cardStatus":0,"startDate":"","endDate":"","expireStartDate":"",
                "expireEndDate":"","cardNo":"","contact":"","assist":"","currentPage":1,"pageSize":20}
        res = requests.post(url = url,json=body,headers=headers)
        logger.info(res.json())

    def class_teardown(self):
        logger.info('-----用例执行结束-------')
