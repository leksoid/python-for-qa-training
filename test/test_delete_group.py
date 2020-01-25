def test_delete_group(app):
    app.group_helper.delete_first()
    app.navigation.back_to_home_page()