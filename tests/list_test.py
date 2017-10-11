import unittest

from app.cart_models.item import Item

from app.Exceptions import ItemAlreadyExist, ItemDoesNotExist
from app.cart_models.Shopping_list import ShoppingList


class TestShoppingList (unittest.TestCase):
    def setUp(self):
        self.list = ShoppingList('Breakfast', 'start your day with smile')
        self.morning = Item("bread", 50, 1, "Breko")
        self.midmorning = Item("rice", "150", "1", "Breko")
        self.lunch = Item("beef", "250", "1", "light")

    def test_add_shoppinglist_item(self):
        self.assertEqual(0, len(self.list.categories))
        self.list.add_item(self.morning)
        self.list.add_item(self.midmorning)
        # lis of categories should remain 1
        self.assertEqual(1, len(self.list.categories))
        # list of items in the category breko should be 2
        self.assertEqual(2, len(self.list.categories[self.morning.category]))


    def test_remove_shoppinglist_item(self):
        self.list.add_item(self.morning)
        self.list.add_item(self.lunch)
        self.assertEqual(2, len(self.list.categories))
        self.list.remove_item(self.morning)
        self.assertEqual(1, len(self.list.categories))

    def test_category_remove_is_empty(self):
        self.list.add_item(self.lunch)
        self.assertEqual(1, len(self.list.categories))
        self.list.remove_item(self.lunch)
        self.assertEqual(0, len(self.list.categories))

    def test_remove_nonexisting_shoppinglist_item(self):
        item = Item('Supper', 400, 2, "Delicious")
        with self.assertRaises(ItemDoesNotExist):
            self.list.remove_item(item)

    def test_add_existing_shopping_list_item(self):
        self.list.add_item(self.morning)
        with self.assertRaises(ItemAlreadyExist):
            self.list.add_item(self.morning)

    def test_update_shoppinglist_item(self):
        self.list.add_item(self.morning)
        new_item = Item("bread",200, 1, "Breko" )
        self.list.update_item(new_item)
        self.assertEqual(new_item.price, self.list.get_item(self.morning).price)

    def test_adding_existing_item_in_the_same_category_raises_exception(self):
        self.list.add_item(self.morning)
        self.list.add_item(self.midmorning)
        with self.assertRaises(ItemAlreadyExist):
            self.list.add_item(self.midmorning)

    def test_updating_non_existing_item_raises_exception(self):
        with self.assertRaises(ItemDoesNotExist):
            self.list.update_item(self.morning)