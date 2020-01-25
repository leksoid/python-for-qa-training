import pytest
from fixture.application import Application


fixture = None

@pytest.fixture()
def app(request):
    """Start the app"""
    global fixture
    if fixture is None:
        fixture = Application()  # initialization of fixture
        fixture.auth.login()
    else:
        if not fixture.is_valid():
            fixture = Application()  # initialization of fixture
            fixture.auth.login()
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop_app(request):
    def final_operation():
        fixture.auth.logout()
        fixture.tear_down()
    request.addfinalizer(final_operation)  # how the fixture should be destroyed
    return fixture
