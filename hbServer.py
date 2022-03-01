import socket
import datetime
import numpy as np
from multiprocessing import Process
import time
import threading
# import redis
# import pymongo
# 用ifconfig 查看的IP
ip_addr_innet = "192.168.1.1"
# ip_addr_innet = '127.0.0.1'
port = 9999

# mongoclient = "mongodb://localhost:27017/"
# kzz_db = 'heartbeat'
# hb_col = "cur_hb"


client_list = ["1080ti",
               "3090x1",
               "6400",
               "6700",
                "7100k",
                "393012k",
                # "xuniji",
               ]




def updata_heartbeat(name, now_time, numeracy):

    import redis
    # 连接到远程服务器
    # r = redis.Redis(host='www.lrdkzz.com', port=6379, db=0, password='123456')
    r = redis.Redis(host='localhost', port=6379,db=0,password='123456')
    r.set(name, str(now_time))  # 设置 name 对应的值
    # data = r['1080ti']
    r.set(name+"_c", numeracy)  # 设置 name 对应的值
    return True

def Wait_connection():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip_addr_innet, port))
    s.listen(1)
    s.settimeout(None)
    while True:  # 第四步：服务端做连接循环的接，可以做到接收多个人发的连接
        print('服务端开始运行了')
        conn,addr=s.accept()
        print('双向链接是', conn)  # 打印conn：
        print('客户端地址', addr)  # 打印addr：
        t = threading.Thread(target=keep_alive, args=(conn, addr))
        t.start()


def keep_alive(conn, addr):

    max_try = 5
    while max_try:
        try:
            client_msg=conn.recv(1024)#客户端发送过来的消息
            client_msg_str = str(client_msg, 'utf-8')
            str_split = client_msg_str.split("-")
            id = str_split[0]
            numeracy = str_split[2]
            starttime = time.time()
            for i in range(len(client_list)):
                if id == client_list[i]:
                    updata_heartbeat(client_list[i],starttime,numeracy)

            print('client msg: %s' %(client_msg_str))
            conn.close()
            break
        except:
            print("error")
            time.sleep(1)
            max_try -= 1



def net_is_used(port,ip='127.0.0.1'):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((ip,port))
        s.shutdown(2)
        print('%s:%d is used' % (ip,port))
        return True
    except:
        print('%s:%d is unused' % (ip,port))
        return False

if __name__ == '__main__':
    port_is_used = True
    while port_is_used:
        port_is_used = net_is_used(port,ip_addr_innet)
        time.sleep(0.5)

    # starttime = time.time()
    starttime = datetime.datetime.now() - datetime.timedelta(days=1)
    starttime = starttime.timestamp()
    print(starttime)
    # exit()
    for i in range(len(client_list)):
        updata_heartbeat(client_list[i],starttime,"0.000")
    Wait_connection()



