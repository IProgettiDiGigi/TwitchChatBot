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
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import os
import subprocess

discord = "https://discord.gg/GgtRDvR"
instagram = "https://instagram.com/"
twitchpassword = "Password"
twitchusername = "Username"
streamerusername = "Streamer"

def work(TEXT):
    try:

        PRESENZA_INSTAGRAM = False
        PRESENZA_AZIONE = False
        PRESENZA_DISCORD = False
        stop_words = set(stopwords.words('italian'))

        word_tokens = word_tokenize(TEXT)

        filtered_sentence = [w for w in word_tokens if not w in stop_words]

        filtered_sentence = []

        for w in word_tokens:
            if w not in stop_words:
                filtered_sentence.append(w)
            if w == "avete" or w == "Avete":
                filtered_sentence.append(w)

        print(filtered_sentence)

        try:
            with open("AIMgmt/instagram.gigilearn") as f:
                for line in f.read().splitlines():
                    if line.lower() in (string.lower() for string in filtered_sentence):
                        PRESENZA_INSTAGRAM = True

            with open("AIMgmt/discord.gigilearn") as f:
                for line in f.read().splitlines():
                    if line.lower() in (string.lower() for string in filtered_sentence):
                        PRESENZA_DISCORD = True

            with open("AIMgmt/show.gigilearn") as f:
                for line in f.read().splitlines():
                    if line.lower() in (string.lower() for string in filtered_sentence):
                        PRESENZA_AZIONE = True
        except:
            print("Errore di lettura dizionari")



        response = "IGNORE_GIGIREAD"
        if PRESENZA_AZIONE == True:
            if PRESENZA_DISCORD == True and PRESENZA_INSTAGRAM == False:
                response = "Passa su Discord {} !".format(discord)
            if PRESENZA_INSTAGRAM == True and PRESENZA_DISCORD == False:
                response = "Passa su Instagram {} !".format(instagram)
            if PRESENZA_INSTAGRAM == True and PRESENZA_DISCORD == True:
                response = "Passa su Instagram {} e su Discord {} !".format(instagram, discord)
        print(response)
        return response
    except:
        print("Errore nell'AI Working")

try:
    print("[-] Starting...")
    options = Options()
    options.headless = False


    driver = webdriver.Firefox(options=options, executable_path=r'geckodriver.exe')
    url = 'https://www.twitch.tv/popout/{}/chat?popout='.format(streamerusername)
    driver.get(url)
    tabelladastampare = prettytable.PrettyTable()
    tabelladastampare.field_names = ["//", "secondo"]
    def randomString(stringLength=999999):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))
    print("[-] Mi sto connettendo a Twitch...")
    response = requests.get(url)
    if str(response) == "<Response [200]>":
        print("[$] Ci siamo.")
        driver.get(url)
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//span[text()='0']")))
        driver.find_element_by_xpath("//span[text()='0']").click()
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Inizia subito!']")))
        driver.find_element_by_xpath("//div[text()='Inizia subito!']").click()
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//img[@alt='Evidenzia il mio messaggio']")))
        driver.find_element_by_xpath("//img[@alt='Evidenzia il mio messaggio']").click()
        print("[-] Faccio il login...")
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "login-username")))
        driver.find_element_by_id("login-username").send_keys(twitchusername)
        driver.find_element_by_id("password-input").send_keys(twitchpassword)
        time.sleep(1)
        driver.find_element_by_id("password-input").send_keys(Keys.ENTER)
        input("[!] Completa l'accesso e Premi INVIO per continuare...")
        print("[-] Ok")
        driver.find_element_by_xpath("//textarea[@placeholder='Invia un messaggio']").click()
        driver.find_element_by_xpath("//p[text()='OK, tutto chiaro!']").click()
        lastid = -1
        print("[-] Controllo nuovi messaggi...")
        while True:
            allmessages = driver.find_elements_by_class_name("chat-line__message")
            maxmex= len(allmessages)-1
            if lastid != maxmex:
                if maxmex > 0 and allmessages:
                    lastmex = allmessages[maxmex].find_element_by_class_name("text-fragment").text
                    res = work(lastmex)
                    if res != "IGNORE_GIGIREAD":
                        driver.find_element_by_xpath("//textarea[@placeholder='Invia un messaggio']").send_keys(res)
                        driver.find_element_by_xpath("//textarea[@placeholder='Invia un messaggio']").send_keys(Keys.ENTER)

                    lastid = maxmex
            time.sleep(0.5)

    driver.close()
except :
    print("Errore generico")
    pass

