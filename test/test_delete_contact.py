def test_delete_contact(app):
    app.auth.login()
    app.contact_helper.delete_first()
    app.auth.logout()