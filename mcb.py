#! /usr/bin/env python3

# mcb.py - Saves and loads pieces of text to the clipboard.
#   Usage:
#   ./mcb.py save <keyword> - Saves clipboard to keyword.
#   ./mcb.py <keyword> - Loads data from keyword to clipboard.
#   ./mcb.py list - Loads all keywords to clipboard.

import shelve
import pyperclip
import sys

mcbShelf = shelve.open("mcb")

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    mcbShelf[sys.argv[2]] = pyperclip.paste()

# List keywords and load content.
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcbShelf.keys())))

    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])


mcbShelf.close()
