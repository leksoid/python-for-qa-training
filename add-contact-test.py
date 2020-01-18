# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()  # initialization of fixture
    request.addfinalizer(fixture.tear_down)  # how the fixture should be destroyed
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(first_name="John", last_name="Paparonchik", title="CEO", company="Purple Pants",
                                   primary_address="1234 Somewhere Rd\nSan Matiago, CA 92109",
                                   mobile_number="6192778990", email="paparonchik@pants.com"))
    app.back_to_home_page()
    app.logout()
