from model.contact import Contact
from random import randrange


def test_edit_contact_names(app, data_provider_contacts):
    new_test_data = Contact(first_name="Abrahabra", last_name="Babangida")
    # ensure pre-condition
    if app.contact_helper.get_count() == 0:
        app.contact_helper.create(data_provider_contacts)
    # main test
    initial_contacts = app.contact_helper.get_contacts()
    index = randrange(len(initial_contacts))
    new_test_data.id = initial_contacts[index].id
    app.contact_helper.edit_by_index(new_test_data, index)
    assert len(initial_contacts) == app.contact_helper.get_count()
    final_contacts = app.contact_helper.get_contacts()
    initial_contacts[index] = new_test_data
    assert sorted(initial_contacts, key=Contact.by_id_or_max) == sorted(final_contacts, key=Contact.by_id_or_max)


def test_edit_contact_email(app, data_provider_contacts):
    if app.contact_helper.get_count() == 0:
        app.contact_helper.create(data_provider_contacts)
    app.contact_helper.edit_first(Contact(email="new-email@yahoo.com"))
