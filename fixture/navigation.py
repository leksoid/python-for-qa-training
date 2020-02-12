class NavigationHelper:

    def __init__(self, application, host_url):
        self.app = application
        self.host_url = host_url

    def return_to_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("group page").click()

    def back_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_id("maintable")) > 0):
            wd.find_element_by_link_text("home").click()

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_id("maintable")) > 0):
            wd.get("".join([self.host_url, "/addressbook/"]))