from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import sys
import time
import random
from bs4 import BeautifulSoup
import requests
from datetime import datetime

#color codes
black = lambda text: '\033[0;30m' + text + '\033[0m'
red = lambda text: '\033[0;31m' + text + '\033[0m'
green = lambda text: '\033[0;32m' + text + '\033[0m'
yellow = lambda text: '\033[0;33m' + text + '\033[0m'
blue = lambda text: '\033[0;34m' + text + '\033[0m'
magenta = lambda text: '\033[0;35m' + text + '\033[0m'
cyan = lambda text: '\033[0;36m' + text + '\033[0m'
white = lambda text: '\033[0;37m' + text + '\033[0m'
colors = [red,green,yellow,blue,magenta,cyan,white]

payload_amount = 0

ERASE_LINE = '\033[2K\033[1G'

def banner():
    banner = '''
.__     __    __                   .__        __
|  |___/  |__/  |_______   __  _  _|__| ____ |  | __
|  |  \\   __\\   __\\____ \\  \\ \\/ \\/ /  |/    \\|  |/ /
|   Y  \\  |  |  | |  |_> >  \\     /|  |   |  \\    <
|___|  /__|  |__| |   __/____\\/\\_/ |__|___|  /__|_ \\
     \\/           |__| /_____/             \\/     \\/

                                by MrDebugger
'''
    random_color = random.choice(colors)
    print (random_color(banner + "\n"))

def setup():
    start_time = datetime.now().time()
    new_start_time = start_time.strftime("%H:%M:%S")
    folder_name = datetime.now().time()
    new_folder_name = folder_name.strftime("%H_%M_%S")
    return new_start_time,new_folder_name

def main(list,payload_amount):
    try:
        stuff_we_need = setup()
        print (green("[{}] " + white("Starting\n"))).format(stuff_we_need[0])
        os.mkdir("screenshots/" + stuff_we_need[1])
        webdriver32_loc = "chromedriver_win32/chromedriver.exe"
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver32 = webdriver.Chrome(executable_path=webdriver32_loc,chrome_options=options)
        subs_file = open(list,"r")
        for sub in subs_file:
            sub = sub.strip()
            if "http" in sub:
                time.sleep(0.1)
            else:
                sub = "https://" + sub
            payload_amount += 1
            print (cyan("[*] " + white("snap shotting: {}"))).format(sub)
            driver32.get(sub)
            time.sleep(0.2)
            driver32.save_screenshot("screenshots/" + stuff_we_need[1] + "/screen_" + str(payload_amount) + ".png")
        driver32.close()
        stop_time = datetime.now().time()
        new_stop_time = stop_time.strftime("%H:%M:%S")
        print (green("\n[{}] " + white("Done"))).format(new_stop_time)
    except KeyboardInterrupt:
        driver32.quit()
        os.system("clear")
        sys.exit(0)
    except Exception:
        time.sleep(0.1)

try:
    list = sys.argv[1]
    os.system("clear")
    banner()
    main(list,payload_amount)
except IndexError:
    os.system("clear")
    banner()
    print (red("[!] " + white("provide a list with subdomains/domains")))
    sys.exit()
