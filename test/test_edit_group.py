from model.group import Group


def test_edit_group_name(app):
    test_data = Group(name="First Sample", header="It is awesome", footer="No its not")
    new_test_data = Group(name="newName")
    if app.group_helper.get_count() == 0:
        app.group_helper.create(test_data)
    initial_groups = app.group_helper.get_groups()
    new_test_data.id = initial_groups[0].id
    app.group_helper.edit_first(new_test_data)
    final_groups = app.group_helper.get_groups()
    assert len(initial_groups) == len(final_groups)
    initial_groups[0] = new_test_data
    assert sorted(initial_groups, key=Group.by_id_or_max) == sorted(final_groups, key=Group.by_id_or_max)


def test_edit_group_header(app):
    if app.group_helper.get_count() == 0:
        app.group_helper.create(Group(name="First Sample", header="It is awesome", footer="No its not"))
    app.group_helper.edit_first(Group(header="newHeader"))


def test_edit_group_footer(app):
    if app.group_helper.get_count() == 0:
        app.group_helper.create(Group(name="First Sample", header="It is awesome", footer="No its not"))
    app.group_helper.edit_first(Group(footer="newFooter"))
