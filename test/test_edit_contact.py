from model.contact import Contact


def test_edit_contact_names(app):
    test_data = Contact(first_name="John", last_name="Paparonchik", title="CEO", company="Purple Pants",
                        primary_address="1234 Somewhere Rd\nSan Matiago, CA 92109",
                        mobile_number="6192778990", email="paparonchik@pants.com")
    new_test_data = Contact(first_name="Abrahabra", last_name="Babangida")
    # ensure pre-condition
    if app.contact_helper.get_count() == 0:
        app.contact_helper.create(test_data)
    # main test
    initial_contacts = app.contact_helper.get_contacts()
    new_test_data.id = initial_contacts[0].id
    app.contact_helper.edit_first(new_test_data)
    assert len(initial_contacts) == app.contact_helper.get_count()
    final_contacts = app.contact_helper.get_contacts()
    initial_contacts[0] = new_test_data
    assert sorted(initial_contacts, key=Contact.by_id_or_max) == sorted(final_contacts, key=Contact.by_id_or_max)


def test_edit_contact_email(app):
    if app.contact_helper.get_count() == 0:
        app.contact_helper.create(
            Contact(first_name="John", last_name="Paparonchik", title="CEO", company="Purple Pants",
                    primary_address="1234 Somewhere Rd\nSan Matiago, CA 92109",
                    mobile_number="6192778990", email="paparonchik@pants.com"))
    app.contact_helper.edit_first(Contact(email="new-email@yahoo.com"))
