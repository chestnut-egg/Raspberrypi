import socket
import smtplib
from email.mime.text import MIMEText
import config as mail

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

def ip_send_mail(myip):
    ret = True
    fromaddr = mail.fromaddr
    toaddrs = mail.toaddrs
    username = mail.username
    password = mail.password
    server = smtplib.SMTP(mail.smtp_sever)

    try:
        # 正文
        text = "IP: " + str(myip)

        # 配置标题和正文
        msg = MIMEText(text, 'plain', 'utf-8')
        msg['Subject'] = 'IP For RaspberryPi'
        msg['From'] = fromaddr
        msg['To'] = toaddrs

        # 启动SMTP发送邮件
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(fromaddr, toaddrs, msg.as_string())
        server.quit()

    except Exception:
        ret = False
    return ret

ret = ip_send_mail(get_host_ip())
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
