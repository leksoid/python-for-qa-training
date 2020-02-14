from model.group import Group
from random import randrange
from data.group_data import data_provider
import pytest


@pytest.mark.parametrize("test_data", data_provider, ids=[repr(each) for each in data_provider])
def test_delete_group(app, test_data):
    if app.group_helper.get_count() == 0:
        app.group_helper.create(test_data)
    initial_groups = app.group_helper.get_groups()
    index = randrange(len(initial_groups))
    app.group_helper.delete_by_index(index)
    assert len(initial_groups) - 1 == app.group_helper.get_count()
    final_groups = app.group_helper.get_groups()
    initial_groups[index:index+1] = []
    assert initial_groups == final_groups
