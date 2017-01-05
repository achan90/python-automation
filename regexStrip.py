#! /usr/bin/env python3

import re


def stripRegex(*arg):
    arguments = []
    regexSpace = re.compile(r"^(\s+)|$(\s+)")

    for x in arg:
        arguments.append(x)

    if len(arguments) == 1:
        sentence = regexSpace.sub("", arguments[0])
        print(sentence)

    elif len(arguments) == 2:
        regexSpace = re.compile(r"[{}]".format(arguments[1]))
        sentence = regexSpace.sub("", arguments[0])
        print(sentence)

    else:
        exit("Too many arguments")


a = "  jEEEsus    "
b = "su"
stripRegex(a, b)
stripRegex(a)
