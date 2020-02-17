from random import randrange


def test_delete_group(app, data_provider_groups):
    if app.group_helper.get_count() == 0:
        app.group_helper.create(data_provider_groups)
    initial_groups = app.group_helper.get_groups()
    index = randrange(len(initial_groups))
    app.group_helper.delete_by_index(index)
    assert len(initial_groups) - 1 == app.group_helper.get_count()
    final_groups = app.group_helper.get_groups()
    initial_groups[index:index+1] = []
    assert initial_groups == final_groups
