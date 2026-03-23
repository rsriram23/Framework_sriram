from pages.login_page import LoginPage

class TestLogin:
    lp = LoginPage()
    def test_valid_login(self):
        assert self.lp.perform_login() == 'SUCCESS', "Expected a success message."


    def test_invalidUserName_login(self):
        error_message_expected = "We are unable to match the details you entered with our records"
        message_received=self.lp.perform_login('iu')
        assert error_message_expected==message_received,f"Expected a failed message but got {message_received}."

    def test_invalidPassword_login(self):
        error_message_expected = "Invalid password"
        message_received=self.lp.perform_login('iu')
        assert error_message_expected in message_received,f"Expected 'Invalid password' message but got {message_received}."
