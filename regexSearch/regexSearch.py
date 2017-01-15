#! /usr/bin/env python3
# Searches through all text files on cwd for user supplied regex.

import re
import os


def regexSearch():
    regex = re.compile(input("Enter regex pattern:  "))
    fileList = os.listdir(os.getcwd())

    for file in fileList:
        open(file, "r")
        matches = regex.findall(file.read())

        print("Searching {}".format(file))

        if matches is not None:
            for match in matches:
                print("Match found: {}".format("".join(match)))

        else:
            print("No matches found on {}".format(file))


regexSearch()
