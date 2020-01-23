import pytest
from fixture.application import Application


@pytest.fixture()
def app(request):
    """Start the app"""
    fixture = Application()  # initialization of fixture
    request.addfinalizer(fixture.tear_down)  # how the fixture should be destroyed
    return fixture
