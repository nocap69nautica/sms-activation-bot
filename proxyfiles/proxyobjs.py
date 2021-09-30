import zipfile
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

with open("proxyfiles\proxybridge.txt", "r+") as proxyfile:
    proxylist = proxyfile.readlines()


def remove_lineMain(fileName, lineToSkip):
    """ Removes a given line from a file """
    with open(fileName, 'r') as read_file:
        lines = read_file.readlines()

    currentLine = 1
    with open(fileName, 'w') as write_file:
        for line in lines:
            if currentLine == lineToSkip:
                pass
            else:
                write_file.write(line)

            currentLine += 1

# call the function, passing the file and line to skip


def remove_lineBridge(fileName1, filename2, lineToSkip):
    """ Removes a given line from a file """
    with open(fileName1, 'r') as read_file:
        lines = read_file.readlines()

    currentLine = 1
    with open(filename2, 'w') as write_file:
        for line in lines[:2]:
            if currentLine == lineToSkip:
                pass
            else:
                write_file.write(line)

            currentLine += 1

# call the function, passing the file and line to skip


def colon1():
    for proxy in proxylist:
        colon1 = proxy.find(":") + 1
        colon2 = proxy.find(":", colon1) + 1
        colon3 = proxy.find(":", colon2) + 1  # rp_user_4674
        colonEnding = proxy.find(":", colon3)
        colon2ActualEnding = proxy.find(":", colon1)
        colon1Actual = proxy[:colon1]  # prov.rampagenetworks.co.uk:
        first = colon1Actual.replace(":", "")
        return first


def colon2():
    for proxy in proxylist:
        colon1 = proxy.find(":") + 1
        colon2 = proxy.find(":", colon1) + 1
        colon3 = proxy.find(":", colon2) + 1  # rp_user_4674
        colonEnding = proxy.find(":", colon3)
        colon2ActualEnding = proxy.find(":", colon1)
        colon2Actual = proxy[colon1:colon2ActualEnding]
        second = colon2Actual.replace(":", "")
        return second


def colon3():
    for proxy in proxylist:
        colon1 = proxy.find(":") + 1
        colon2 = proxy.find(":", colon1) + 1
        colon3 = proxy.find(":", colon2) + 1  # rp_user_4674
        colonEnding = proxy.find(":", colon3)
        colon2ActualEnding = proxy.find(":", colon1)
        colon3Actual = proxy[colon2:colon3]
        third = colon3Actual.replace(":", "")
        return third


def colonending():
    for proxy in proxylist:
        colon1 = proxy.find(":") + 1
        colon2 = proxy.find(":", colon1) + 1
        colon3 = proxy.find(":", colon2) + 1  # rp_user_4674
        colonEnding = proxy.find(":", colon3)
        colon2ActualEnding = proxy.find(":", colon1)
        colon4Actual = proxy[colon3:colonEnding]
        return colon4Actual


PROXY_HOST = colon1()  # rotating proxy or host
PROXY_PORT = colon2()  # port
PROXY_USER = colon3()  # username
PROXY_PASS = colonending()  # password


manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
}
"""

background_js = """
var config = {
        mode: "fixed_servers",
        rules: {
        singleProxy: {
            scheme: "http",
            host: "%s",
            port: parseInt(%s)
        },
        bypassList: ["localhost"]
        }
    };

chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "%s",
            password: "%s"
        }
    };
}

chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
);
""" % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)


def get_chromedriver(use_proxy=False, user_agent=None):
    chrome_options = webdriver.ChromeOptions()
    if use_proxy:
        pluginfile = 'proxy_auth_plugin.zip'

        with zipfile.ZipFile(pluginfile, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)
        chrome_options.add_extension(pluginfile)
    if user_agent:
        chrome_options.add_argument('--user-agent=%s' % user_agent)
    driver = webdriver.Chrome(
        executable_path="C:\webdrivers\chromedriver.exe",
        options=chrome_options)
    return driver


def main():
    try:
        d = get_chromedriver(use_proxy=True)
        actions = ActionChains(d)
        # driver.get('https://www.google.com/search?q=my+ip+address')
        d.get('https://eu.aimeleondore.com/products/ald-new-balance-p550-3')
        sleep(5)
        close = d.find_element_by_class_name("glClose")
        actions.click(close)
        d.execute_script('window.scrollTo(0,1500);')
        WebDriverWait(d, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "label[placeholder='8']"))).click()
        sleep(3)
        d.close()
    finally:
        with open("proxyfiles\proxybridge.txt", 'r') as bridge:
            bridgeAll = bridge.readline()
        with open("proxyfiles\proxylog.txt", 'r+') as log:
            log.readlines()
            log.write("\n")
            log.write(bridgeAll)
        remove_lineBridge("proxyfiles/proxyMain.txt",
                          "proxyfiles/proxybridge.txt", 1)
        remove_lineMain("proxyfiles\proxyMain.txt", 1)


if __name__ == '__main__':
    main()
