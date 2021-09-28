import random
import names
import csv
import functools


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


def Main():
    emails = input(
        "Please type how many profiles you would like to make...")
    if emails.isdigit() is True:
        return int(emails)
    if emails.isdigit() is False:
        print("Error invalid character/s, make sure you are entering a digit.")


def trackcalls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.has_been_called = True
        return func(*args, **kwargs)
    wrapper.has_been_called = False
    return wrapper


@trackcalls
def example():
    pass


example()

if example.has_been_called:
    total = [0]
    for i in range(1):
        total.reverse()
        if total[0] == 0:
            total.append(1)
        if total[0] != 0:
            total.reverse()
            last = total[-1]
            end = last + 1
            total.append(end)
        ending = total[-1]
        with open(f'./end{ending}.csv', 'w', newline='') as file:
            fieldNames = ['first name', 'second name', 'email']
            writer = csv.DictWriter(file, fieldnames=fieldNames)
            writer.writeheader()
            for i in range(Main()):
                fullNames = names.get_full_name()
                name = fullNames.replace(
                    " ", "") + str(random.randint(0, 99))
                gmailsAcc = name + gmailAccounts.domainNameGmail(gmail)
                space = fullNames.find(" ")
                first = fullNames[:space]
                second = fullNames[space:].replace(" ", "")
                writer.writerow(
                    {'first name': first, 'second name': second, 'email': gmailsAcc})
            file.close()
