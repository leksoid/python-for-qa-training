import pytest
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()  # initialization of fixture
    request.addfinalizer(fixture.tear_down)  # how the fixture should be destroyed
    return fixture
