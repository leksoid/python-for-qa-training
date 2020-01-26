from model.group import Group


def test_edit_group_name(app):
    if app.group_helper.get_count() == 0:
        app.group_helper.create(Group(name="First Sample", header="It is awesome", footer="No its not"))
    app.group_helper.edit_first(Group(name="newName"))

def test_edit_group_header(app):
    if app.group_helper.get_count() == 0:
        app.group_helper.create(Group(name="First Sample", header="It is awesome", footer="No its not"))
    app.group_helper.edit_first(Group(header="newHeader"))

def test_edit_group_footer(app):
    if app.group_helper.get_count() == 0:
        app.group_helper.create(Group(name="First Sample", header="It is awesome", footer="No its not"))
    app.group_helper.edit_first(Group(footer="newFooter"))
