#! /usr/bin/env python3
# Adds bullet points to beginning of each new line of text on clipboard

import pyperclip

text = pyperclip.paste()


def separator(clipboard):
    lines = clipboard.split("\n")

    for line in range(len(lines)):
        lines[line] = "* {}".format(lines[line])
    return "\n".join(lines)


# Copies the finished bullet point list to clipboard
pyperclip.copy(separator(text))
print("Bullet list created:")
print(pyperclip.paste())
