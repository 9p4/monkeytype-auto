#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

import signal
import sys
import time


def signal_handler(signal, frame):
    print("exiting")
    driver.close()
    sys.exit(0)


options = Options()
options.binary = "/usr/bin/firefox"

driver = webdriver.Firefox(options=options, executable_path="/usr/bin/geckodriver")

signal.signal(signal.SIGINT, signal_handler)

driver.get("https://monkeytype.com/")
assert "Monkeytype" in driver.title
while True:
    input("Press enter to start...")
    totype = ""
    words = driver.find_elements(By.CLASS_NAME, "word")
    for word in words:
        for letter in word.find_elements(By.TAG_NAME, "letter"):
            totype += letter.get_attribute("innerText")
        totype += " "

    # Begin typing
    typebox = driver.find_element(By.ID, "wordsInput")
    for character in totype:
        typebox.send_keys(character)
        time.sleep(0.02)
    # typebox.send_keys(totype)

    input("Press enter to run another set, press ^C or whatever to quit")
