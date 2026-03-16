

from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome,ChromeOptions



class BasePage:

    def __init__(self):
        self.url='https://www.dell.com/support/home/en-in'
        self.name = 'SRIRAM'

    def open_site(self):
        o = ChromeOptions()
        o.add_experimental_option('detach', True)
        self.d = Chrome(o)
        self.d.get(self.url)
