class ContactHelper:

    def __init__(self, application):
        self.app = application

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def delete_first(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()

    def edit_first(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@title='Edit']").click()
        self.fill_form(contact)
        wd.find_element_by_name("update").click()
    
    def fill_form(self, contact):
        self.enter_field("firstname", contact.first_name)
        self.enter_field("lastname", contact.last_name)
        self.enter_field("title", contact.title)
        self.enter_field("company", contact.company)
        self.enter_field("address", contact.primary_address)
        self.enter_field("mobile", contact.mobile_number)
        self.enter_field("email", contact.email)

    def enter_field(self, by_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(by_name).clear()
            wd.find_element_by_name(by_name).send_keys(value)