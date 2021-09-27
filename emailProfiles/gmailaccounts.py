import random
import names
import sys


class gmailAccounts():

    def __init__(self, gmail, outlook):
        self.gmailDomain = gmail
        self.outlookDomain = outlook

    def domainNameGmail(self):
        return self.gmailDomain

    def domainNameOutlook(self):
        return self.outlookDomain


def counter(i=[0]):
    i[0] += 1
    return i[0]


def accounts():
    emails = input(
        "Please type how many profiles you would like to make...")
    if emails.isdigit() is True:
        return int(emails)
    if emails.isdigit() is False:
        print("Error invalid character/s, make sure you are entering a digit.")


for i in range(1):
    open(f"profiles{counter}", "w")
for i in range(accounts()):
    fullNames = names.get_full_name().replace(" ", "")
    fullNames + str(random.randint(0, 99))
    print(fullNames, file=open(f"profiles{counter}", "a"))
