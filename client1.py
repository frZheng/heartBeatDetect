import socket
import time

ip_addr = '192.168.1.1'
port = 9999
id = "xxx"

import os
class Solution:
    # 获取next数组
    def get_next(self, T):
        i = 0
        j = -1
        next_val = [-1] * len(T)
        while i < len(T)-1:
            if j == -1 or T[i] == T[j]:
                i += 1
                j += 1
                # next_val[i] = j
                if i < len(T) and T[i] != T[j]:
                    next_val[i] = j
                else:
                    next_val[i] = next_val[j]
            else:
                j = next_val[j]
        return next_val

    # KMP算法
    def kmp(self, S, T):
        i = 0
        j = 0
        next = self.get_next(T)
        while i < len(S) and j < len(T):
            if j == -1 or S[i] == T[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == len(T):
            return i - j
        else:
            return -1

file_path = r"C:\qskg\log"
# file_path = r"qskg\log"
s = Solution()
kmp_func = s.kmp
INIT_STR = "0.000"
def get_numeracy():
    numeracy = INIT_STR

    # try:
    file_list = sorted(os.listdir(file_path))
    poi_file = os.path.join(file_path,file_list[-1])
    print(poi_file)
    with open(poi_file, "r") as fin:
        lines = fin.readlines()
        if len(lines) > 100:
            lines = lines[:-100]
        for line in lines:
            if ("Total" in line):
                # print("\n\n", line)
                line_split = line.split("|")
                target_str = line_split[1]
                # print(target_str)
                str_1_index = kmp_func(target_str, "Total:")
                numeracy = target_str[str_1_index+6:]
                # print(str_1_index)
                # print(target_str[str_1_index:])
    return numeracy.replace(" ","")
    # except:
    #     print("get_numeracy error")
    #     return numeracy
# numeracy = get_numeracy()
# print(numeracy, len(numeracy))
# exit()
def run_func():
    a = 0
    while True:

        time.sleep(10)
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip_addr,port))
        keepclass = str(id) + "-我已连接" + str(a) + "次"
        numeracy = get_numeracy()
        if numeracy == INIT_STR:
            print("no numeracy")
            continue
        keepclass += "-"
        keepclass += numeracy
        print(keepclass)
        s.send(bytes(keepclass,'UTF-8'))#向服务端发送消息
        s.close()
        a += 1

while True:
    try:
        run_func()
    except:
        print("error")
        time.sleep(1)