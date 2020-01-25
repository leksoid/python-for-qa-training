from model.group import Group


def test_edit_group_name(app):
    app.group_helper.edit_first(Group(name="newName"))
    app.navigation.back_to_home_page()

def test_edit_group_header(app):
    app.group_helper.edit_first(Group(header="newHeader"))
    app.navigation.back_to_home_page()

def test_edit_group_footer(app):
    app.group_helper.edit_first(Group(footer="newFooter"))
    app.navigation.back_to_home_page()