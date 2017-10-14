import unittest

from app.views import app


class Testingviewroutes(unittest.TestCase):
    def setUp(self):
        # create a test client
        self.app = app.test_client()
        self.app.testing = True

    # define paths
    def get_result(self, path):
        """ sends get request to the defined path """
        return self.app.get(path)

    def test_app_root_status(self):
        result = self.get_result('/')
        # the user is redirected to login page if not authenticated
        self.assertEqual(result.status_code, 302)

    def test_status_code_for_register(self):
        # Test If a non Logged in User can access the signup page
        self.assertEqual(200, self.get_result("/register").status_code)

    def test_status_code_for_login(self):
        result = self.get_result('/login')
        self.assertEqual(result.status_code, 200)

    def test_unlogged_in_user_can_not_access_the_logout(self):
        # Test If a User Will be redirected to the login page on trying to access the logout page
        self.assertEqual(302, self.get_result("/logout").status_code)

    def test_access_to_un_available_endpoint(self):
        self.assertEquals(404, self.get_result("/Shopping_list").status_code)

    def test_anonymous_user_is_always_redirected_to_login(self):
        self.assertEquals(302, self.get_result("/create_shoppinglist").status_code)
