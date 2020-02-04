from model.group import Group


def test_delete_group(app):
    test_data = Group(name="First Sample", header="It is awesome", footer="No its not")
    if app.group_helper.get_count() == 0:
        app.group_helper.create(test_data)
    initial_groups = app.group_helper.get_groups()
    app.group_helper.delete_first()
    final_groups = app.group_helper.get_groups()
    assert len(initial_groups) - 1 == len(final_groups)
    initial_groups[0:1] = []
    assert initial_groups == final_groups
