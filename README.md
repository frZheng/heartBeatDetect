# heartBeatDetect
电脑心跳检测, 网页查看远程电脑是否死机与算力.



client1.py

客户机使用的, 用于检测本地算力发送心跳. 查看的是本地的log文件, 使用的是nbminer38, 如果有旧日志可以删除. 因为在读取文件的时候有排序, 然后区最后一个文件的倒数100行, 如果命名不根据时间排序可能会出错, 为了防止万一, 直接把所有日志全部删除就好.



hbServer.py

修改ip_addr_innet为阿里云的内网地址. client_list是客户机发送的名称, 与客户端的名称一一对应.



hbWeb.py

修改IpAddr为阿里云的内网地址, IpAddr_out为阿里云的外网地址.



send_email.py

修改mail_host为邮箱服务器的域名. mail_user为邮箱. mail_pass为POP3/SMTP的秘钥,可以在邮箱生成.



