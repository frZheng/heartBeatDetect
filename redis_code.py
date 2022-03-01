
import redis
# 连接到远程服务器
r = redis.Redis(host='www.lrdkzz.com', port=6379,db=0,password='123456')
# r = redis.Redis(host='localhost', port=6379,db=0,password='123456')
r.set('1080ti', "1234567894512564598896158484456")  # 设置 name 对应的值
data = r['1080ti']
string=str(data,"utf-8")
get_data = r.get('1080ti')
get_string=str(get_data,"utf-8")
print(r['1080ti'])
print(r.get('1080ti'))  # 取出键 name 对应的值
print(type(r.get('1080ti')))  # 查看类型

print(string)
print(get_string)  # 取出键 name 对应的值
print(type(get_string))  # 查看类型

# 关闭连接
r.close()