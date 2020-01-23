class AuthorizationHelper:

    def __init__(self, application):
        self.app = application

    def login(self, username, password):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()