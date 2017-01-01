#! /usr/bin/env python3

import pyperclip

# Still need to figure out how to encrypt the passwords.
PASSWORDS = {"email": "dkapdkpakdpakdpakdpakgpoampd",
             "reddit": "pdkapdkapkfgpak",
             "facebook": "fpakfpakfkaåfkåa"}


account = input("Enter account name: ")

if account.lower() in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for {} copied to clipboard".format(account))

else:
    while True:
        print("There is no account named {}".format(account))
        add_account = input("Do you wish to add it? Y/N: ")

        # Still need to figure how to permanently save the updated dictionary.
        # Dedicated password file that can be imported could possibly work.
        if add_account.lower() == "y":
            PASSWORDS.setdefault(account, input(
                "Enter {} password: ".format(account)))
            print("Password for {} saved".format(account))
            # Used for testing, will be removed once script is completed.
            print(PASSWORDS)
            exit()

        elif add_account.lower() == "n":
            exit()

        else:
            continue
