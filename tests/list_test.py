import unittest
from cart_models.item import Item
from cart_models.Shopping_list import ShoppingList
from Exceptions import ItemAlreadyExist, ItemDoesNotExist

class TestShoppingList (unittest.TestCase):
    def setUp(self):
        self.list = ShoppingList('Breakfast', 'start your day with smile')
        self.morning = Item("bread", "50", "1", "Breko")
        #self.lunch = Item("rice", "150", "1", "heavy")
        #self.supper = Item("beef", "250", "1", "light")

    def test_add_shoppinglist_item(self):
        self.list.add_item(self.morning)
        self.assertEqual(1, len(self.list.categories))

    def test_remove_shoppinglist_item(self):
        self.list.add_item(self.morning)
        self.list.remove_item(self.morning)
        self.assertEqual(0, len(self.list.categories))

    def test_remove_nonexisting_shoppinglist_item(self):
        with self.assertRaises(ItemDoesNotExist):
            self.list.remove_item(self.morning)

    def test_add_existing_shopping_list_item(self):
        self.list.add_item(self.morning)
        with self.assertRaises(ItemAlreadyExist):
            self.list.add_item(self.morning)