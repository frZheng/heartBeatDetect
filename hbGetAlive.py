from hbServer import client_list
# from hbServer import mongoclient
# from hbServer import kzz_db
# from hbServer import hb_col
import time
# import pymongo
import send_email
import os
import eventlet  # 导入eventlet这个模块
eventlet.monkey_patch()  # 必须加这条代码
filePath = "./all"
alive_txt = "alive.txt"

# # 更新心跳
# def get_heartbeat(name):
#     myclient = pymongo.MongoClient(mongoclient)
#     mydb = myclient[kzz_db]
#     mycol = mydb[hb_col]
#
#     myquery = {"name": name}
#     mydoc = mycol.find(myquery)
#
#     for x in mydoc:
#         return x["now_time"]
#     return -1

# 更新心跳
def get_heartbeat(name):
    import redis

    # 连接到远程服务器
    r = redis.Redis(host='www.lrdkzz.com', port=6379, db=0, password='123456')
    # try:
    # print("get ", name)
    with eventlet.Timeout(2, False):  # 设置超时时间为2秒
        get_data = r.get(name)
        get_string = str(get_data, "utf-8")
        get_data_c = r.get(name + "_c")
        get_string_c = str(get_data_c, "utf-8")
        # print(get_string)
        return [float(get_string),get_string_c]

    return [-1,"0.000"]

def create_path(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
create_path(filePath)
def get_alive():

    start_flag = 0 # 第一次的标志位
    send_flag = [0]*len(client_list) #标记发送了


    while True:
        fout = open(os.path.join(filePath, alive_txt), "w", encoding="utf-8")
        msg = ""
        for i in range(len(client_list)):
            res_list = get_heartbeat(client_list[i])
            hb_time = res_list[0]
            numeracy = res_list[1]
            cur_time = time.time()
            minute_warm = 10
            hb_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(hb_time))
            if cur_time-hb_time>60*minute_warm:
                if send_flag[i] == 0:
                    # print(client_list[i] + "离线,请检查")
                    if start_flag==1:
                        send_email.send_mail_fun(client_list[i]+"离线", client_list[i]+"离线,请检查",None,[])
                        # send_email.send_mail_fun(client_list[i], client_list[i] + "离线,请检查")
                send_flag[i] = 1

                msg += "离线" + "`" + client_list[i] + "`" + hb_time_str + "`" + numeracy + "\n"
            else:
                send_flag[i] = 0
                msg += "在线" + "`" + client_list[i] + "`" + hb_time_str + "`" + numeracy +"\n"

            start_flag = 1
        #     print(client_list[i],hb_time)
        # print(msg)
        fout.write(msg + "完成\n")
        fout.flush()
        fout.close()
        time.sleep(1)

# get_alive()
if __name__ == '__main__':

    while True:
        # get_alive()
        try:
            get_alive()
        except:
            print("error")
            time.sleep(1)






