# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()  # initialization of fixture
    request.addfinalizer(fixture.tear_down)  # how the fixture should be destroyed
    return fixture


def test_add_new_group(app):
    app.auth.login(username="admin", password="secret")
    app.group_helper.create(Group(name="First Sample", header="It is awesome", footer="No its not"))
    app.auth.logout()


def test_add_new_empty_group(app):
    app.auth.login(username="admin", password="secret")
    app.group_helper.create(Group(name="", header="", footer=""))
    app.auth.logout()
