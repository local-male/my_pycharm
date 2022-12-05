# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 当前时间 2022/10/8 17:27:28


import pulsar
import time
client = pulsar.Client('pulsar://101.37.145.159:6650')
consumer = client.subscribe('persistent://ve-global/distribute/parkAutoDestroy',subscription_name='test_theme')
while True:
    msg = consumer.receive()
    print("Received message: '%s'" % msg.data())
    consumer.acknowledge(msg)
    time.sleep(0.1)
client.close()
