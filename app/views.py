from app.cart_models.Shopping_list import ShoppingList
from app.cart_models.User_Account import Accounts
from app.cart_models.item import Item
from flask import Flask, render_template, url_for, flash, Markup
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from app.forms import Register, Login, CreateShoppingList, AddItem
from werkzeug.utils import redirect
from app.Exceptions import ShoppingListDoesNotExist, ShoppingListAlreadyExist, ItemDoesNotExist, ItemAlreadyExist
from app.cart_models.user import User
app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisismysecretkey'
bootstrap = Bootstrap(app)
accounts=Accounts()
login_manager=LoginManager()
login_manager.login_view = "/login"
login_manager.login_message_category = "info"
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


@app.route("/register", methods=['GET', 'POST'])
def signup():
    global accounts
    form=Register()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    else:
        if form.validate_on_submit():
            if accounts.get_user(form.email.data):
                # User Exist
                flash("User Already Exists", "warning")
            else:
                accounts.add_user(
                    User(form.username.data, form.email.data, form.password.data))
                flash("User Created Successfully", "info")
                return redirect("login")
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
                flash(Markup('user does not exist, Please <a href="/register">click here to register</a>'), 'danger')
        return render_template("Login.html", form=form)


@app.route('/dashboard')
def dashboard():
    return render_template('UserDashboard.html')


@app.route("/create_shoppinglist", methods=['GET', 'POST'])
@login_required
def create_shopping_lst():
    form = CreateShoppingList()
    if form.validate_on_submit():
        shopping_list = ShoppingList(form.name.data, form.body.data)

        try:
            current_user.create_shopping_lst(shopping_list)
        except ShoppingListAlreadyExist:
            flash("Shopping List " + form.name.data + " Already Exists", "warning")
            return render_template("create_shoppinglist.html",form=form)

        flash(form.name.data + " has been created, your app has "
              + str(len(current_user.shopping_lists)) + " Shopping Lists", "info")

        return redirect(url_for('index'))

    return render_template("create_shoppinglist.html", form=form)


@app.route("/add_item/<shopping_list_name>", methods=['GET', 'POST'])
@login_required
def add_item(shopping_list_name):
    form = AddItem()
    if form.validate_on_submit():
        """ 
        Instantiate an Item Object from the form data submitted by the current_user """
        item = Item(form.ItemName.data, form.price.data, form.quantity.data, form.CatName.data)
        try:
            shopping_list = current_user.get_shopping_lst(shopping_list_name)
            shopping_list.add_item(item)
            # current_user.update_shopping_list(shopping_list)
            flash(" " + item.name + " Successfully Added into Shopping List " + shopping_list_name, "info")

            return redirect(url_for('index'))

        except ItemAlreadyExist:
            flash(item.name + " Already Exists", "warning")
            return redirect(url_for('index'))
    else:
        return render_template("add_item.html", form=form, shopping_list_name=shopping_list_name)


@app.route("/update_item/<shopping_list_name>/<name>/<price>/<quantity>/<category>",  methods=['GET', 'POST'])
@login_required
def update_item(shopping_list_name, name, price, quantity, category):
    form = AddItem()
    """ 
    Item that you wish to update is created from parameters passed in the URL 
    """
    item_to_update = Item(name=name, price=price, category=category,
                          quantity=quantity)

    if form.validate_on_submit():
        item = Item(name=form.ItemName.data, price=form.price.data,
                    quantity=form.quantity.data,  category=form.CatName.data)

        try:
            shopping_list = current_user.get_shopping_lst(shopping_list_name)
            shopping_list.update_item(item=item, )
            flash(item.name + "Has been Successfully Updated", "success")
        except ShoppingListDoesNotExist:
            flash("No Shopping List With name " + shopping_list_name +
                  " Try Adding it instead", "warning")
        except ItemDoesNotExist:
            flash("Sorry Item " + item.name +
                  " Cannot Be Updated. Make sure you have such item first",
                  "warning")
        return redirect(url_for('index'))
    else:
        return render_template("update_item.html", form=form, shopping_list_name=shopping_list_name, item=item_to_update)


@app.route("/share_shoppinglist", methods=['GET', 'POST'])
@login_required
def share_shoppinglist():
    """
    This Endpoint Will sllow users to share their shopping lists with other users
    """
    flash("Bare with us, this module will be live soon!.", "info")
    return redirect(url_for('index'))


@app.route("/delete_shopping_list/<shopping_list_name>", methods=['GET', 'POST'])
@login_required
def delete_shopping_list(shopping_list_name):
        current_user.delete_shopping_list(shopping_list_name)
        flash(shopping_list_name + " Deleted Successfully ", "success")
        return redirect(url_for('index'))


@app.route("/delete_item/<shopping_list_name>/<name>/<price>/<quantity>/"
           "<category>", methods=['GET', 'POST'])
@login_required
def delete_item(shopping_list_name, name, price, quantity, category):
    """
    Deletes an item from a shopping_list. Creates a the item to delete from the
    url supplied parameters
    """
    item = Item(name=name, price=price, category=category, quantity=quantity)
    if current_user.is_authenticated:
        try:
            current_user.get_shopping_lst(shopping_list_name).remove_item(item)
            flash(item.name + " Deleted Successfully ", "success")
        except ShoppingListDoesNotExist:
            flash("Shopping List " + shopping_list_name + " Does Not Exist", "warning")
        except ItemDoesNotExist:
            flash("The Item " + item.name + "That You Wish To Delete Does Not Exist", "warning")

        return redirect(url_for('index'))


@app.route("/logout")
@login_required
def logout():
    """Logs Out A Currently LoggedIn User"""
    logout_user()
    flash("Thank you for using our App, Goodbye!", "success")
    return redirect(url_for("login"))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('Notfound.html'), 404


if __name__ == '__main__':
    app.debug=True
    app.run()
