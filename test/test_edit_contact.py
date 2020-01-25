from model.contact import Contact


def test_edit_contact_first_name(app):
    app.auth.login()
    app.contact_helper.edit_first(Contact(first_name="Abrahabra"))
    app.auth.logout()

def test_edit_contact_email(app):
    app.auth.login()
    app.contact_helper.edit_first(Contact(email="new-email@yahoo.com"))
    app.auth.logout()