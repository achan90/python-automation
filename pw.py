#! /usr/bin/env python3

import pyperclip
import shelve

# Still need to figure out how to encrypt the passwords.
PASSWORDS = shelve.open("passwords")


account = input("Enter account name: ")

if account.lower() in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for {} copied to clipboard".format(account))

else:
    while True:
        print("There is no account named {}".format(account))
        add_account = input("Do you wish to add it? Y/N: ")

        if add_account.lower() == "y":
            PASSWORDS[account] = input(
                "Enter {} password: ".format(account))
            print("Password for {} saved".format(account))
            exit()

        elif add_account.lower() == "n":
            exit()

        else:
            continue

PASSWORDS.close()
