#! /usr/bin/env python3

import pyperclip
import re

text = pyperclip.paste()
regexMail = re.compile(r"""
    ( [a-zA-Z.-_+%0-9]+ )      # username
    ( @ )                      # @ symbol
    ( [a-zA-Z0-9.-]+ )         # domain
    ( \. \w{2,4} )             # domain extension
    """, re.VERBOSE)
regexPhone = re.compile(r"""
    ( \d{3} | \( \d{3} \) ) ?                # area code
    ( [-\s.] ) ?                             # separator
    ( \d{3} )                                # first numbers
    ( [-\s.] )                               # separator
    ( \d{4} )                                # last numbers
    ( \s* (ext | x | ext.) \s* (\d{2,5}) ) ? # extension
    """, re.VERBOSE)


def finder(text, emails, numbers):
    matches = [[], []]
    substitute = re.compile(r"\.+")

    for x in emails.findall(text):
        if emails.findall(text) is None:
            print("No emails found.")

        else:
            matches[0].append("".join(x))

    for x in numbers.findall(text):
        if numbers.findall(text) is None:
            print("No phone numbers found.")

        else:
            matches[1].append("".join(x))

    if matches is None:
        print("Search complete,no matches found.")

    else:
        formattedMatches = []

        for x in matches[0]:
            formattedMatches.append(x)

        for x in range(len(matches[1])):
            matches[1][x] = substitute.sub("-", matches[1][x])
            formattedMatches.append(matches[1][x])

        print("\n".join(formattedMatches))
        pyperclip.copy("\n".join(formattedMatches))
        print("Search complete, matches copied to clipboard.")


finder(text, regexMail, regexPhone)
