from flask import Flask,request,render_template
import pickle

app = Flask(__name__)


@app.route('/')
def hello_world():
	return render_template("login.html")

database={'nachi':'123','james':'aac','karthik':'asdsf'}

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    x = name1.capitalize()
    if name1 == x:
         if pwd.isalnum():
              return render_template('home.html', name=name1)
         else:
              return render_template('login.html', info='Invalid info')
    else:
         return render_template('login.html', info='Invalid info')

         
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8081)