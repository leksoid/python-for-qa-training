def test_delete_contact(app):
    app.auth.login(username="admin", password="secret")
    app.contact_helper.delete_first()