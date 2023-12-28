import mysql.connector
import re
from minio import Minio
import time
import requests
from minio.error import S3Error

# 建立连接
conn = mysql.connector.connect(
    host="192.168.232.133",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="root",  # 数据库密码
    database="sql_kf_douyin"  # 要连接的数据库
)

# 设置代理字典
proxies = {
    "http": "http://127.0.0.1:10809",
    "https": "http://127.0.0.1:10809",
}

client = Minio(
    "192.168.232.133:9000",
    access_key="hRLjfyCGyguiXui0KnA6",
    secret_key="ApKD6jMfGdQoMlN1hBarqDjwRamPXz7qnmVD50kH",
    secure=False  # 设置为False如果你的MinIO服务器不是运行在HTTPS上
)
bucket_name = "chat"

# 创建游标对象
cursor = conn.cursor()

# 执行SQL语句
cursor.execute("SELECT * FROM wolive_chats")

# 获取所有记录
records = cursor.fetchall()


def fileupload(file, url):
    print(url)
    response = requests.get(url, proxies=proxies)
    with open('./file/tmp.jpg', 'wb') as f:
        f.write(response.content)
    client.fput_object(bucket_name, file, "./file/tmp.jpg")



def formate_row(row):
    cid = row[0]
    visiter_id = row[1]
    service_id = row[2]
    business_id = row[3]
    content = row[4]
    timestamp = row[5]
    state = row[6]
    direction = row[7]
    unstr = row[8]
    avatar = row[9]
    match = re.search(r'src="([^"]+)"', content)
    if match:
        content = match.group(1)
        if "kf.douyin" not in content:
            content = "https://kf.douyin68.com" + content
        source_pic = content.split("/")[-1]
        fileupload(source_pic, content)
    rows = [cid, visiter_id, service_id, business_id, content, timestamp, state, direction, unstr, avatar]
    print(rows)


# 遍历结果
for row in records:
    formate_row(row)
    cid = row[0]
    visiter_id = row[1]
    service_id = row[2]
    business_id = row[3]
    content = row[4]
    timestamp = row[5]
    state = row[6]
    direction = row[7]
    unstr = row[8]
    avatar = row[9]
    # print(content)

# 关闭游标和连接
cursor.close()
conn.close()
