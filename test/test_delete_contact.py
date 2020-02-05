from model.contact import Contact
from random import randrange


def test_delete_contact(app):
    test_data = Contact(first_name="John", last_name="Paparonchik", title="CEO", company="Purple Pants",
                        primary_address="1234 Somewhere Rd\nSan Matiago, CA 92109",
                        mobile_number="6192778990", email="paparonchik@pants.com")
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
