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
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        WebDriverWait(wd, 10).until(ec.presence_of_element_located((By.ID, "maintable")))
        self.contacts_cache = None

    def select_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_elements_by_xpath("//*[@title='Edit']")[index].click()

    def edit_first(self, contact):
        self.edit_by_index(contact, 0)

    def edit_by_index(self, contact, index):
        wd = self.app.wd
        self.select_to_edit_by_index(index)
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
        self.enter_field("home", contact.home_number)
        self.enter_field("work", contact.work_number)
        self.enter_field("email", contact.email)
        self.enter_field("email2", contact.email2)
        self.enter_field("email3", contact.email3)


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
                address = cols[3].text
                emails = cols[4].text
                phones = cols[5].text
                self.contacts_cache.append(Contact(first_name=f_name, last_name=l_name, primary_address=address,
                                                   all_emails=emails, all_phones=phones, id=id))
        return list(self.contacts_cache)

    def get_field_value(self, by_name):
        wd = self.app.wd
        return wd.find_element_by_name(by_name).get_attribute("value")

    def get_contact_from_edit_page(self, index):
        self.select_to_edit_by_index(index)
        first_name = self.get_field_value("firstname")
        last_name = self.get_field_value("lastname")
        title = self.get_field_value("title")
        company = self.get_field_value("company")
        address = self.get_field_value("address")
        mobile_phone = self.get_field_value("mobile")
        home_phone = self.get_field_value("home")
        work_phone = self.get_field_value("work")
        email = self.get_field_value("email")
        email_2 = self.get_field_value("email2")
        email_3 = self.get_field_value("email3")
        return Contact(first_name=first_name, last_name=last_name, title=title, company=company,
                       primary_address=address, mobile_number=mobile_phone, email=email, email2=email_2,
                       email3=email_3, home_number=home_phone, work_number=work_phone)
