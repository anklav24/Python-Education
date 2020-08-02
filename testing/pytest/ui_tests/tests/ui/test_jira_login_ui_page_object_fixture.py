import pytest
from testing.pytest.ui_tests.src.pages.header_page import HeaderPage
from testing.pytest.ui_tests.src.pages.login_page import LoginPage


@pytest.mark.usefixtures("get_driver")
class TestLogin:

    def test_login_to_jira_page_object(self):
        self.login_page = LoginPage(self.driver)
        self.header_page = HeaderPage(self.driver)
        self.login_page.open()
        assert self.login_page.at_page()
        self.login_page.login_to_jira()
        assert self.header_page.at_page()
