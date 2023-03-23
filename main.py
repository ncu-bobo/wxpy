import itchat
import re

import getInfo


@itchat.msg_register('Text')
def text_reply(msg):
    match1 = re.search("hello", msg["Text"])
    match2 = re.search("天气", msg["Text"])
    match3 = re.search("新闻",msg["Text"])
    if match1:
        return "Hello, how are you?"
    elif match2:
        conditions = getInfo.getWeatherInfo()
        dateArray = conditions[0].split('-')
        res = f"你好吖，今天是{dateArray[0]}年{dateArray[1]}月{dateArray[2]}日。\n{conditions[1]}天气为{conditions[2]}, 平均气温为{conditions[3]}°C。" \
              f"\n今天也要多多加油哦！"
        return res
    elif match3:
        news = getInfo.getNewsInfo()
        res = f"每日新闻快看：\n"
        itchat.send_msg(res, toUserName=msg['FromUserName'])
        for index, value in enumerate(news):
            res = f"{index+1}: {value}\n"
            itchat.send_msg(res, toUserName=msg['FromUserName'])


itchat.auto_login(hotReload=True)
itchat.run()