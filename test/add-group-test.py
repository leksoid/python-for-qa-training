# -*- coding: utf-8 -*-
from model.group import Group


def test_add_new_group(app):
    app.auth.login(username="admin", password="secret")
    app.group_helper.create(Group(name="First Sample", header="It is awesome", footer="No its not"))
    app.auth.logout()


def test_add_new_empty_group(app):
    app.auth.login(username="admin", password="secret")
    app.group_helper.create(Group(name="", header="", footer=""))
    app.auth.logout()
