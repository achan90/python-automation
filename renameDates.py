#! /usr/bin/env python3

# renameDates.py - Renames filenames with American MM-DD-YYYY date format
#                  to European DD-MM-YYY

import shutil
import os
import re


def renameDates(mode):
    # Regex to match files with american date format
    dateRegex = re.compile(r"""
        ^(.*?)-                     # all text before the date
        ( (0|1)? \d )-              # one or two digits for the month
        ( (0|1|2|3)? \d )           # one or two digits for the day
        ( 20\d\d )                  # four digits for the year
        (.*?)$                      # all text after the date

        """, re.VERBOSE)

    # Loop over files in working directory
    for amerFilename in os.listdir("."):
        mo = dateRegex.search(amerFilename)

        # Kkip files without date
        if mo is None:
            continue

        # Get parts of the filename
        before = mo.group(1)
        month = mo.group(2)
        day = mo.group(4)
        year = mo.group(6)
        after = mo.group(7)

        # Form the european style filename
        euroFilename = ("{}{}-{}-{}{}".format(before, month, day, year, after))
        # Get full absolute filepaths
        absWorkingDir = os.path.abspath(".")
        amerFilename = os.path.join(absWorkingDir, amerFilename)
        euroFilename = os.path.join(absWorkingDir, euroFilename)

        # Rename the files
        print("Renaming '{}' to '{}'".format(amerFilename, euroFilename))
        confirmation = input("\nDo you want to continue? [Y/N]:  ")

        if confirmation.lower() == "y":
            print("File renamed")
            shutil.move(amerFilename, euroFilename)

        elif confirmation.lower() == "n":
            print("File skipped".format(amerFilename))
            continue
