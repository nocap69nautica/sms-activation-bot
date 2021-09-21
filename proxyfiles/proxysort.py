from selenium.webdriver.chrome import options
from seleniumwire import webdriver
from time import sleep


proxylist = open("Mainproxy.txt", "r")


def lineCount():
    line_count = 0
    for line in proxylist:
        if line != "\n":
            line_count += 1
    return line_count


linecount = lineCount()


def proxySortHttps():
    for proxy in proxylist:
        colon1 = proxy.find(":") + 1
        colon1Remove = proxy[:colon1].replace(
            ":", "")  # prov.rampagenetworks.co.uk
        colon2 = proxy.find(":", colon1) + 1
        colon2Remove = proxy[colon1:colon2].replace(":", "")  # 31112
        colon3 = proxy.find(":", colon2)
        colon3Remove = proxy[colon2:colon3]  # rp_user_4674
        colonEnding = proxy.find(":", colon3) + 1
        # lj5fW8skDdWxQZOg_country-France_session-RPGoWwFB
        colonEndingRemove = proxy[colonEnding:]
        start = "https://" + colon3Remove + colonEndingRemove
        finish = "@" + colon1Remove + colon2Remove
        done = start.strip() + finish.strip()
        return done


def proxySortHttp():
    for proxy in proxylist:
        colon1 = proxy.find(":") + 1
        colon1Remove = proxy[:colon1].replace(
            ":", "")  # prov.rampagenetworks.co.uk
        colon2 = proxy.find(":", colon1) + 1
        colon2Remove = proxy[colon1:colon2].replace(":", "")  # 31112
        colon3 = proxy.find(":", colon2)
        colon3Remove = proxy[colon2:colon3]  # rp_user_4674
        colonEnding = proxy.find(":", colon3) + 1
        # lj5fW8skDdWxQZOg_country-France_session-RPGoWwFB
        colonEndingRemove = proxy[colonEnding:]
        start = "http://" + colon3Remove + colonEndingRemove
        finish = "@" + colon1Remove + colon2Remove
        full = start.strip() + finish.strip()
        return full


httpopen = open("httpproxy.txt", "w")
httpopen.write(proxySortHttp())


PATH = "C:\webdrivers\chromedriver.exe"


w = webdriver.Chrome(PATH, seleniumwire_options=options)
w.get("https://twitter.com/PepsiMaxUK")
sleep(10)
w.quit()
