from utilities.excel_ops import ExcelOperations
from pages.base_page import BasePage
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


class LoginPage(BasePage):

    def perform_login(self,login_type='v'):
        # bp=BasePage()
        excel=ExcelOperations()

        self.open_site()
        u,p=excel.get_data_from_users_excel(login_type)

        url=self.url
        sleep(5)
        action=ActionChains(self.d)
        signin=self.d.find_element('xpath',"//span[text()='Sign In']/ancestor::a")
        # signin.click()
        action.move_to_element(signin).perform()
        sleep(5)
        print(self.d.current_url)
        signin_button=self.d.find_element('css selector','div.mh-myaccount-ctas>a')
        signin_button.click()
        print(self.d.current_url)
        self.d.find_element('id',"SignInModel_EmailAddress").send_keys(u)
        sleep(60)
        continue_button=self.d.find_element("id","btnContinue")
        continue_button.click()
        print(self.d.current_url)

        if login_type=='v':

            sleep(10)

            password_field=self.d.find_element("id","userPwd_UserInputSecret")
            password_field.send_keys(p)
            sleep(5)
            final_signin_button = self.d.find_element("id", "btnSignIn")
            final_signin_button.click()
            print(self.d.current_url)
            sleep(25)
            print(self.d.current_url)
            return "SUCCESS"
        else:
            if login_type=='iu':
                return self.d.find_element('id','divMessageBarContent').text
            else:
                return self.d.find_element('id', 'divMessageBarContent').text