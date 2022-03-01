# 文件上传
import flask, os, sys, time
from flask import request

# 文件存储的路径
filePath = "./all"
your_port = 9998  # 开放的端口

IpAddr = "192.168.1.1"
IpAddr_out = "192.168.1.2"

interface_path = os.path.dirname(__file__)
sys.path.insert(0, interface_path)  # 将当前文件的父目录加入临时系统变量

server = flask.Flask(__name__, static_folder='static')

alive_txt = "alive.txt"

def create_path(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


create_path(filePath)

log_file_name = "log.txt"
abs_log_file_name = os.path.join(filePath, log_file_name)

array = []

if os.path.isfile(abs_log_file_name):
    with open(abs_log_file_name, "r") as fin:
        for line in fin.readlines():
            line = line[:-1]  # 去掉\n
            line_list = line.split(",")
            array.append((line_list[0], line_list[1]))
print(abs_log_file_name)
log = open(abs_log_file_name, 'a')  # append the log



@server.route('/', methods=['get'])
def index():
    # 读取文件
    print("index")
    # 10秒刷新一次
    h2 = '<script type="text/javascript"> function myrefresh() {window.location.reload();} setTimeout(\'myrefresh()\',10000); </script>'
    # 0.1秒刷新
    h3 = '<script type="text/javascript"> function myrefresh() {window.location.reload();} setTimeout(\'myrefresh()\',100); </script>'
    # h2 = '<meta http-equiv="refresh" content="5;url=http://{}:{}/"> '.format(IpAddr_out, str(your_port))
    try:
        with open(os.path.join(filePath,alive_txt),"r",encoding="utf-8") as fin:
            lines = fin.readlines()
            h4 = '<table border="1"><tr><th>状态</th><th>机器名</th><th>时间</th><th>num</th></tr>'
            h5 = '<table border="1"><tr><th>状态</th><th>机器名</th><th>时间</th><th>num</th></tr>'
            if len(lines) < 1:
                return "无数据" + h3

            if "完成" in lines[-1]:
                lines = lines[:-1]
                for i in lines:
                    if i[-1] == "\n":
                        i = i[:-1]
                    i_list = i.split("`")
                    if i_list[0] == "在线":
                        h4 += '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(i_list[0],i_list[1],i_list[2],i_list[3])
                    else:
                        h5 += '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(i_list[0],i_list[1],i_list[2],i_list[3])
            else:
                return "请等待下次刷新" + h3
            h4 += '</table>'
            h5 += '</table>'
        h1 = '<h2>在线机器</h2> ' + h4 + '<hr>'

        h1 += '<h2>离线机器</h2> ' + h5 + '<hr>'

        return h1 + h2
    except:
        return "未知错误" + h3



print('----------路由和视图函数的对应关系----------')
print(server.url_map)  # 打印路由和视图函数的对应关系
server.run(host='0.0.0.0', port=your_port, debug=True)  # 任何电脑都能访问，需要电脑开启端口的外部访问
# server.run(port=your_port) #只能本地访问




