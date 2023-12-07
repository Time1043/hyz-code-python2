# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/7 16:24
# @File    ：office3v3_email_sending.py.py
# @Function: 配置文件读取、csv文件读取


# 读取配置文件 读取要发送的csv文件
import configparser
import csv
# 邮箱信息发送
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class EmailSender:
    def __init__(self, smtp_server, smtp_port, sender_email, password):
        """ 登录邮箱(邮箱类型、用户信息) """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.password = password

    def send_email(self, receiver_email, subject, body):
        """ 封装邮箱(收件人、邮件主题、邮件内容)、发送邮件(服务器连接、登录账户、发送邮件) """
        msg = MIMEText(body, 'plain', 'utf-8')
        msg['From'] = self.sender_email
        msg['To'] = receiver_email
        msg['Subject'] = Header(subject, 'utf-8')

        try:
            server = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, receiver_email, msg.as_string())
            print(f'邮件发送成功：{receiver_email}')
        except Exception as e:
            print(f'邮件发送失败：{e}')
        finally:
            server.close()


# 配置文件的读取 (一次)
config = configparser.ConfigParser()
config.read('config.ini')
smtp_server = config['EMAIL_SETTINGS']['smtp_server']
smtp_port = int(config['EMAIL_SETTINGS']['smtp_port'])
sender_email = config['EMAIL_SETTINGS']['sender_email']
password = config['EMAIL_SETTINGS']['password']
email_sender = EmailSender(smtp_server, smtp_port, sender_email, password)

# 邮件的发送 (多次)
with open('emails.csv', newline='', encoding='utf-8') as csvfile:
    email_reader = csv.DictReader(csvfile)
    for row in email_reader:
        email_sender.send_email(row['receiver_email'], row['subject'], row['body'])
