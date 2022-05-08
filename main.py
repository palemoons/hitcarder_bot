from daka import DaKa
from halo import Halo
from apscheduler.schedulers.blocking import BlockingScheduler
import miraicle
from plugins import *
import getpass
import time
import datetime
import os
import sys
import requests
import json
import re


def doDaka(username, password):
    print("🚌 打卡任务启动")
    dk = DaKa(username, password)
    try:
        dk.login()
    except Exception as err:
        message = str(err)
        return message

    print('正在获取个人信息...')
    try:
        dk.get_info()
    except Exception as err:
        print('获取信息失败，请手动打卡，更多信息: ' + str(err))
        message = '获取信息失败，请手动打卡，更多信息: ' + str(err)
        return message

    try:
        res = dk.post()
        if str(res['e']) == '0':
            print('打卡成功')
            message = '打卡成功'
        else:
            print(res['m'])
            message = res['m']
    except:
        print('数据提交失败')
        message = '数据提交失败'
        return message
    return message


def main():
    if os.path.exists('./config.json'):
        configs = json.loads(open('./config.json', 'r').read())
        users = configs["users"]
        bot = configs["bot"]
    else:
        print('⚠️未在当前目录下检测到配置文件')
        return

    for user in users:
        message = doDaka(user["username"], user["password"])
        bot.send_friend_msg(qq=user["qq"], msg=message)

    @miraicle.Mirai.receiver('FriendMessage')
    def receive_daka(bot: miraicle.Mirai, msg: miraicle.FriendMessage):
        if msg.plain in ['/打卡']:
            user = [user for user in users if user["qq"] == msg.sender][0]
            message = doDaka(user["username"], user["password"])
            bot.send_friend_msg(qq=user["qq"], msg=message)

    bot = miraicle.Mirai(qq=bot["qq"], verify_key=bot["verify_key"], port=bot["port"])
    bot.run()
    

if __name__ == "__main__":
    main()
