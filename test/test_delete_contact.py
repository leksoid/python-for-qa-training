from random import randrange
from data.contact_data import data_provider
import pytest


@pytest.mark.parametrize("test_data", data_provider, ids=[repr(each) for each in data_provider])
def test_delete_contact(app, test_data):
    if app.contact_helper.get_count() == 0:
        app.contact_helper.create(test_data)
    initial_contacts = app.contact_helper.get_contacts()
    index = randrange(len(initial_contacts))
    app.contact_helper.delete_by_index(index)
    app.wd.refresh()
    assert len(initial_contacts) - 1 == app.contact_helper.get_count()
    final_contacts = app.contact_helper.get_contacts()
    initial_contacts[index:index+1] = []
    assert initial_contacts == final_contacts
