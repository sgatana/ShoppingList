from app.Exceptions import ItemDoesNotExist, ItemAlreadyExist

#This Class Manages Items In a User Shopping List
class ShoppingList:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.categories = {}

    def add_item(self, item):
        try:
            self.get_item(item)
            raise ItemAlreadyExist()
        except KeyError:
            #get the category
            cat_dict = self.categories.get(item.category, {})
            #add the item to that category, if the its a new category, both item and category are added
            cat_dict.update({item.name: item})

            self.categories.update({item.category: cat_dict})

    def remove_item(self, item):
        try:
            #a category can be deleted if it doesnt have an item
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