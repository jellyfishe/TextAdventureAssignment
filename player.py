from game_data import Item
class Player:

    def __init__(self, x, y):
        '''
        Creates a new Player.
        :param x: x-coordinate of position on map
        :param y: y-coordinate of position on map
        :return:

        This is a suggested starter class for Player.
        You may add new parameters / attributes / methods to this class as you see fit.
        Consider every method in this Player class as a "suggested method":
                -- Suggested Method (You may remove/modify/rename these as you like) --
        '''
        self.x = x
        self.y = y
        self.inventory = [Item("TCard", 2, 5, 10),Item("CCard", 2, 5, 10),Item("BCard", 2, 5, 10)]
        self.victory = False

    def move(self, dx, dy):
        '''
        Given integers dx and dy, move player to new location (self.x + dx, self.y + dy)
        :param dx:
        :param dy:
        :return:
        '''
        self.x += dx
        self.y += dy

    def move_north(self):
        '''These integer directions are based on how the map must be stored
        in our nested list World.map'''
        self.move(0,-1)

    def move_south(self):
        self.move(0,1)

    def move_east(self):
        self.move(1,0)

    def move_west(self):
        self.move(-1,0)

    def add_item(self, item):
        '''
        Add item to inventory.
        :param item:
        :return:
        '''

    def remove_item(self, item):
        '''
        Remove item from inventory.
        :param item:
        :return:
        '''

    def get_inventory(self):
        '''
        Return inventory.
        :return:
        '''
    def get_item(self, name):
        for item in self.inventory:
            if item.get_name() == name:
                return item
        return None
