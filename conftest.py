import pytest
from fixture.application import Application


fixture = None


@pytest.fixture()
def app(request):
    """Start the app"""
    global fixture
    browser = request.config.getoption("--browser")
    host_url = request.config.getoption("--hostUrl")
    username = request.config.getoption("--username")
    password = request.config.getoption("--password")
    if fixture is None:
        fixture = Application(browser, host_url)  # initialization of fixture
    else:
        if not fixture.is_valid():
            fixture = Application(browser, host_url)
    fixture.auth.ensure_login(username=username, password=password)
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop_app(request):
    def final_operation():
        fixture.auth.ensure_logout()
        fixture.tear_down()
    request.addfinalizer(final_operation)  # how the fixture should be destroyed
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--hostUrl", action="store", default="http://localhost")
    parser.addoption("--username", action="store")
    parser.addoption("--password", action="store")