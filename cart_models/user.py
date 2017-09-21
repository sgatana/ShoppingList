from flask_login import  UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from Exceptions import ShoppingListAlreadyExist, ShoppingListDoesNotExist

class User(UserMixin):
    def __init__(self, username,email,password):
        """hash password """
        self.password_hash = generate_password_hash(password)
        self.name=username
        self.id=email
        self.shopping_list = {}

    def __name__(self):
        return self.name

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def create_shopping_list(self, Shoppinglist):
       """a method that adds shopping list"""

       if Shoppinglist.name in self.shopping_list:
        raise ShoppingListAlreadyExist(Shoppinglist.name + "has been created")
        self.shopping_list.update({Shoppinglist.name: Shoppinglist})

    def delete_Shoppinglist(self, ShoppinglistName):
        """this method removes shopping list from user shopping lists"""
        try:
            self.shopping_list.pop(ShoppinglistName)
        except KeyError:
            raise ShoppingListDoesNotExist

    def get_shopping_list(self, ShoppinglistName):
        """this method returns a shopping  name"""
        try:
            self.shopping_list[ShoppinglistName]
        except KeyError:
            return self.shopping_list[ShoppinglistName]

    def update_shopping_list(self, shoppinglist):

        """method accept parameter and updates your shopping list"""
        self.delete_Shoppinglist(shoppinglist.name)
        self.delete_Shoppinglist(shoppinglist)

    def get_num_of_shopping_list(self):
        return  len(self.shopping_list)