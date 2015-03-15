# -*- coding: utf-8 -*-
import pytest
from contact import Contacttext, Contactdate
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.init_contact_creation()
    app.fill_text_form(Contacttext(firstname="Michael", middlename="J.", lastname="Fox", nickname="Marti", title="Actor", company="Hollywood", address="Los Angeles", homephone="911", mobilephone="9911", workphone="999111", fax="919191", email2="mail2@mail.ff", email3="mail3@mail.ff", homepage="fox.ff", address2="adr2", phone2="02", notes="Back to the Future"))
    app.fill_birthdate_form(Contactdate(day=9, month=6, year=1961))
    app.fill_annivdate_form(Contactdate(day=26, month=10, year=1985))
    app.fill_pic_form(path="C:\\img.jpg")
    app.confirm_contact_creation()
    app.logout()
