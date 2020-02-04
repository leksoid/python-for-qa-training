from model.contact import Contact


def test_delete_contact(app):
    test_data = Contact(first_name="John", last_name="Paparonchik", title="CEO", company="Purple Pants",
                        primary_address="1234 Somewhere Rd\nSan Matiago, CA 92109",
                        mobile_number="6192778990", email="paparonchik@pants.com")
    if app.contact_helper.get_count() == 0:
        app.contact_helper.create(test_data)
    initial_contacts = app.contact_helper.get_contacts()
    app.contact_helper.delete_first()
    app.wd.refresh()
    final_contacts = app.contact_helper.get_contacts()
    assert len(initial_contacts) - 1 == len(final_contacts)
    initial_contacts[0:1] = []
    assert initial_contacts == final_contacts
