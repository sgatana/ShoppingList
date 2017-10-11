class Item:
    """define your class item"""
    def __init__(self, name, price, quantity, category=None):
        self.name = name
        self.price = price
        self.quantity = quantity
        """check if you category is empty and initialize it to general"""
        if category is None:
            self.category = "General"
        else:
            self.category = category

    def __eq__(self, item):
        if self.name is item.name and self.price is item.price and \
                        self.quantity is item.quantity and \
                        self.category is item.category:
            return True
        else:
            return False

    def __ne__(self, item):
        return not self.__eq__(item)