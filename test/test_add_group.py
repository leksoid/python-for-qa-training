# -*- coding: utf-8 -*-
from model.group import Group
from data.group_data import data_provider
import pytest


@pytest.mark.parametrize("test_data", data_provider, ids=[repr(each) for each in data_provider])
def test_add_new_group(app, test_data):
    initial_groups = app.group_helper.get_groups()
    app.group_helper.create(test_data)
    final_groups = app.group_helper.get_groups()
    initial_groups.append(test_data)
    assert sorted(initial_groups, key=Group.by_id_or_max) == sorted(final_groups, key=Group.by_id_or_max)


