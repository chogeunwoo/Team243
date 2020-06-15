import pymysql
import connection
import json

def get_dbInsert_register(name, email, pw, phone_num):
    conn = connection.connection()
    try:
        sql = "SELECT email FROM test.os_member where email =" + "'" + email + "'"
        cursor = conn.cursor()
        cursor.execute(sql)
        row_num = cursor.rowcount
    finally:
        cursor.close()
    if row_num > 0:
        return "fail"
    else:
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO os_member (name, email, pw, phone_num) VALUES (%s, %s, %s, %s);"
            val = (name, email, pw, phone_num)
            cursor.execute(sql,val)
            conn.commit()
        finally:
            cursor.close()
            return "true"

def get_dbSelect_register(email,pw):
    conn = connection.connection()
    try:
        cursor = conn.cursor()
        sql = "SELECT email FROM test.os_member where email=" + "'" + email + "'" + "AND pw=" + "'" + pw +"'"
        cursor.execute(sql)
        row_num = cursor.rowcount
    finally:
        cursor.close()
        if row_num > 0:
            row = cursor.fetchall()
            for row_data in row :
                json_object = {
                    "email": row_data[0]
                }
            return json_object
        else:
            return "fail"

def get_dbInsert_post(title,body,email):
    conn = connection.connection()
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO post (ptitle, pbody, email) VALUES (%s, %s, %s);"
        val = (title, body, email)
        cursor.execute(sql,val)
        conn.commit()
    finally:
        cursor.close()
        return "true"

def get_dbSelect_post():
    conn = connection.connection()
    try:
        cursor = conn.cursor()
        sql = "SELECT * FROM test.post"
        cursor.execute(sql)
        row_num = cursor.rowcount
    finally:
        cursor.close()
        if row_num > 0:
            row = cursor.fetchall()
            post_list[]
            for row_data in row :
                json_object = {
                    "pno": row_data[0]
                    "ptitle": row_data[1]
                    "pbody": row_data[2]
                    "email": row_data[3]
                }
                post_list[row_data]
                print (post_list[row_data])
            
            #json.dumps(row)
            # print(json.dumps(row))
            return post_lsit#json.dumps(row)
        else:
            return "fail"