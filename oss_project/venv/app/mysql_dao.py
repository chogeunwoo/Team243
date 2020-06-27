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

def get_dbInsert_changeMyinfo(name, email, pw, phone_num):
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

def get_dbSelect_myinfo(email):
    conn = connection.connection()
    try:
        cursor = conn.cursor()
        sql = "SELECT name, email, pw, phone_num FROM test.os_member where email=" + "'" + email + "'"
        cursor.execute(sql)
        row_num = cursor.rowcount
    finally:
        cursor.close()
        if row_num > 0:
            row = cursor.fetchall()
            for row_data in row :
                json_object = {
                    "name": row_data[0],
                    "id": row_data[1],
                    "pw": row_data[2],
                    "phone_num": row_data[3]
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
            #json.dumps(row)
            # print(json.dumps(row))
            return post #json.dumps(row)
        else:
            return ""

def get_dbDelete_post(pno):
    conn = connection.connection()
    try:
        cursor = conn.cursor()
        sql = "DELETE FROM test.post WHERE pno =" + pno
        cursor.execute(sql)
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
    conn = connection.connection()
    try:
        cursor = conn.cursor()
        sql = "SELECT diary_id, diary_title, diary_body, diary_date FROM test.diary"
        cursor.execute(sql)
        conn.commit()
        row_num = cursor.rowcount
    finally:
        cursor.close()
        if row_num > 0:
            row = cursor.fetchall()
            post=[]
            for row_data in row:
                post.append(
                    {
                        'diary_id': row_data[0],
                        'diary_title': row_data[1],
                        'diary_body': row_data[2],
                        'diary_date': row_data[3]
                    }
                )
            #json.dumps(row)
            # print(json.dumps(row))
            return post #json.dumps(row)
        else:
            return "fail"

def get_dbUpdate_diary(diary_id, diary_title, diary_body, diary_date):
    conn = connection.connection()
    try:
        cursor = conn.cursor()
        sql = "UPDATE `test.diary` SET `diary_title` = %s `diary_body` = %s `diary_date` = %s WHERE `diary_id` = %s"
        cursor.execute(sql, (diary_title, diary_body, diary_date, diary_id))
        conn.commit()
    finally:
        cursor.close()
        return "true"

def get_dbMore_diary(diary_id):
    conn = connection.connection()
    try:
        cursor = conn.cursor()
        sql = "SELECT * FROM test.diary WHERE diary_id = " + diary_id
        cursor.execute(sql)
        row_num = cursor.rowcount
    finally:
        cursor.close()
        if row_num > 0:
            row = cursor.fetchall()
            for row_data in row:
                post = (
                    {
                        'diary_id': row_data[0],
                        'diary_title': row_data[1],
                        'diary_body': row_data[2],
                        'diary_date': row_data[3]
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

def get_dbChange_post(ptitle,pbody,pno):
    conn = connection.connection()
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE test.post SET ptitle = '%s', pbody = '%s' WHERE pno= %d"%(ptitle,pbody,(int(pno))))
        conn.commit()
    finally:
        cursor.close()
        return "true"


def get_dbDelete_diary(diary_id):
    conn = connection.connection()
    try:
        cursor = conn.cursor()
        sql = "DELETE FROM test.diary WHERE diary_id =" + diary_id
        cursor.execute(sql)
        conn.commit()
    finally:
        cursor.close()
        return "true"

def get_centerSelect():
    conn = connection.connection()
    try:
        sql = "SELECT center_city,center_group,center_town,center_address,center_name,center_number FROM test.healthnew"
        cursor = conn.cursor()
        cursor.execute(sql)
        row_num = cursor.rowcount
    finally:
        cursor.close()
    if row_num > 0:
        object_list = []
        row = cursor.fetchall()
        object_list.append(row_num)
        for row_data in row:
            json_object = {"city": row_data[0], "group": row_data[1], "town": row_data[2], "address": row_data[3], "name": row_data[4], "number": row_data[5]}
            object_list.append(json_object)
        return object_list
    return "fail"


def get_dbSelect_password(email, name):
    conn = connection.connection()
    try:
        sql = "SELECT pw FROM test.os_member where email =" + "'" + email + "'" + "AND name = '" + name + "'"
        cursor = conn.cursor()
        cursor.execute(sql)
        row_num = cursor.rowcount
    finally:
        cursor.close()
    if row_num > 0:
        row = cursor.fetchall()
        for row_data in row :
            result = row_data[0]
        return result
    return "fail"

def get_dbInsert_comment(inputComment,loginId,pno):
    conn = connection.connection()
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO comment (cbody, userId, pno) VALUES ('%s',' %s', '%s');"
        val = (inputComment, loginId, int(pno))
        cursor.execute(sql,val)
        cursor.commit()
    finally:
        cursor.close()
        return "true"

    