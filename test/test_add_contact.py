# -*- coding: utf-8 -*-
from model.contact import Contact
from data.contact_data import data_provider
import pytest


@pytest.mark.parametrize("test_data", data_provider, ids=[repr(each) for each in data_provider])
def test_add_contact(app, test_data):
    initial_contacts = app.contact_helper.get_contacts()
    app.contact_helper.create(test_data)
    final_contacts = app.contact_helper.get_contacts()
    initial_contacts.append(test_data)
    assert sorted(initial_contacts, key=Contact.by_id_or_max) == sorted(final_contacts, key=Contact.by_id_or_max)
