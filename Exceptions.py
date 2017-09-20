class ItemDoesNotExist(Exception):
    """If an Item Does Not Exist This Exception is thrown"""
    pass


class ItemAlreadyExist(Exception):
    """If an Item Does Exist This Exception is thrown"""
    pass


class UserAlreadyExist(Exception):
    """If a User Does Exist This Exception is thrown"""
    pass


class UserDoesNotExist(Exception):
    """If a User Does Not Exist This Exception is thrown"""
    pass


class ShoppingListDoesNotExist(Exception):
    """Raised If A non-existing ShoppingList removed from the shopping List
    """
    pass


class ShoppingListAlreadyExist(Exception):
    """Raised on Attempt to add an existing shopping list """
    pass