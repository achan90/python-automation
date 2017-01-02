#! /usr/bin/env python3

import re


def isPhoneNumber(message):
    regex = re.compile(r"(\d{3}-)?(\d{3}-\d{4})")
    match = regex.findall(message)

    for x in match:
        print("Found phone number: {}".format("".join(x)))


message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."
isPhoneNumber(message)
