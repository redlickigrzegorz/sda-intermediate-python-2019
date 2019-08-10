class ItemValueNotPositive(Exception):
    def __init__(self):
        self.message = "Item's value equals zero!"
