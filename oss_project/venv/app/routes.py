from flask import Flask, render_template, request
import mysql_dao
 
app = Flask(__name__)

@app.route('/')
def main():
  return render_template('main.html')

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
  app.run(host='0.0.0.0', port=80) 
  #port : 5000