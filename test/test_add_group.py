# -*- coding: utf-8 -*-
from model.group import Group


def test_add_new_group(app):
    test_data = Group(name="First Sample", header="It is awesome", footer="No its not")
    initial_groups = app.group_helper.get_groups()
    app.group_helper.create(test_data)
    final_groups = app.group_helper.get_groups()
    initial_groups.append(test_data)
    assert sorted(initial_groups, key=Group.by_id_or_max) == sorted(final_groups, key=Group.by_id_or_max)


def test_add_new_empty_group(app):
    test_data = Group(name="", header="", footer="")
    initial_groups = app.group_helper.get_groups()
    app.group_helper.create(test_data)
    final_groups = app.group_helper.get_groups()
    initial_groups.append(test_data)
    assert sorted(initial_groups, key=Group.by_id_or_max) == sorted(final_groups, key=Group.by_id_or_max)

