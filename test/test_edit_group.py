from model.group import Group
from random import randrange


def test_edit_group_name(app, data_provider_groups):
    new_test_data = Group(name="newName")
    if app.group_helper.get_count() == 0:
        app.group_helper.create(data_provider_groups)
    initial_groups = app.group_helper.get_groups()
    index = randrange(len(initial_groups))
    new_test_data.id = initial_groups[index].id
    app.group_helper.edit_by_index(new_test_data, index)
    assert len(initial_groups) == app.group_helper.get_count()
    final_groups = app.group_helper.get_groups()
    initial_groups[index] = new_test_data
    assert sorted(initial_groups, key=Group.by_id_or_max) == sorted(final_groups, key=Group.by_id_or_max)


def test_edit_group_header(app, data_provider_groups):
    if app.group_helper.get_count() == 0:
        app.group_helper.create(data_provider_groups)
    app.group_helper.edit_first(Group(header="newHeader"))


def test_edit_group_footer(app, data_provider_groups):
    if app.group_helper.get_count() == 0:
        app.group_helper.create(data_provider_groups)
    app.group_helper.edit_first(Group(footer="newFooter"))
