#! /usr/bin/env python3

import pprint

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(table):
    width = []

    for x in range(len(table)):
        for y in range(len(table[x])):
            width.append(len(table[x][y]))

    for x in range(len(table)):
        for y in range(len(table[x])):
            table[x][y] = str(table[x][y]).rjust(max(width))

    for x in range(len(table[0])):
        printer(table, x)


def printer(table, listLength):
    columns = []
    for x in range(len(table)):
        columns.append((table[x][listLength]))

    print("".join(columns))


printTable(tableData)
