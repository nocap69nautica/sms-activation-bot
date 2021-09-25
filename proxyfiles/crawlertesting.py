import os
import zipfile
import proxyobjs
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from time import sleep

PROXY_HOST = proxyobjs.colon1()  # rotating proxy or host
PROXY_PORT = proxyobjs.colon2()  # port
PROXY_USER = proxyobjs.colon3()  # username
PROXY_PASS = proxyobjs.colonending()  # password


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
    s = Service(executable_path="C:\webdrivers\chromedriver.exe")
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
        service=s,
        options=chrome_options)
    return driver


def main():
    driver = get_chromedriver(use_proxy=True)
    # driver.get('https://www.google.com/search?q=my+ip+address')
    driver.get('https://twitter.com/KylekicksZn')
    sleep(15)
    with open("c:\\Users\\kyle\\dev\\sms-activate-bot\\proxyfiles\\proxybridge.txt", 'r+') as bridge:
        f1 = bridge.readline()
        bridge.truncate(0)
        bridge.close()
    with open("c:\\Users\\kyle\\dev\\sms-activate-bot\\proxyfiles\\proxyMain.txt", 'r+') as proxieRemove:
        lines = proxieRemove.readlines()
        proxieRemove.seek(0)
        proxieRemove.truncate()
        proxieRemove.writelines(lines[1])
    with open("c:\\Users\\kyle\\dev\\sms-activate-bot\\proxyfiles\\proxylog.txt", 'r+') as log:
        log.write(f1)


if __name__ == '__main__':
    main()
