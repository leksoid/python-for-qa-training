from model.group import Group


class GroupHelper:

    def __init__(self, application):
        self.app = application

    def create(self, group):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        wd.find_element_by_name("new").click()
        self.fill_form(group)
        wd.find_element_by_name("submit").click()
        self.app.navigation.return_to_groups_page()

    def delete_first(self):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        self.select_first()
        wd.find_element_by_name("delete").click()
        self.app.navigation.open_groups_page()

    def edit_first(self, group):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        self.select_first()
        wd.find_element_by_name("edit").click()
        self.fill_form(group)
        wd.find_element_by_name("update").click()
        self.app.navigation.open_groups_page()

    def select_first(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def fill_form(self, group):
        self.enter_field("group_name", group.name)
        self.enter_field("group_header", group.header)
        self.enter_field("group_footer", group.footer)

    def enter_field(self, by_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(by_name).clear()
            wd.find_element_by_name(by_name).send_keys(value)

    def get_count(self):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_groups(self):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        groups = []
        for each in wd.find_elements_by_css_selector(".group"):
            id = each.find_element_by_name("selected[]").get_attribute("value")
            name = each.text
            groups.append(Group(name=name, id=id))
        return groups