from pages.base_page import BasePage

class TestLogin():
    def test_login(self):
        bp=BasePage()
        bp.support_login()
