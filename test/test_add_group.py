# -*- coding: utf-8 -*-
from model.group import Group


def test_add_new_group(app):
    app.group_helper.create(Group(name="First Sample", header="It is awesome", footer="No its not"))
    app.navigation.back_to_home_page()

def test_add_new_empty_group(app):
    app.group_helper.create(Group(name="", header="", footer=""))
    app.navigation.back_to_home_page()