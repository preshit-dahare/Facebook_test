from facebook_login_utlities.login_page import LoginPageActions


class TestLoginTitle:

    def test_login_page_title(self):
        """
        test case to test the title of our webpage
        :return:
        """
        _expected_title = "Log in to Facebook"

        assert LoginPageActions().title_of_page() == _expected_title
    def test_login_page_title_incorrect(self):
        """
        test case to test the title of our webpage
        :return:
        """
        _expected_title = "ABCHLSKJLKJ to Facebook"

        assert LoginPageActions().title_of_page() == _expected_title

    def test_login_page_message(self):
        LoginPageActions().login_to_facebook()

