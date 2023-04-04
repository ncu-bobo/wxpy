import threading
import time
import itchat
import re
import schedule
import getInfo


@itchat.msg_register('Text')
def text_reply(msg):
    match1 = re.search("hello", msg["Text"])
    match2 = re.search("天气", msg["Text"])
    match3 = re.search("新闻",msg["Text"])
    match4 = re.search("quit", msg["Text"])
    if match1:
        global user_bo
        user_bo = msg['FromUserName']
        print('收到消息：'+msg['FromUserName'])
        return "波波一号已成功对接！"
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
    elif match4:
        itchat.logout()
        print('账号成功退出！')

def push_message():
    print('每日新闻推送')
    conditions = getInfo.getWeatherInfo()
    dateArray = conditions[0].split('-')
    res = f"你好吖，今天是{dateArray[0]}年{dateArray[1]}月{dateArray[2]}日。\n{conditions[1]}天气为{conditions[2]}, 平均气温为{conditions[3]}°C。" \
          f"\n今天也要多多加油哦！"
    itchat.send_msg(res, toUserName=user_bo)
    news = getInfo.getNewsInfo()
    res = "每日新闻快看："
    itchat.send_msg(res, toUserName=user_bo)
    for index, value in enumerate(news):
        res = f"{index + 1}: {value}\n"
        itchat.send_msg(res, toUserName=user_bo)

#使用独立线程
def run_wechat():
    itchat.run()

if __name__ == '__main__':
    # 登录微信
    itchat.auto_login(hotReload=True, enableCmdQR=True)
    # 启动一个新线程来运行itchat.run()方法
    wechat_thread = threading.Thread(target=run_wechat)
    wechat_thread.start()

    # 定时任务
    schedule.every().day.at("16:11").do(push_message)

    while True:
        schedule.run_pending()
        time.sleep(1)