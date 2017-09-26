import unittest
from Exceptions import UserAlreadyExist, UserDoesNotExist
from cart_models.User_Account import Accounts
from cart_models.user import User


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Accounts()
        self.user = User("steve", "steve@gmail.com", "steve2017")

    def test_create_user(self):
        self.account.add_user(self.user)
        self.assertEqual(1, len(self.account.users))

    def test_exception_raised_on_existing_user(self):
        self.account.add_user(self.user)
        with self.assertRaises(UserAlreadyExist):
            self.account.add_user(self.user)

    def test_remove_user(self):
        self.account.add_user(self.user)
        self.assertEqual(1, len(self.account.users))
        self.account.remove_user("steve@gmail.com")
        self.assertEqual(0, len(self.account.users))

    def test_removing_a_non_user_raises_exception(self):
        with self.assertRaises(UserDoesNotExist):
            self.account.remove_user("andela@gmail.com")


if __name__ == '__main__':
    unittest.main()
