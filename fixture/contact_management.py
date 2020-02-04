from model.contact import Contact
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class ContactHelper:

    def __init__(self, application):
        self.app = application

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.navigation.back_to_home_page()
        self.contacts_cache = None

    def delete_first(self):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        WebDriverWait(wd, 10).until(ec.presence_of_element_located((By.ID, "maintable")))
        self.contacts_cache = None

    def edit_first(self, contact):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_element_by_xpath("//*[@title='Edit']").click()
        self.fill_form(contact)
        wd.find_element_by_name("update").click()
        self.contacts_cache = None
    
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

    def get_count(self):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contacts_cache = None

    def get_contacts(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.app.navigation.open_home_page()
            self.contacts_cache = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                cols = element.find_elements_by_tag_name("td")
                l_name = cols[1].text
                f_name = cols[2].text
                self.contacts_cache.append(Contact(first_name=f_name, last_name=l_name, id=id))
        return list(self.contacts_cache)
