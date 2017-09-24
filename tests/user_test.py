import unittest

from Exceptions import ShoppingListDoesNotExist, ShoppingListAlreadyExist
from cart_models.Shopping_list import ShoppingList
from cart_models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        """Create global User And ShoppingList for use throughout the class"""
        self.user = User("gatana", "test@gmail.com", "test@2017")
        self.shopping_list = ShoppingList("Naivas", "Shop with a difference")

        """Ensure user can create a shopping list"""
    def test_user_can_create_shopping_list(self):
        self.user.create_shopping_lst(self.shopping_list)
        self.assertEqual(1, len(self.user.shopping_lists))

        """Ensure user can delete a shopping list"""
    def test_user_can_delete_a_shopping_list(self):
        self.user.create_shopping_lst(self.shopping_list)
        self.assertEqual(1, len(self.user.shopping_lists))
        self.user.delete_shopping_list(self.shopping_list.name)
        self.assertEqual(0, len(self.user.shopping_lists))

    def test_user_delete_nonexisting_shopping_list(self):
        self.assertEqual(0, len(self.user.shopping_lists))
        with self.assertRaises(ShoppingListDoesNotExist):
            self.user.delete_shopping_list("List does not exist")

    def test_exception_raised_on_try_to_create_similar_shopping_lists(self):
        self.user.create_shopping_lst(self.shopping_list)
        self.user.create_shopping_lst(ShoppingList("naivas", "buy stuff"))
        with self.assertRaises(ShoppingListAlreadyExist):
            self.user.create_shopping_lst(ShoppingList("naivas", "Already existing"))

    def test_get_shopping_list_returns_if_item_found(self):
        self.user.create_shopping_lst(self.shopping_list)
        self.assertEqual(1, len(self.user.shopping_lists))
        self.assertEqual("Naivas", self.user.get_shopping_lst("Naivas").name)
        self.assertEqual(1, len(self.user.shopping_lists))

    def test_get_shoppinglist_raises_exception_if_shoppinglist_not_found(self):
        """tests if the get method in user returns the shoppingList Specified by
               key and raises (ShoppingListDoesNotExist)exception if not found
               """
        with self.assertRaises(ShoppingListDoesNotExist):
            self.user.get_shopping_lst(ShoppingList( "Naivas","Shopping List not found"))

if __name__ == '__main__':
    unittest.main()