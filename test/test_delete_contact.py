from model.contact import Contact


def test_delete_contact(app):
    if app.contact_helper.get_count() == 0:
        app.contact_helper.create(Contact(first_name="John", last_name="Paparonchik", title="CEO", company="Purple Pants",
                                      primary_address="1234 Somewhere Rd\nSan Matiago, CA 92109",
                                      mobile_number="6192778990", email="paparonchik@pants.com"))
    app.contact_helper.delete_first()
