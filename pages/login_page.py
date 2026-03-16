from utilities.excel_ops import ExcelOperations
from pages.base_page import BasePage
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


class LoginPage(BasePage):

    def perform_login(self):
        # bp=BasePage()
        excel=ExcelOperations()

        self.open_site()
        u,p=excel.get_data_from_users_excel()

        url=self.url
        # with open('../testdata/user_data.json','r') as user_json:
        #     user_info=json.load(user_json)
        # username=user_info['user']["support_user_password"]
        # print(username)
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
        sleep(20)
        continue_button=self.d.find_element("id","btnContinue")
        continue_button.click()
        print(self.d.current_url)
        sleep(10)

        password_field=self.d.find_element("id","userPwd_UserInputSecret")
        password_field.send_keys(p)
        sleep(5)
        final_signin_button = self.d.find_element("id", "btnSignIn")
        final_signin_button.click()
        print(self.d.current_url)
        sleep(25)
        print(self.d.current_url)
