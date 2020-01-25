def test_delete_contact(app):
    app.contact_helper.delete_first()
    app.navigation.back_to_home_page()