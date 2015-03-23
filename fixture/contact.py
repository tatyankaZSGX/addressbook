__author__ = 'ZSGX'

from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_contact_form(self, Contact):
        wd = self.app.wd
        self.app.edit_field(field_name="firstname", text=Contact.firstname)
        self.app.edit_field(field_name="middlename", text=Contact.middlename)
        self.app.edit_field(field_name="lastname", text=Contact.lastname)
        self.app.edit_field(field_name="nickname", text=Contact.nickname)
        self.app.edit_field(field_name="title", text=Contact.title)
        self.app.edit_field(field_name="company", text=Contact.company)
        self.app.edit_field(field_name="address", text=Contact.address)
        # wd.find_element_by_name("theform").click()
        #telephones
        self.app.edit_field(field_name="home", text=Contact.homephone)
        self.app.edit_field(field_name="mobile", text=Contact.mobilephone)
        self.app.edit_field(field_name="work", text=Contact.workphone)
        self.app.edit_field(field_name="fax", text=Contact.fax)
        # email & homepage
        self.app.edit_field(field_name="email2", text=Contact.email2)
        self.app.edit_field(field_name="email3", text=Contact.email3)
        self.app.edit_field(field_name="homepage", text=Contact.homepage)
        # Secondary
        self.app.edit_field(field_name="address2", text=Contact.address2)
        self.app.edit_field(field_name="phone2", text=Contact.phone2)
        self.app.edit_field(field_name="notes", text=Contact.notes)
        #birthday
        if Contact.bday is not None:
            d = Contact.bday + 2
            if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%s]" % d).is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%s]" % d).click()
        if Contact.bmonth is not None:
            m = Contact.bmonth + 1
            if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%s]" % m).is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%s]" % m).click()
        self.app.edit_field(field_name="byear", text=Contact.byear)
        #anniversary
        if Contact.aday is not None:
            d = Contact.aday + 2
            if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[%s]" % d).is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[%s]" % d).click()
        if Contact.amonth is not None:
            m = Contact.amonth + 1
            if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[%s]" % m).is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[%s]" % m).click()
        self.app.edit_field(field_name="ayear", text=Contact.ayear)
        # photo
        if Contact.filepath is not None:
            wd.find_element_by_name("photo").send_keys(Contact.filepath)

    def create(self, Contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(Contact)
        #confirm contact creation
        wd.find_element_by_name("submit").click()
        self.go_to_homepage()
        self.contact_cache = None

    def go_to_homepage(self):
        wd = self.app.wd
        if wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("add")) > 0:
            return
        wd.find_element_by_link_text("home").click()

    def go_to_editpage_from_details(self):
        wd = self.app.wd
        self.go_to_homepage()
        #go to details
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[7]/a/img").click()
        #init editing
        wd.find_element_by_name("modifiy").click()

    def go_to_editpage_from_homepage(self):
        wd = self.app.wd
        self.go_to_homepage()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()

    def edit_contact(self, Contact):
        wd = self.app.wd
        self.fill_contact_form(Contact)
        #confirm contact creation
        wd.find_element_by_name("update").click()
        self.go_to_homepage()
        self.contact_cache = None

    def delete_first_contact_from_homepage(self):
        wd = self.app.wd
        self.go_to_homepage()
        #select first contact
        wd.find_element_by_name("selected[]").click()
        #delete
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.go_to_homepage()
        self.contact_cache = None

    def delete_first_contact_while_editing(self):
        wd = self.app.wd
        self.go_to_homepage()
        #select first contact
        wd.find_element_by_name("selected[]").click()
        #init editing
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        #delete from edit page
        wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()
        self.go_to_homepage()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.go_to_homepage()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.go_to_homepage()
            self.contact_cache = []
            for el in wd.find_elements_by_name("entry"):
                cell_list = el.find_elements_by_tag_name("td")
                firstname = cell_list[2].text
                lastname = cell_list[1].text
                id = el.find_element_by_name("selected[]").get_attribute("id")
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return list(self.contact_cache)