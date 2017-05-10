# -*- coding: UTF-8 -*-
import json
import itchat, time
import smtplib
from itchat.content import *
from email.mime.text import MIMEText
from email.header import Header


# 加载配置信息
def load_config():
    f = open("config.json", encoding='utf-8')
    return json.load(f)


class WxMessage:
    name = ''
    type = ''
    msg = ''

    def __init__(self, name, type, msg):
        self.name = name
        self.type = type
        self.msg = msg

# 获取配置信息
config = load_config()

mail_info = config['mail_info']
keys = config['keys']


# 第三方 SMTP 服务
mail_host = mail_info['host']  # 设置服务器
mail_user = mail_info['account']  # 用户名
mail_pass = mail_info['password']  # 口令
mg = WxMessage('', '', '')
sender = mail_info['sender']
receivers = mail_info['receivers']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱


# 注册普通消息
@itchat.msg_register(TEXT)
def friend_msg(msg):
    mg.name = msg.user.nickName
    mg.type = "朋友"
    mg.msg = msg.text
    print_msg(mg)


# 注册群聊消息
@itchat.msg_register(TEXT, isGroupChat=True)
def group_msg(msg):
    mg.name = msg.actualNickName
    mg.type = msg.user.nickName
    mg.msg = msg.text
    print_msg(mg)


# 打印到的消息
def print_msg(mg):

    message_info = "发送类型：" + mg.type + "\n" + "发送人：" + mg.name + "\n" + "内容：" + mg.msg + "\n"

    for item in keys:
        if item in mg.msg:
            send_email(mg, message_info)
            break

    print_log(message_info)


# 如果匹配到消息，进行发送邮件
def send_email(mg, message_info):
    message = MIMEText(message_info, 'plain', 'utf-8')
    message['From'] = Header(mg.type, 'utf-8')
    message['To'] = Header(mg.name, 'utf-8')
    subject = mg.name
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        info = "邮件发送成功"
    except smtplib.SMTPException as e:
        info = e

    print_log(info)


# 输出日志到log
def print_log(msg):
    msg = "\n" + msg
    f = open(config['log_path'], 'ab+')
    f.write(msg.encode("utf-8"))
    f.close()

# 登陆微信
itchat.auto_login(True)
# 运行
itchat.run(True)
