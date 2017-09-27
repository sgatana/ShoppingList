from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from Exceptions import ShoppingListAlreadyExist, ShoppingListDoesNotExist


class User(UserMixin):
    def __init__(self, username, email, password):
        """hash password """
        self.password_hash = generate_password_hash(password)
        self.name = username
        self.id = email
        self.shopping_lists = {}

    def __name__(self):
        return self.name

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def create_shopping_lst(self, Shoppinglist):

        """a method that adds shopping list"""
        if Shoppinglist.name in self.shopping_lists:
            raise ShoppingListAlreadyExist
        self.shopping_lists.update({Shoppinglist.name: Shoppinglist})

    def delete_shopping_list(self, ShoppinglistName):
        """this method removes shopping list from user shopping lists"""
        try:
            self.shopping_lists.pop(ShoppinglistName)
        except KeyError:
            raise ShoppingListDoesNotExist

    def get_shopping_lst(self, ShoppinglistName):
        """this method returns a shopping  name"""
        try:
            self.shopping_lists[ShoppinglistName]
        except KeyError:
            raise ShoppingListDoesNotExist
        return self.shopping_lists[ShoppinglistName]

    def update_shopping_list(self, shoppinglist):

        """method accept parameter and updates your shopping list"""
        self.delete_shopping_list(shoppinglist.name)
        self.create_shopping_lst(shoppinglist)

    def get_num_of_shopping_lists(self):
        return len(self.shopping_lists)
