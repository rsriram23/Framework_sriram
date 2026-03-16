
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self):
        self.url='https://www.dell.com/support/home/en-in'

    def open_site(self):
        o = webdriver.ChromeOptions()
        o.add_experimental_option('detach', True)
        self.d = webdriver.Chrome(o)
        self.d.get(self.url)
