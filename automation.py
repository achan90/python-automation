allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}


def totalBrought(quests, items):
    itemTotal = 0

    for k, v in quests.item():
        itemTotal += v.get(items, 0)
    return itemTotal
