from selenium import webdriver
from fixture.auth import AuthorizationHelper
from fixture.navigation import NavigationHelper
from fixture.contact_management import ContactHelper
from fixture.group_management import GroupHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.navigation = NavigationHelper(self)
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
