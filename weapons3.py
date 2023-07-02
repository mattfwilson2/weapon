import itertools
import random
from class_info import *

CHAR_CLASS = str()
CHAR_LEVEL = 1
INVENTORY = []
CLASSES = ['Barbarian', 'Sorcerer', 'Rogue', 'Necromancer', 'Druid']
RARITY = ['Common', 'Magic', 'Rare', 'Legendary', 'Unique']

class Item:
    id_iter = itertools.count(1)
    def __init__(self):
        self.id = next(Item.id_iter)
        self.type_equipment = True
        self.type_consumable = False
        self.type_quest = False

class Weapon(Item):
    def __init__(self, rarity: str, adj: dict, weapon: list):
        super().__init__()
        self._rarity = rarity
        self._level = 5
        self._weap_adj = ''.join(random.choices(adj.get(self._rarity)))
        self._weap_type = ''.join(random.choices(weapon))
        self._drop = self._weap_adj + ' ' + self._weap_type
        self._show_rarity = '[' + self._drop + '] ' + self._drop
        INVENTORY.append(self._drop)

    def __repr__(self):
        return self._adj, self._weap_type

    def get_id(self):
        return self.id

    def check_rarity(self):
        if self._rarity == 'Legendary' or self._rarity == 'Unique':
            self._rarity = self._rarity.upper()

    def show_drop(self):
        print(f'[{self._rarity}] {self._drop}')

    def show_details(self):
        print(f'Equipment: {self.type_equipment}\nConsumable: {self.type_consumable}\nQuest item: {self.type_quest}')

if __name__ == "__main__":
    while True:
        roll_input = input('Roll item? ')
        if roll_input in 'y':
            rarity_roll = ''.join(random.choices(RARITY, weights=[10, 7, 4, 2, 1]))
            item = Weapon(rarity_roll, sor_adj, sor_weap)
            item.check_rarity()
            item.show_drop()
            item.show_details()
        elif roll_input == 'inv':
            print(f'Inventory: {INVENTORY}')
        else:
            print(f'Exiting...')
            break

