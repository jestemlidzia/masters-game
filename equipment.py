import item

class Equipment(object):
    def __init__(self):
        self.item_list = []

    def add_item_to_equipment(self, item):
        self.item_list.append(item)
        print('The item {} has been put into the backpack'.format(item.name))

    def print_backpack(self):
        if len(self.item_list)!=0:
            print('Items in your backpack:')
            for lifted_item in self.item_list:
                print(lifted_item.name)
        else:
            print('Your backpack is empty')

    def check_item_in_backpack(self, item_name):
        # if item in self.item_list:
        for i in range(len(self.item_list)):
            if item_name == self.item_list[i].name:
                print('{} is in the backpack'.format(item_name))
                return True
        else:
            print('There is no {} in the backpack'.format(item_name))
            return False

    def close_backpack(self):
        print('TODO')

    def select_item(self):
        print('TODO')

    def remove_item(self):
        print('TODO')
    
    def update_equip(self):
        print("TODO")