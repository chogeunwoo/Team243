import pymysql

def connection():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='asd123', db='test', charset='utf8')
    return conn