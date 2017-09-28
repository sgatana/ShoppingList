from Exceptions import UserAlreadyExist, UserDoesNotExist


class Accounts:
    """ Creates an Account where users can be stored"""

    def __init__(self):
        self.users = {}

    def add_user(self, user):
        """ Create User and add to the dictionary """
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

    def get_user(self, email):
        if email in self.users:
            return self.users[email]

