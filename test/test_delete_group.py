from model.group import Group


def test_delete_group(app):
    if app.group_helper.get_count() == 0:
        app.group_helper.create(Group(name="First Sample", header="It is awesome", footer="No its not"))
    app.group_helper.delete_first()
