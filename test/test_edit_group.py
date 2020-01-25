from model.group import Group


def test_edit_group_name(app):
    app.auth.login()
    app.group_helper.edit_first(Group(name="newName"))
    app.auth.logout()

def test_edit_group_header(app):
    app.auth.login()
    app.group_helper.edit_first(Group(header="newHeader"))
    app.auth.logout()

def test_edit_group_footer(app):
    app.auth.login()
    app.group_helper.edit_first(Group(footer="newFooter"))
    app.auth.logout()