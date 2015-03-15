# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(firstname="Michael", middlename="J.", lastname="Fox", nickname="Marti",
                               title="Actor", company="Hollywood", address="Los Angeles", homephone="911",
                               mobilephone="9911", workphone="999111", fax="919191", email2="mail2@mail.ff",
                               email3="mail3@mail.ff", homepage="fox.ff", address2="adr2", phone2="02",
                               notes="Back to the Future", bday=9, bmonth=6, byear=1961, aday=26, amonth=10,
                               ayear=1985, path="C:\\img.jpg"))
    app.session.logout()
