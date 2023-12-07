# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/7 14:47
# @File    ：office3v1_email_sending.py
# @Function: 消息的自动发送 —— 邮件

import smtplib  # 发邮件：处理SMTP协议
from email.mime.text import MIMEText  # 封装邮件：MIMEtext 只包含文本内容的 MIME 邮件对象
from email.header import Header  # 封装邮件：确保非ASCII字符可以被正确编码和解码

# 邮件发送者和接收者
sender_email = "1665434994@qq.com"
receiver_email = "15218975015@163.com"
# 邮件主题和内容
subject = "这是邮件主题"
body = "这里是邮件内容。"

# 创建 MIMEText 对象
msg = MIMEText(body, 'plain', 'utf-8')
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = Header(subject, 'utf-8')

# SMTP 服务器信息
smtp_server = "smtp.qq.com"
smtp_port = 465  # 或者根据您的邮件服务商的要求更改端口
password = "cxaxewnsvglueijb"

# 发送邮件
try:
    # 创建 SMTP 连接
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.login(sender_email, password)
    # 发送邮件
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("邮件发送成功")
except Exception as e:
    print(f"邮件发送失败: {e}")
finally:
    server.quit()
