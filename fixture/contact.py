__author__ = 'ZSGX'

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, Contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        # first name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Contact.firstname)
        # middle name
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(Contact.middlename)
        # last name
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Contact.lastname)
        # nickname
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(Contact.nickname)
        # title
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(Contact.title)
        # company
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(Contact.company)
        # address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(Contact.address)
        wd.find_element_by_name("theform").click()
        # telephones
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(Contact.homephone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(Contact.mobilephone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(Contact.workphone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(Contact.fax)
        # email & homepage
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(Contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(Contact.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(Contact.homepage)
        # Secondary
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(Contact.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(Contact.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(Contact.notes)
        #birthday
        d = Contact.bday + 2
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%s]" % d).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%s]" % d).click()
        m = Contact.bmonth + 1
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%s]" % m).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%s]" % m).click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(Contact.byear)
        #anniversary
        d = Contact.aday + 2
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[%s]" % d).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[%s]" % d).click()
        m = Contact.amonth + 1
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[%s]" % m).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[%s]" % m).click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(Contact.ayear)
        # photo
        #wd.find_element_by_name("photo").click()
        wd.find_element_by_name("photo").send_keys(Contact.filepath)
        #confirm contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
