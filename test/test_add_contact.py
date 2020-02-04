# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    initial_contacts = app.contact_helper.get_contacts()
    test_data = Contact(first_name="Bob", last_name="Bermuda", title="CEO", company="Purple Pants",
                        primary_address="1234 Somewhere Rd\nSan Matiago, CA 92109",
                        mobile_number="6192778990", email="paparonchik@pants.com")
    app.contact_helper.create(test_data)
    final_contacts = app.contact_helper.get_contacts()
    initial_contacts.append(test_data)
    assert sorted(initial_contacts, key=Contact.by_id_or_max) == sorted(final_contacts, key=Contact.by_id_or_max)
