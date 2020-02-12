# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


def random_data(pre, limit):
    chars = string.ascii_letters + string.digits + " "
    body = "".join([random.choice(chars) for i in range(random.randrange(limit))])
    return f"{pre}{body}"


data_provider = [
    Group(name=random_data("name", 10), header=random_data("header", 20), footer=random_data("footer", 20)),
    Group(name="", header="", footer="")
]


@pytest.mark.parametrize("test_data", data_provider, ids=[repr(each) for each in data_provider])
def test_add_new_group(app, test_data):
    initial_groups = app.group_helper.get_groups()
    app.group_helper.create(test_data)
    final_groups = app.group_helper.get_groups()
    initial_groups.append(test_data)
    assert sorted(initial_groups, key=Group.by_id_or_max) == sorted(final_groups, key=Group.by_id_or_max)


