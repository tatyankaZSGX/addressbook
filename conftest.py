__author__ = 'ZSGX'

import pytest
from fixture.application import Application

fixture = None

@pytest.fixture()
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    homeurl = request.config.getoption("--homeurl")
    if fixture is None:
        fixture = Application(browser, homeurl)
    else:
        if not fixture.is_valid():
            fixture = Application(browser, homeurl)
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture

@pytest.fixture(scope = "session", autouse = True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--homeurl" ,action="store", default="http://localhost/addressbook/")