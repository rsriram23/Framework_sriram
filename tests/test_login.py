from pages.login_page import LoginPage

class TestLogin:
    lp = LoginPage()
    def test_valid_login(self):
        login_message=self.lp.perform_login()
        assert 'sriram' in login_message.lower(), "Expected a welcome 'user' message."


    def test_invalidUserName_login(self):
        error_message_expected = "We are unable to match the details you entered with our records"
        message_received=self.lp.perform_login('iu')
        assert error_message_expected==message_received,f"Expected a failure message but got {message_received}."

    def test_invalidPassword_login(self):
        error_message_expected = "incorrect password"
        message_received=self.lp.perform_login('ip')
        assert error_message_expected in message_received,f"Expected 'Invalid password' message but got {message_received}."
