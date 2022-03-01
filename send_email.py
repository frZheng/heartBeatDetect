

from email.mime.text import MIMEText
import smtplib

import time


def log_string(log, string):
    message = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))+"  "+string
    log.write(message+ '\n')
    log.flush()
    print(message)

def send_mail(to_list, sub, content,log=None):

    mail_host = "smtp.qq.com"
    mail_user = "1546465464@qq.com"
    mail_pass = "dsafsdafga46456+ihfdii"  # qq邮箱smtp生成的密码
    port = 587

    me = "懒人打可转债"+"<"+mail_user+">"
    msg = MIMEText(content, _subtype='plain', _charset='utf-8')
    # msg = content
    msg['Subject'] = sub
    msg['From'] = me
    # for i in to_list:

    # try:
    if 1:
        server = smtplib.SMTP()
        # server = smtplib.SMTP(mail_host,port)
        server.connect(mail_host,port)
        server.login(mail_user, mail_pass)
        for i in range(len(to_list)):
            if log is None:
                print("to "+to_list[i],"")
            else:
                log_string(log, "to " + to_list[i])
            msg['To'] = ";".join([to_list[i]])
            server.sendmail(me, to_list[i], msg.as_string())
        server.close()
        return True
    # except Exception:
    #     print("err")
    #     return False
def send_mail_fun(sub, content,log=None,user_email=["sdadfadfa@qq.com"]):
    mail_to_list = ["safafa@163.com"]  # 目标邮箱
    send_mail(mail_to_list+user_email, sub, content,log)
if __name__ == '__main__':
    mailto_list = ["asfaf@163.com"]  # 目标邮箱
    send_mail(mailto_list + [], 'test', '002212')