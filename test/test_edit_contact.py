from model.contact import Contact


def test_edit_contact_first_name(app):
    app.contact_helper.edit_first(Contact(first_name="Abrahabra"))
    app.navigation.back_to_home_page()

def test_edit_contact_email(app):
    app.contact_helper.edit_first(Contact(email="new-email@yahoo.com"))
    app.navigation.back_to_home_page()