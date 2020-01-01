import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import random
import string
import prettytable
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from statistics import mean
try:
    print("[-] Starting...")
    options = Options()
    options.headless = False
    twitchpassword = "insert your password here"
    driver = webdriver.Firefox(options=options, executable_path=r'geckodriver.exe')
    url = 'https://www.twitch.tv/popout/martins4k/chat?popout='
    driver.get(url)
    tabelladastampare = prettytable.PrettyTable()
    tabelladastampare.field_names = ["//", "secondo"]
    def randomString(stringLength=999999):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))
    print("[-] Me sto a connette a tuicce...")
    response = requests.get(url)
    if str(response) == "<Response [200]>":
        print("[$] Ollah! Ci siamo.")
        driver.get(url)
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//p[text()='0']")))
        driver.find_element_by_xpath("//p[text()='0']").click()
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Inizia subito!']")))
        driver.find_element_by_xpath("//div[text()='Inizia subito!']").click()
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//img[@alt='Evidenzia il mio messaggio']")))
        driver.find_element_by_xpath("//img[@alt='Evidenzia il mio messaggio']").click()
        print("[-] Faccio il login...")
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "login-username")))
        driver.find_element_by_id("login-username").send_keys("Your_Twitch_username")
        driver.find_element_by_id("password-input").send_keys(twitchpassword)
        time.sleep(1)
        driver.find_element_by_id("password-input").send_keys(Keys.ENTER)
        input("[!] Premi INVIO per continuare...")
        print("[-] Andiamo avanti :)")
        driver.find_element_by_xpath("//textarea[@placeholder='Invia un messaggio']").click()
        driver.find_element_by_xpath("//p[text()='OK, tutto chiaro!']").click()
        lastid = -1
        while True:
            allmessages = driver.find_elements_by_class_name("chat-line__message")
            maxmex= len(allmessages)-1
            if lastid != maxmex:
                if maxmex > 0 and allmessages:
                    lastmex = allmessages[maxmex].find_element_by_class_name("text-fragment").text



                    if lastmex == "chi è gigi?" or lastmex == "chi cazzo è gigi?" or lastmex == "chi è gigi" or lastmex=="chi cazzo è gigi":
                        ans = "Gigi è un figo della madonna HeyGuys "
                        driver.find_element_by_xpath("//textarea[@placeholder='Invia un messaggio']").send_keys(ans)
                        driver.find_element_by_xpath("//textarea[@placeholder='Invia un messaggio']").send_keys(Keys.ENTER)

                    if lastmex == "tomare" or lastmex == "to mare":
                        ans = "Onta Kreygasm "
                        driver.find_element_by_xpath("//textarea[@placeholder='Invia un messaggio']").send_keys(ans)
                        driver.find_element_by_xpath("//textarea[@placeholder='Invia un messaggio']").send_keys(Keys.ENTER)

                    if lastmex == "!insta" or lastmex == "!instagram":
                        ans = "Sto sfigato su Instagram: martins4k"
                        driver.find_element_by_xpath("//textarea[@placeholder='Invia un messaggio']").send_keys(ans)
                        driver.find_element_by_xpath("//textarea[@placeholder='Invia un messaggio']").send_keys(Keys.ENTER)





                    lastid = maxmex
            time.sleep(0.5)

    driver.close()
except:
    pass