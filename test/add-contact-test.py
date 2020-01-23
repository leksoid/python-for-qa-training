# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()  # initialization of fixture
    request.addfinalizer(fixture.tear_down)  # how the fixture should be destroyed
    return fixture


def test_add_contact(app):
    app.auth.login(username="admin", password="secret")
    app.contact_helper.create(Contact(first_name="John", last_name="Paparonchik", title="CEO", company="Purple Pants",
                                      primary_address="1234 Somewhere Rd\nSan Matiago, CA 92109",
                                      mobile_number="6192778990", email="paparonchik@pants.com"))
    app.navigation.back_to_home_page()
    app.auth.logout()
