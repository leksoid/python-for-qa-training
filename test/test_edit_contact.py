from model.contact import Contact


def test_edit_contact_first_name(app):
    if app.contact_helper.get_count() == 0:
        app.contact_helper.create(Contact(first_name="John", last_name="Paparonchik", title="CEO", company="Purple Pants",
                                      primary_address="1234 Somewhere Rd\nSan Matiago, CA 92109",
                                      mobile_number="6192778990", email="paparonchik@pants.com"))
    app.contact_helper.edit_first(Contact(first_name="Abrahabra"))
    app.navigation.back_to_home_page()

def test_edit_contact_email(app):
    if app.contact_helper.get_count() == 0:
        app.contact_helper.create(Contact(first_name="John", last_name="Paparonchik", title="CEO", company="Purple Pants",
                                      primary_address="1234 Somewhere Rd\nSan Matiago, CA 92109",
                                      mobile_number="6192778990", email="paparonchik@pants.com"))
    app.contact_helper.edit_first(Contact(email="new-email@yahoo.com"))
    app.navigation.back_to_home_page()