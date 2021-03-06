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

    def go_to_details(self, index):
        wd = self.app.wd
        ind = index+2
        self.go_to_homepage()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[%s]/td[7]/a/img" % ind).click()

    def go_to_details_by_id(self, id):
        wd = self.app.wd
        self.go_to_homepage()
        wd.find_element_by_css_selector("a[href='view.php?id=%s']" % id).click()

    def go_to_editpage_by_index_from_details(self, index):
        wd = self.app.wd
        self.go_to_details(index)
        #init editing
        wd.find_element_by_name("modifiy").click()

    def go_to_editpage_by_id_from_details(self, id):
        wd = self.app.wd
        self.go_to_details_by_id(id)
        #init editing
        wd.find_element_by_name("modifiy").click()

    def go_to_editpage_by_index_from_homepage(self, index):
        wd = self.app.wd
        ind = index+2
        self.go_to_homepage()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[%s]/td[8]/a/img" % ind).click()

    def go_to_editpage_by_id_from_homepage(self, id):
        wd = self.app.wd
        self.go_to_homepage()
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()

    def edit_contact(self, Contact):
        wd = self.app.wd
        self.fill_contact_form(Contact)
        #confirm contact creation
        wd.find_element_by_name("update").click()
        self.go_to_homepage()
        self.contact_cache = None

    def delete_first_contact_from_homepage(self):
        wd = self.app.wd
        self.delete_contact_by_index_from_homepage(0)

    def delete_contact_by_index_from_homepage(self, index):
        wd = self.app.wd
        self.go_to_homepage()
        #select contact
        wd.find_elements_by_name("selected[]")[index].click()
        #delete
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.go_to_homepage()
        self.contact_cache = None

    def delete_contact_by_id_from_homepage(self, id):
        wd = self.app.wd
        self.go_to_homepage()
        #select contact
        wd.find_element_by_css_selector("input[id='%s']" % id).click()
        #delete
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.go_to_homepage()
        self.contact_cache = None

    def delete_first_contact_while_editing(self):
        wd = self.app.wd
        self.delete_contact_by_index_while_editing(0)

    def delete_contact_by_index_while_editing(self, index):
        wd = self.app.wd
        self.go_to_editpage_by_index_from_homepage(index)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()
        self.go_to_homepage()
        self.contact_cache = None

    def delete_contact_by_id_while_editing(self, id):
        wd = self.app.wd
        self.go_to_editpage_by_id_from_homepage(id)
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
                address = cell_list[3].text
                mails = cell_list[4].text
                tel = cell_list[5].text
                id = el.find_element_by_name("selected[]").get_attribute("id")
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, tel=tel,
                                                  address=address, mails = mails))
        return list(self.contact_cache)

    def get_contact_props_from_editpage(self, index):
        wd = self.app.wd
        self.go_to_editpage_by_index_from_homepage(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        middlename = wd.find_element_by_name("middlename").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        nickname = wd.find_element_by_name("nickname").get_attribute("value")
        company = wd.find_element_by_name("company").get_attribute("value")
        title = wd.find_element_by_name("title").get_attribute("value")
        address = wd.find_element_by_name("address").text
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        fax = wd.find_element_by_name("fax").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homepage = wd.find_element_by_name("homepage").get_attribute("value")
        address2 = wd.find_element_by_name("address2").text
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        notes = wd.find_element_by_name("notes").text
        return Contact(firstname=firstname, middlename=middlename,lastname=lastname, nickname=nickname, title=title,
                       company=company, address=address, homephone=home, mobilephone=mobile, workphone=work, fax=fax,
                       email=email, email2=email2, email3=email3, homepage=homepage, address2=address2,
                       phone2=phone2, notes=notes, id=id)

    def clean(self, contact):
        def exclude_spaces(str):
            newstr = ' '.join(map(lambda x: x.strip(), str.split()))
            return newstr
        return Contact(id=contact.id, firstname=exclude_spaces(contact.firstname),
                       lastname=exclude_spaces(contact.lastname), address=exclude_spaces(contact.address),
                       homephone=exclude_spaces(contact.homephone), mobilephone=exclude_spaces(contact.mobilephone),
                       workphone=exclude_spaces(contact.workphone), phone2=exclude_spaces(contact.phone2),
                       email=exclude_spaces(contact.email), email2=exclude_spaces(contact.email2),
                       email3=exclude_spaces(contact.email3), tel=None, mails=None)