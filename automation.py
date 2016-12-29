inventory = {"arrow": 12, "gold coin": 42, "rope": 1, "torch": 6, "dagger": 1}
loot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]


def displayInventory(items):
    total = 0
    print("Inventory:")

    for x, y in items.items():
        if y == 1:
            print(y, x)
            total += y

        elif y > 1 and x == "torch":
            print(y, "torches")
            total += y

        else:
            print(y, "{}s".format(x))
            total += y

    print("Total number of items: {}".format(total))


def addToInventory(inventory, loot):
    for x in loot:
        if x in inventory:
            inventory[x] += 1

        else:
            inventory.setdefault("{}".format(x), 1)

    displayInventory(inventory)


addToInventory(inventory, loot)
