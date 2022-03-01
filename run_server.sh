#!/bin/bash
#rm server.txt
rm get_alive.txt
rm nohup.out


PROCESS=`ps -ef | grep hbServer.py | grep -v grep | awk '{print $2}' | xargs kill -9`
PROCESS=`ps -ef | grep hbGetAlive.py | grep -v grep | awk '{print $2}' | xargs kill -9`
PROCESS=`ps -ef | grep hbWeb.py | grep -v grep | awk '{print $2}' | xargs kill -9`

sleep 10 #时间需要长一点,否则断开连接后再打开可能无法打开,这种等待还是存在问题

# ps -ef |grep python
nohup /root/anaconda3/bin/python hbServer.py &
nohup /root/anaconda3/bin/python hbGetAlive.py >> get_alive.txt &
nohup /root/anaconda3/bin/python hbWeb.py >> hbWeb.txt &