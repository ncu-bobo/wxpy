import itchat
import re

import getInfo


@itchat.msg_register('Text')
def text_reply(msg):
    match1 = re.search("hello", msg["Text"])
    match2 = re.search("天气", msg["Text"])
    if match1:
        return "Hello, how are you?"
    elif match2:
        conditions = getInfo.getWeatherInfo()
        res = f"你好，今天是{conditions[0]}，{conditions[1]}天气为{conditions[2]}, 平均气温为{conditions[3]}"
        return res


itchat.auto_login(hotReload=True)
itchat.run()