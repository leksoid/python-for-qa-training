# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, json_provider_contacts):
    initial_contacts = app.contact_helper.get_contacts()
    app.contact_helper.create(json_provider_contacts)
    final_contacts = app.contact_helper.get_contacts()
    initial_contacts.append(json_provider_contacts)
    assert sorted(initial_contacts, key=Contact.by_id_or_max) == sorted(final_contacts, key=Contact.by_id_or_max)
