from flask import*
from flask_mail import Mail, Message
import sqlite3
app=Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'subinv663@gmail.com'
app.config['MAIL_PASSWORD'] = 'subin1234'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True



mail = Mail(app)  # instantiate the mail class
'''
# configuration of mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'subinv663@gmail.com'
app.config['MAIL_PASSWORD'] = 'subin1234'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)'''


'''# message object mapped to a particular URL ‘/’
@app.route("/")
def index():
    msg = Message(
        'Hello',
        sender='yourId@gmail.com',
        recipients=['receiver’sid@gmail.com']
    )
    msg.body = 'Hello Flask message sent from Flask-Mail'
    mail.send(msg)
    return 'Sent'
'''

@app.route("/")
def aaa():
    return render_template("index.html")
@app.route("/blog-single")
def bbb():
    return render_template("blog-single.html")
@app.route("/send" , methods = ["POST"])
def ccc():
    if request.method== 'POST':
        name=request.form['n1']
        email=request.form['e1']
        msg=request.form['d1']
        c=sqlite3.connect("semail.db")
        cur=c.cursor()
        cur.execute("create table  if not exists t1(name text, email text, message text)")
        cur.execute("insert into t1 values(?,?,?)" , (name,email,msg))
        c.commit()
        msg1 = Message('MESSAGE FROM zodiac site', sender='subinv663@gmail.com', recipients=['subinv663@gmail.com'])
        mssg="hello ... /n                           message:     "+msg+"              from:      "+email
        msg1.body = mssg
        mail.send(msg1)
    return "success"

if __name__=="__main__":
    app.run(debug=True)
