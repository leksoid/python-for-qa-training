# -*- coding: utf-8 -*-
from model.group import Group


def test_add_new_group(app, json_provider_groups):
    initial_groups = app.group_helper.get_groups()
    app.group_helper.create(json_provider_groups)
    final_groups = app.group_helper.get_groups()
    initial_groups.append(json_provider_groups)
    assert sorted(initial_groups, key=Group.by_id_or_max) == sorted(final_groups, key=Group.by_id_or_max)


