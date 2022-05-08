import miraicle
import datetime
import json
from daka import DaKa

configs = json.loads(open('./config.json', 'r').read())
users = configs["users"]
bot = configs["bot"]

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

@miraicle.scheduled_job(miraicle.Scheduler.every().minute.at('::00'))
def schedule(bot: miraicle.Mirai):
    now = datetime.datetime.now()
    for user in users:
      if int(now.hour) == int(user["schedule"]["hour"]) and int(now.minute) == int(user["schedule"]["minute"]):
        message = doDaka(user["username"], user["password"])
        bot.send_friend_msg(qq=user["qq"], msg=message)
