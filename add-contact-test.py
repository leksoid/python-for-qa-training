# -*- coding: utf-8 -*-
from selenium import webdriver
from contact import Contact
import unittest


class AddContactTest(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.create_new_contact(wd, Contact(first_name="John", last_name="Paparonchik",
                                            title="CEO", company="Purple Pants",
                                            primary_address="1234 Somewhere Rd\nSan Matiago, CA 92109",
                                            mobile_number="6192778990", email="paparonchik@pants.com"))
        self.back_to_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def back_to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def create_new_contact(self, wd, contact):
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").send_keys(contact.primary_address)
        wd.find_element_by_name("mobile").send_keys(contact.mobile_number)
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()