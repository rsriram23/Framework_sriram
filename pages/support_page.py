from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as cond_exp
from time import sleep

class SupportPage(BasePage):
    def __init__(self):
        super().__init__()
        self.open_site()
        self.d.find_element('xpath', "//button[@role='menuitem']/span[contains(text(),'Support')]/..").click()
        self.d.find_element('xpath', "//a[contains(text(),'Support Home')]").click()
        print(self.d.current_url)
        self.search_box=self.wait_obj.until(cond_exp.element_to_be_clickable(('id', 'homemfe-dropdown-input')))

    def search_14g_guide(self):

        self.search_box.clear()
        self.search_box.send_keys("Integrated System for Microsoft Azure Stack Hub 14G")
        button=self.d.find_element('id', 'btnSubmit')
        self.d.execute_script('arguments[0].click()',button)
        sleep(10)
        urlc=self.d.current_url
        self.d.close()
        return urlc

    def search_rasr_document(self):
        #search textbox - mh-search-input
        # sleep(30)
        # self.d.back()
        self.search_box.clear()
        self.search_box.send_keys("RASR")

        # sleep(20)
        button = self.d.find_element('id', 'btnSubmit')
        self.d.execute_script('arguments[0].click()', button)

        sleep(40)
        urlcurrent=self.d.current_url
        self.d.close()
        return urlcurrent