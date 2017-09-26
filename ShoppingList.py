from flask import Flask, render_template, url_for, flash
from flask_login import LoginManager, login_user, UserMixin, current_user, login_required, logout_user
from werkzeug.utils import redirect
from flask_bootstrap import Bootstrap
from Exceptions import ShoppingListAlreadyExist, ShoppingListAlreadyExist, UserDoesNotExist, UserAlreadyExist, ItemDoesNotExist, ItemAlreadyExist
from cart_models.user import User
from cart_models.User_Account import Accounts
from cart_models.Shopping_list import ShoppingList
from cart_models.item import Item
from forms import Register, Login


app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisismysecretkey'
bootstrap = Bootstrap(app)
accounts=Accounts()
login_manager=LoginManager()

login_manager.login_view = "/login"
login_manager.login_message_category="info"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(email):
    """load user using the given email"""
    return accounts.get_user(email)


@app.route('/',  methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return render_template("UserDashboard.html")
    else:
        return redirect(url_for("login"))

@app.route("/register")
def signup():
    form=Register()
    return render_template('SignUp.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form=Login()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    else:
        if form.validate_on_submit():
            user = accounts.get_user(form.email.data)
            if user:
                if user.verify_password(form.password.data):
                    login_user(user)
                    return redirect(url_for('index'))
                else:
                    flash("invalid username or password", 'danger')

            else:
                flash("user does not exist", 'danger')

        return render_template("Login.html", form=form)


@app.route('/dashboard')
def dashboard():
    return render_template('UserDashboard.html')

if __name__ == '__main__':
    app.debug=True
    app.run()
