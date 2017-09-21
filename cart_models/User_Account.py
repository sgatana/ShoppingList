from Exceptions import UserAlreadyExist, UserDoesNotExist


class Accounts(object):
    """ Creates an Account where users can be stored"""

    def __init__(self):
        self.users = {}

    def add_user(self, user):
        """ This Method Creates a User and is added into dictionary of users """
        if user.id in self.users:
            raise UserAlreadyExist
        else:
            self.users.update({user.id: user})

    def remove_user(self, email):
        """ This Method removes a user from users dictionary using the email"""
        try:
            self.users.pop(email)
        except KeyError:
            raise UserDoesNotExist

    def check_user(self, email):
        if email in self.users:
            return self.users[email]

    def all_users(self):
        return self.users