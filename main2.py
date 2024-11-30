import sqlite3
from http.client import responses

import requests
from bs4 import BeautifulSoup

class DataBaseGUI:
    def __init__(self):
        self.connection = sqlite3.connect("itstep_DB.sl3", 5)
        self.cur = self.connection.cursor()

    def create_table(self):
        self.cur.execute("CREATE TABLE IF NOT EXIST Animals (name TEXT, buy TEXT, sell TEXT);")

    def updateValue(self):



class Currency:
    def __init__(self):
        self.citeUrl = "https://minfin.com.ua/ua/currency/"

    def update(self):
        self.response = requests.get(self.citeUrl)
        if self.response.status_code == 200:
            self.soup = BeautifulSoup(self.response.text, features="html.parser")
            self.soup_list = self.soup.find_all("div", {"class":"sc-1x32wa2-9 bKmKjX"})
            self.total = str(self.soup_list[0]).split("<")[1].split(">")[1]
            self.total2 = str(self.soup_list[3]).split("<")[1].split(">")[1]

