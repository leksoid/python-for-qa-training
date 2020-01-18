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
    app.login(username="admin", password="secret")
    app.create_new_group(Group(name="First Sample", header="It is awesome", footer="No its not"))
    app.logout()


def test_add_new_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_new_group(Group(name="", header="", footer=""))
    app.logout()
