
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self):
        self.url='https://www.dell.com/support/home/en-in'
        # self.d=''

    def open_site(self):
        o = webdriver.ChromeOptions()
        o.add_experimental_option('detach', True)
        self.d = webdriver.Chrome(o)
        self.wait_obj=WebDriverWait(self.d,30)
        self.d.get(self.url)
