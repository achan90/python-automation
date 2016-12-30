#! ~/Documents/python3/projects/environments/automation/bin/python3
import sys
import pyperclip

PASSWORDS = {"email": "dkapdkpakdpakdpakdpakgpoampd",
             "blog": "pdkapdkapkfgpak",
             "luggage": "fpakfpakfkaåfkåa"}


if len(sys.argv) < 2:
    print("Usage: python pw.py [account] - copy account password")
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for {} copied to clipboard".format(account))
else:
    print("There is no account named {}".format(account))
