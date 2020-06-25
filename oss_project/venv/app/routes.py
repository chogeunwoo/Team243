from flask import Flask, render_template, request, session, redirect, escape
import mysql_dao
from flask_mail import Mail, Message
import smtplib
 
app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "juyeone125@gmail.com" 
app.config['MAIL_PASSWORD'] = 'wndus481!!' 
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
mail = Mail(app)   

@app.route('/')
def main():
  if 'username' in session:
    result = '%s' % escape(session['username'])
    return render_template('main.html', loginId = result)

  else:
    session['username'] = ''
    result = '%s' % escape(session['username'])
    return redirect('/')

@app.route('/contact')
def contact():
  if 'username' in session:
    result = '%s' % escape(session['username'])
    return render_template('contact.html', loginId = result)

@app.route("/contact", methods=['post', 'get'])
def email_test():
   
    if request.method == 'POST':
        senders = request.form['name_sender']
        senders2 = request.form['email_sender']
        receiver = request.form['email_receiver']
        content = '보내는 사람:' + senders + '\n\n' + '답장 받을 이메일:' + senders2 + '\n\n' + '문의 내용:' + request.form['email_content']
        receiver = receiver.split(',')
       
        for i in range(len(receiver)):
            receiver[i] = receiver[i].strip()

        result = send_email(senders, receiver, content)
    return "Your mail has been sent successfully"
   
def send_email(senders, receiver, content):
    msg = Message('Stop Smoking 문의 메일', sender = senders, recipients = receiver)
    msg.body = content
    mail.send(msg)

@app.route('/about')
def about():
  if 'username' in session:
    result = '%s' % escape(session['username'])
    return render_template('about.html', loginId = result)

@app.route('/services')
def services():
  if 'username' in session:
    result = '%s' % escape(session['username'])
    return render_template('services.html', loginId = result)

@app.route('/freeBoard')
def freeBoard():
  if 'username' in session:
    result = '%s' % escape(session['username'])
    post = mysql_dao.get_dbSelect_post()
    print(post)
    return render_template('freeBoard.html', content=post, loginId=result)

@app.route('/more', methods=['POST'])
def more():
  if request.method == "POST":
    pno = request.form["pno"]
    post = mysql_dao.get_dbSelect_pno(pno)
    if 'username' in session:
      result = '%s' % escape(session['username'])
  print(result)
  return render_template('more.html', content=post, loginId = result)

@app.route('/changePost', methods=['POST'])
def changePost():
  if request.method == "POST":
    pno = request.form["pno"]
    post = mysql_dao.get_dbSelect_pno(pno)
    if 'username' in session:
      result = '%s' % escape(session['username'])
    else:
      session['username'] = ''
      result = '%s' % escape(session['username'])
    return redirect('/changePost')
  return render_template('changePost.html', content=post, loginId = result)

@app.route('/deletePost', methods=['POST'])
def deletePost():
  if request.method == "POST":
    pno = request.form["pno"]
    delete = mysql_dao.get_dbDelete_post(pno)
  return redirect('/freeBoard')


@app.route('/changePost_route', methods=['POST'])
def changePost_route():
  if request.method == "POST":
    pno = request.form["pno"]
    ptitle = request.form["ptitle"]
    pbody = request.form["pbody"]
    update = mysql_dao.get_dbChange_post(pno,ptitle,pbody)
  return update
    
@app.route('/createPost')
def createPost():
  if session['username'] == '':
    return redirect('/')
  else:
    result = '%s' % escape(session['username'])
    return render_template('createPost.html',loginId = result)

@app.route('/createPost_route', methods=['GET','POST'])
def createPost_route():
  if request.method == "POST":
    ptitle = request.form["ptitle"]
    pbody = request.form["pbody"]
    email = session["username"]
    content = mysql_dao.get_dbInsert_post(ptitle,pbody,email)
  return content
  
@app.route('/health_center')
def health_center():
  content = mysql_dao.get_centerSelect()

  if 'username' in session:
    result = '%s' % escape(session['username'])
    return render_template('health_center.html', loginId = result)

  else:
    session['username'] = ''
    result = '%s' % escape(session['username'])

  return redirect('/health_center')

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/login_route', methods=['GET', 'POST'])
def login_route():
  if request.method == "POST":
    reqid = request.form["id"]
    reqpw = request.form["pw"]
    content = mysql_dao.get_dbSelect_register(reqid, reqpw)
    
    if(content != 'fail'):
      result = content["email"]
      session['username'] = result
      return result
    else:
      result = "fail"
      return result

@app.route('/logout_route')
def logout_rout():
  session.pop('username',None)
  return redirect('/')

@app.route('/createAccount')
def createAccount_page():
  if 'username' in session:
    result = '%s' % escape(session['username'])
    return render_template('createAccount.html', loginId = result)

  else:
    session['username'] = ''
    result = '%s' % escape(session['username'])

  return redirect('/createAccount')

@app.route('/register_route', methods=['GET', 'POST'])
def register_route(): 
  if request.method == "POST":
    reqname = request.form["name"]
    reqid = request.form["id"]
    reqpw = request.form["pw"]
    reqphone_num = request.form["phone_num"]
    content = mysql_dao.get_dbInsert_register(reqname,reqid,reqpw,reqphone_num)

  return content
@app.route('/myinfo')
def myinfo():
  return render_template('myinfo.html')

@app.route('/changeMyinfo')
def changeMyinfo():
  return render_template('changeMyinfo.html')

@app.route('/diary')
def diary():
  content = mysql_dao.get_dbSelect_diary()
  return render_template('diary.html',trade = content)

@app.route('/new_diary')
def new_diary():  
    return render_template('new_diary.html')


@app.route('/diary_route', methods=['GET', 'POST'])
def diary_route():
  if request.method == "POST":
    title = request.form["title"]
    body = request.form["body"]
    date = request.form["date"]
    content = mysql_dao.get_dbInsert_diary(title, body, date)
    return content
    
@app.route('/diary_more',methods =['GET','POST'])
def diary_more():
  if request.method == "POST":
    diary_id = request.form["id"]
    content = mysql_dao.get_dbMore_diary(diary_id)
    return render_template('diary_more.html', trade = content)

@app.route('/diary_update_route', methods = ['GET','POST'])
def diary_update_route():
  if request.method == "POST":
    diary_id = request.form["id"]
    content = mysql_dao.get_dbMore_diary(diary_id)
    return render_template('diary_update.html',trade = content)

@app.route('/diary_update_view', methods = ['GET','POST'])
def diary_update_view():
  if request.method == "POST":
    diary_id = request.form["id"]
    title = request.form["title"]
    body = request.form["body"]
    date = request.form["date"]
    mysql_dao.get_dbUpdate_diary(diary_id, title, body, date)
    return redirect("diary")

@app.route('/diary_delete',methods = ['GET','POST'])
def diary_delete():
  if request.method == "POST":
    diary_id = request.form["id"]
    content = mysql_dao.get_dbDelete_diary(diary_id)
    return redirect("diary")


@app.route('/forgot_password_page')
def forgot_password_page():
  if 'username' in session:
    result = '%s' % escape(session['username'])
    return render_template('password.html', loginId = result)

  else:
    session['username'] = ''
    result = '%s' % escape(session['username'])

  return redirect('/forgot_password_page')

  
@app.route("/password_route", methods=['GET', 'POST'])
def password_route():
  if request.method == "POST":
    reqid = request.form["id"]
    reqname = request.form["name"]

    content = mysql_dao.get_dbSelect_password(reqid,reqname)
  return content

if __name__ == '__main__':
  app.debug = True
  app.use_reloader=True
  app.secret_key = "123123123"
  app.run(host='0.0.0.0', port=80) 
  #port : 5000