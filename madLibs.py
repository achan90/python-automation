#! /usr/bin/env python3

import re
import os


def pathLocator(file):
    filePath = os.path.join(file)
    return filePath


def madLibs():
    regex = re.compile(r"(ADJECTIVE)|(VERB)|(NOUN)")
    file = open(pathLocator(input("Enter path name:  ")), "r")
    fileInput = file.read()
    match = regex.search(fileInput)

    while match is not None:
        if match.group(1) is not None:
            fileInput = regex.sub(
                input("Enter adjective:  "), fileInput, count=1)
            match = regex.search(fileInput)

        elif match.group(2) is not None:
            fileInput = regex.sub(
                input("Enter verb:  "), fileInput, count=1)
            match = regex.search(fileInput)

        elif match.group(3) is not None:
            fileInput = regex.sub(
                input("Enter noun:  "), fileInput, count=1)
            match = regex.search(fileInput)

        else:
            break

    print(fileInput)
    os.chdir(pathLocator(input("Enter directory name:  ")))
    newFile = open("madLibbed.txt", "w")
    newFile.write(fileInput)
    file.close()
    newFile.close()


madLibs()
