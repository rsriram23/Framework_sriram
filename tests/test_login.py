from pages.login_page import LoginPage

class TestLogin:
    def test_login(self):
        lp=LoginPage()
        lp.perform_login()
