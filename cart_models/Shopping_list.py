from Exceptions import ItemDoesNotExist, ItemAlreadyExist


class ShoppingList:
    def __init__(self, name, description):
        """ This Class Manages Items In a User Shopping List"""
        self.name = name
        self.description = description
        self.categories = {}

    def add_item(self, item):
        """If Item is already added Raise an exception"""
        try:
            self.get_item(item)
            raise ItemAlreadyExist("Item already Added")
        except KeyError:
            cat_dict = self.categories.get(item.category, {})
            # First Update The inner Dictionary
            cat_dict.update({item.name: item})
            self.categories.update({item.category: cat_dict})

    def remove_item(self, item):
        try:
            """a category can be deleted if it contains on item  """
            if len(self.categories[item.category]) == 1:
                del (self.categories[item.category])
            else:
                self.categories[item.category].pop(item.name)
        except KeyError:
            raise ItemDoesNotExist

    def update_item(self, item):
        self.remove_item(item)
        self.add_item(item)

    def get_item(self, item):
        """Returns an item object """
        return self.categories[item.category][item.name]

    def get_categories(self):
        return len(self.categories)