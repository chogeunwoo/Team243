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
        print(row_num)
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

def get_dbInsert_diary(diary_title, diary_body, diary_date):
    conn = connection.connection()
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO diary (diary_title, diary_body, diary_date) VALUES (%s, %s, %s);"
        val = (diary_title, diary_body, diary_date)
        cursor.execute(sql,val)
        conn.commit()
    finally:
        cursor.close()
        return "true"

def get_dbSelect_diary():
    try:
        conn = connection.connection()
        with conn.cursor() as cursor:
            sql = "SELECT diary_id, diary_title, diary_body, diary_date FROM test1.diary"
            cursor.execute(sql)
            rows = cursor.fetchall()
    except Exception as e:
        print('->', e)
        rows = None
    finally:
        if conn:
            conn.close()
    return rows

def get_dbUpdate_diary(diary_id, diary_title, diary_body, diary_date):
    conn = connection.connection()
    try:
        cursor = conn.cursor()
        sql = "UPDATE test.diary SET diary_title = " + diary_title + "diary_body = " + diary_body + "diary_date = " + diary_date + "WHERE diary_id = " + diary_id
        val = (diary_title, diary_body, diary_date)
        cursor.execute(sql,val)
        conn.commit()
    finally:
        cursor.close()
        return "true"
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
            post=[]
            for row_data in row:
                post.append(
                    {
                        'pno': row_data[0],
                        'ptitle': row_data[1],
                        'pbody': row_data[2],
                        'email': row_data[3]
                    }
                )
            
            return post
        else:
            return "fail"

def get_dbSelect_pno(pno):
    conn = connection.connection()
    try:
        cursor = conn.cursor()
        sql = "SELECT * FROM test.post where pno=" + "'" + pno + "'"
        cursor.execute(sql)
        row_num = cursor.rowcount
        
    finally:
        cursor.close()
        if row_num > 0:
            row = cursor.fetchall()
            for row_data in row :
                json_object = {
                    'pno': row_data[0],
                    "ptitle": row_data[1],
                    "pbody": row_data[2],
                    "email": row_data[3]
                }
            return json_object
        else:
            return "fail"
