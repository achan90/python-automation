allGuests = {"Alice": {"apples": 5, "pretzels": 12},
             "Bob": {"ham sandwiches": 3, "apples": 2},
             "Carol": {"cups": 3, "apple pies": 1}}


def totalBrought(quests, item):
    numBrought = 0

    for k, v in quests.items():
        numBrought = numBrought + v.get(item, 0)

    return numBrought


print("Number of things being brought:")
print("- Apples         {}".format(totalBrought(allGuests, "apples")))
print("- Cups           {}".format(totalBrought(allGuests, "cups")))
print("- Cakes          {}".format(totalBrought(allGuests, "cakes")))
print("- Ham Sandwiches {}".format(totalBrought(allGuests, "ham sandwiches")))
print("- Apple Pies     {}".format(totalBrought(allGuests, "apple pies")))
