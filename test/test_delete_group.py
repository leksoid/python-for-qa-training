def test_delete_group(app):
    app.auth.login()
    app.group_helper.delete_first()
    app.auth.logout()