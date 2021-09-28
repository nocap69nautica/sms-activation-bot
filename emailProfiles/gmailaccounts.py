import random
import names
import csv


class gmailAccounts():

    def __init__(self, gmail):
        self.gmailDomain = gmail

    def domainNameGmail(self):
        return self.gmailDomain


class outlookAccounts():
    def __init__(self, outlook):
        self.outlookDomain = outlook

    def domainNameOutlook(self):
        return self.outlookDomain


gmail = gmailAccounts(gmail="@gmail.com")
outlook = outlookAccounts(outlook="@outlook.com")


def accounts():
    emails = input(
        "Please type how many profiles you would like to make...")
    if emails.isdigit() is True:
        return int(emails)
    if emails.isdigit() is False:
        print("Error invalid character/s, make sure you are entering a digit.")


with open(f'./end.csv', 'w', newline='') as file:
    fieldNames = ['first name', 'second name', 'email']
    writer = csv.DictWriter(file, fieldnames=fieldNames)
    writer.writeheader()
    for i in range(accounts()):
        fullNames = names.get_full_name()
        name = fullNames.replace(" ", "") + str(random.randint(0, 99))
        gmailsAcc = name + gmailAccounts.domainNameGmail(gmail)
        space = fullNames.find(" ")
        first = fullNames[:space]
        second = fullNames[space:].replace(" ", "")
        writer.writerow(
            {'first name': first, 'second name': second, 'email': gmailsAcc})
