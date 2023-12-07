# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/7 15:59
# @File    ：office3v2_email_sending.py.py
# @Function: 面向对象


import smtplib
from email.mime.text import MIMEText
from email.header import Header


class EmailSender:
    def __init__(self, smtp_server, smtp_port, sender_email, pwd):
        """ 登录邮箱(邮箱类型、用户信息) """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.pwd = pwd

    def send_email(self, receiver_email, subject, body):
        """ 封装邮箱(收件人、邮件主题、邮件内容)、发送邮件(服务器连接、登录账户、发送邮件) """
        msg = MIMEText(body, 'plain', 'utf-8')
        msg['From'] = self.sender_email
        msg['To'] = receiver_email
        msg['Subject'] = Header(subject, 'utf-8')

        try:
            server = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)
            server.login(self.sender_email, self.pwd)
            server.sendmail(self.sender_email, receiver_email, msg.as_string())
            print('邮件发送成功')
        except Exception as e:
            print(f'邮件发送失败：{e}')
        finally:
            server.close()


# SMTP 服务器信息
smtp_server = "smtp.qq.com"
smtp_port = 465
password = "cxaxewnsvglueijb"
# 邮件发送者和接收者
sender_email = "1665434994@qq.com"
receiver_email = "15218975015@163.com"
# 邮件主题和内容
subject = "这是邮件主题2"
body = "这里是邮件内容2。"

email_sender = EmailSender(smtp_server, smtp_port, sender_email, password)
email_sender.send_email(receiver_email, subject, body)
