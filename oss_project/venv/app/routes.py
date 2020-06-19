from flask import Flask, render_template, request, session, redirect, escape
import mysql_dao
 
app = Flask(__name__)


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
  if 'username' in session:
    result = '%s' % escape(session['username'])
    return render_template('health_center.html', loginId = result)

 
@app.route('/login')
def login():
  if 'username' in session:
    result = '%s' % escape(session['username'])
    return render_template('login.html', loginId = result)


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
  return render_template('diary.html', trades = mysql_dao.get_dbSelect_diary())

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

@app.route('/diary_update_route', methods=['GET', 'POST'])
def diary_update_route():
  if request.method == "POST":
    title = request.form["title"]
    body = request.form["body"]
    date = request.form["date"]

  content = mysql_dao.get_dbUpdate_diary(title, body, date)
  return content

if __name__ == '__main__':
  app.debug = True
  app.use_reloader=True
  app.secret_key = "123123123"
  app.run(host='0.0.0.0', port=80) 
  #port : 5000