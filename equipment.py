import item

class Equipment(object):
    def __init__(self):
        self.item_list = []

    def add_item_to_equipment(self, item):
        self.item_list.append(item)