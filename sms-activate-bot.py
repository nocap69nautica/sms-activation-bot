import requests
from time import sleep


# Classes for values in url


class client:
    def __init__(self, api, website):
        self.apiName = api
        self.website = website

    def api_method(self):
        full = self.website.replace("$api_key", "")
        index = full.find("api_key=&"[-1])
        x = full[:index] + self.apiName + full[index:-1]
        return x
    # Gets the website upto api_key= and inputs the api key


class Balance:
    def __init__(self, balance):
        self.balanceName = balance

    def service_balance(self):
        return self.balanceName


class service:
    def __init__(self, servicecode):
        self.services = servicecode

    def serviceinfo(self):
        serviceBlank = self.services.replace("$service", "")
        return serviceBlank


class country:
    def __init__(self, isocode):
        self.iso = isocode

    def countrycode(self):
        iso_here = self.iso.replace("$country", "")
        return iso_here


class getnumber:
    def __init__(self, urlNeeded):
        self.getnumber = urlNeeded

    def getnumberurl(self):
        return self.getnumber

# Urls


ApiUrl = client(api=open("api_key.txt").read(),
                website="https://sms-activate.ru/stubs/handler_api.php?api_key=$api_key&")
BalanceUrl = Balance(balance="&action=getBalance")
ServiceUrl = service(servicecode="&service=$service")
CountryUrl = country(isocode="&country=$country")
GetNumberUrl = getnumber(urlNeeded="&action=getNumber")


# User input function for bot etc.

def Balance_get():
    x = input("Would you like to run this request? [Y/N] ").lower()
    if x == "y":
        r = requests.get(getBalance())
        print(r.text)
    elif x == "n":
        print("Ending...")
    else:
        SyntaxError
        print("Command invalid, ending.")

# Functions stored


def getNumber():
    return GetNumberUrl.getnumberurl()


def urlStart():
    return ApiUrl.api_method()


def getService():
    return ServiceUrl.serviceinfo()


def getIso():
    return CountryUrl.countrycode()


def endNumber():
    return urlStart().strip() + "&action=setStatus" + "&status=8"


def completeNumber():
    return urlStart().strip() + "&action=setStatus" + "&status=6"

# Main functions


def getBalance():
    return ApiUrl.api_method().strip() + BalanceUrl.service_balance()


def order_number():
    serviceNo = input("""First, what service would you like to choose?
You can find a full list of services at:

        |* https://sms-activate.ru/en/api2#additionalService *|

Type service:""").lower()
    boolean = serviceNo.isdigit()
    if len(serviceNo) == 2 and boolean == False:
        serviceCodeUrl = getService() + str(serviceNo)
        actionGetNumber = getNumber() + serviceCodeUrl
        iso = input("Enter country ISO code: ")
        if iso.isdigit() == True and len(iso) == 2:
            iso_url = str(getIso()) + str(iso)
            order = urlStart().strip() + actionGetNumber.strip() + iso_url
            iso_url = requests.get(order)
            print(iso_url.text)
            # This a,b,c is to directly get the ID
            a = iso_url.text.find(":")
            b = iso_url.text.find(":", 20)
            c = iso_url.text[a:b]
            d = c.replace(":", "")
            options = input(
                "TYPE: Complete or Cancel: ").lower()
            if options == "complete":
                completion = completeNumber().strip() + "&id=" + d
                final = requests.get(completion)
                print(completion)
                print(final.text)
            if options == "cancel":
                cancellation = endNumber().strip() + "&id=" + d
                ending = requests.get(cancellation)
                print(cancellation)
                print(ending.text)
        else:
            print(
                "Invalid characters (Too many/less or invalid characters or both. Only input = 'digitdigit' , '24' etc.")
    elif len(serviceNo) != 2 or boolean == True:
        print("Unrecognised ending.")
    else:
        SyntaxError
        print("Unrecognised ending.")


order_number()
