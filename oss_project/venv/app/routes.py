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
  return render_template('contact.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/services')
def services():
  return render_template('services.html')
 
@app.route('/health_center')
def health_center():
  return render_template('health_center.html')
 
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

@app.route('/createAccount')
def createAccount_page():
  return render_template('createAccount.html')

@app.route('/register_route', methods=['GET', 'POST'])
def register_route(): 
  if request.method == "POST":
    reqname = request.form["name"]
    reqid = request.form["id"]
    reqpw = request.form["pw"]
    reqphone_num = request.form["phone_num"]
    
    content = mysql_dao.get_dbInsert_register(reqname,reqid,reqpw,reqphone_num)

  return content

if __name__ == '__main__':
  app.debug = True
  app.use_reloader=True
  app.secret_key = "123123123"
  app.run(host='0.0.0.0', port=80) 
  #port : 5000