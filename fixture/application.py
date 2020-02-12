from selenium import webdriver
from fixture.auth import AuthorizationHelper
from fixture.navigation import NavigationHelper
from fixture.contact_management import ContactHelper
from fixture.group_management import GroupHelper


class Application:

    def __init__(self, browser, host_url):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        elif browser == "edge":
            self.wd = webdriver.Edge()
        else:
            raise ValueError(f"There is no executable for {browser}")
        self.navigation = NavigationHelper(self, host_url)
        self.auth = AuthorizationHelper(self)
        self.group_helper = GroupHelper(self)
        self.contact_helper = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
            
    def tear_down(self):
        self.wd.quit()
