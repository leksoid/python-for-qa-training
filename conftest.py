import pytest
import os.path
import json
from fixture.application import Application


fixture = None
config_file = None


@pytest.fixture()
def app(request):
    """Start the app"""
    global fixture
    global config_file
    browser = request.config.getoption("--browser")
    if config_file is None:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))) as f:
            config_file = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser, config_file["host_url"])  # initialization of fixture
    fixture.auth.ensure_login(username=config_file["username"], password=config_file["password"])
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
    parser.addoption("--target", action="store", default="config.json")
