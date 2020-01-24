from model.contact import Contact


def test_edit_contact(app):
    app.auth.login()
    app.contact_helper.edit_first(Contact(first_name="Alex"))
    app.auth.logout()