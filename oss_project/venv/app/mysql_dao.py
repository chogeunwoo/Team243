import pymysql
import connection
import json
import datetime

def get_dbSelect_stop2(email):
    conn = connection.connection()
    try:
        cursor = conn.cursor()
        sql = "SELECT * FROM test.stop_smoke where email=" + "'" + email + "'"
        cursor.execute(sql)
        row_num = cursor.rowcount
    finally:
        cursor.close()
        post=[]
        if row_num > 0:
            row = cursor.fetchall()
            now = datetime.datetime.now().date()
            for row_data in row :
                post.append(
                    {
                        "email": row_data[0],
                        "smoke_amount": row_data[1],
                        "smoke_date": row_data[2],
                        "smoke_now_date": now,
                        "smoke_reason": row_data[3]
                    }
                )
            result_date = post[0]['smoke_now_date'] - post[0]['smoke_date']

            post.append(result_date.days)
            return post
        else:
            return "fail"

def get_dbSelect_stop(email):
    conn = connection.connection()
    try:
        cursor = conn.cursor()
        sql = "SELECT * FROM test.stop_smoke where email=" + "'" + email + "'"
        cursor.execute(sql)
        row_num = cursor.rowcount
    finally:
        cursor.close()
        if row_num > 0:
            return "fail"
        else:
            return "true"

def get_dbInsert_stop(email, smoke_amount, smoke_date, smoke_reason):
    conn = connection.connection()
    try:
        sql = "SELECT email FROM test.stop_smoke where email =" + "'" + email + "'"
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
            sql = "INSERT INTO stop_smoke (email, smoke_amount, smoke_date, smoke_reason) VALUES (%s, %s, %s, %s);"
            val = (email, smoke_amount, smoke_date, smoke_reason)
            cursor.execute(sql,val)
            conn.commit()
        finally:
            cursor.close()
            createInfo = 1
            return createInfo

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
                    "email": row_data[1],
                    "pw": row_data[2],
                    "phone_num": row_data[3]
                }
            return json_object
        else:
            return "fail"

def get_dbSelect_id(id):
    conn = connection.connection()
    try:
        cursor = conn.cursor()
        sql = "SELECT * FROM test.post where email=" + "'" + id + "'"
        cursor.execute(sql)
        row_num = cursor.rowcount
        
    finally:
        cursor.close()
        if row_num > 0:
            row = cursor.fetchall()
            for row_data in row :
                json_object = {
                    "email": row_data[0],
                    "name": row_data[1],
                    "pw": row_data[2],
                    "phone_num": row_data[3]
                }
            return json_object
        else:
            return "fail"

def get_dbChange_changeMyinfo(email, name, pw, phone_num):
    print(email, name, pw, phone_num,"디비 시작")
    conn = connection.connection()
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE test.os_member SET name = '%s', pw = '%s', phone_num = '%s' WHERE email= '%s'"%(name, pw, phone_num, email))
        conn.commit()
    finally:
        cursor.close()
        cursor = conn.cursor()
        sql = "SELECT name, email, pw, phone_num FROM test.os_member where email=" + "'" + email + "'"
        cursor.execute(sql)
        row_num = cursor.rowcount
        
        cursor.close()
        if row_num > 0:
            row = cursor.fetchall()
            for row_data in row :
                json_object = {
                    "name": row_data[0],
                    "email": row_data[1],
                    "pw": row_data[2],
                    "phone_num": row_data[3]
                }
            print(json_object,"디비 끝")
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
        post=[]
        post.append(row_num)
        if row_num > 0:
            row = cursor.fetchall()
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
            return post

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

def get_dbInsert_diary(diary_title, diary_body, diary_date,result):
    conn = connection.connection()
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO diary (diary_title, diary_body, diary_date,diary_login_id) VALUES (%s, %s, %s,%s);"
        val = (diary_title, diary_body, diary_date,result)
        cursor.execute(sql,val)
        conn.commit()
    finally:
        cursor.close()
        return "true"

def get_dbSelect_diary(result):
    conn = connection.connection()
    try:
        cursor = conn.cursor()
        sql = "SELECT diary_id, diary_title, diary_body, diary_date FROM test.diary WHERE diary_login_id = '" + result + "'"
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

def get_dbUpdate_diary(diary_title, diary_body, diary_date, diary_id):
    conn = connection.connection()
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE test.diary SET diary_title = '%s', diary_body = '%s', diary_date = '%s' WHERE diary_id = %d"%(diary_title, diary_body, diary_date, (int(diary_id))))
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
                    'row_num' : row_num,
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

def get_dbInsert_comment(cbody,userId,pno):
    conn = connection.connection()
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO comment (cbody, userId, pno) VALUES (%s, %s, %s);"
        val = (cbody, userId, pno)
        cursor.execute(sql,val)
        conn.commit()
    finally:
        cursor.close()
        return "true"

def get_dbSelect_comment_list(pno):
    conn = connection.connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM test.comment WHERE pno = %d"%int(pno))
        conn.commit()
        row_num = cursor.rowcount
    finally:
        cursor.close()
        if row_num > 0:
            row = cursor.fetchall()
            comment_list=[]
            comment_list.append(row_num)
            for row_data in row:
                comment_list.append(
                    {
                        'cno': row_data[0],
                        'cbody': row_data[1],
                        'userId': row_data[2],
                        'pno': row_data[3]
                    }
                )
            return comment_list 
        else:
            comment_list=[]
            comment_list.append(0)
            return comment_list


def get_dbSelect_comment(cno):
    conn = connection.connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM test.comment WHERE cno = %d"%int(cno))
        

        conn.commit()
        row_num = cursor.rowcount
    finally:
        cursor.close()
        if row_num > 0:
            row = cursor.fetchall()
            for row_data in row :
                json_object = {
                    'cno': row_data[0],
                    "cbody": row_data[1],
                    "userId": row_data[2],
                    "pno": row_data[3]
                }
            return json_object
        else:
            return "fail"

def get_dbChange_comment(cbody,cno):
    conn = connection.connection()
    try:
        print(cbody,cno)
        cursor = conn.cursor()
        cursor.execute("UPDATE test.comment SET cbody = '%s' WHERE cno= %d"%(cbody,(int(cno))))
        conn.commit()
    finally:
        cursor.close()
        return "true"

def get_dbDelete_comment(cno):
    conn = connection.connection()
    try:
        cursor = conn.cursor()
        sql = "DELETE FROM test.comment WHERE cno =" + cno
        cursor.execute(sql)
        conn.commit()
    finally:
        cursor.close()
        return "true"