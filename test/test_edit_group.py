from model.group import Group


def test_edit_group(app):
    app.auth.login()
    app.group_helper.edit_first(Group(name="newName", header="newHeader", footer="newFooter"))
    app.auth.logout()