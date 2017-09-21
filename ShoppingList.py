from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from forms import Register, Login

app = Flask(__name__)
app.config['SECRET_KEY']='thisismysecretkey'
Bootstrap(app)
@app.route('/')
def signup():
    form=Register()
    #Authentcate User
   # if user.is_authenticated:
    return render_template('SignUp.html', form=form)

@app.route('/login')
def login():
    form=Login()
    return render_template('Login.html', form=form)

@app.route('/dashboard')
def dashboard():
    return render_template('UserDashboard.html')

if __name__ == '__main__':
    app.debug=True
    app.run()
