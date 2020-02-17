from random import randrange


def test_delete_contact(app, data_provider_contacts):
    if app.contact_helper.get_count() == 0:
        app.contact_helper.create(data_provider_contacts)
    initial_contacts = app.contact_helper.get_contacts()
    index = randrange(len(initial_contacts))
    app.contact_helper.delete_by_index(index)
    app.wd.refresh()
    assert len(initial_contacts) - 1 == app.contact_helper.get_count()
    final_contacts = app.contact_helper.get_contacts()
    initial_contacts[index:index+1] = []
    assert initial_contacts == final_contacts
