from inventory import *

loot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]


def addToInventory(inventory, loot):
    for x in loot:
        if x in inventory:
            inventory[x] += 1

        else:
            inventory.setdefault("{}".format(x), 1)

    displayInventory(inventory)


addToInventory(inventory, loot)
