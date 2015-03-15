__author__ = 'ZSGX'

from selenium.webdriver.firefox.webdriver import WebDriver

class Application:

    def __init__ (self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def create_group(self, Group):
        wd = self.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(Group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(Group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(Group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def destroy(self):
        self.wd.quit()

    def init_contact_creation(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def fill_text_form(self, Contacttext):
        wd = self.wd
        # first name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Contacttext.firstname)
        # middle name
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(Contacttext.middlename)
        # last name
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Contacttext.lastname)
        # nickname
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(Contacttext.nickname)
        # title
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(Contacttext.title)
        # company
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(Contacttext.company)
        # address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(Contacttext.address)
        wd.find_element_by_name("theform").click()
        # telephones
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(Contacttext.homephone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(Contacttext.mobilephone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(Contacttext.workphone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(Contacttext.fax)
        # email & homepage
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(Contacttext.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(Contacttext.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(Contacttext.homepage)
        # Secondary
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(Contacttext.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(Contacttext.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(Contacttext.notes)

    def fill_birthdate_form(self, Contactdate):
        wd = self.wd
        d = Contactdate.day + 2
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%s]" % d).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%s]" % d).click()
        m = Contactdate.month + 1
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%s]" % m).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%s]" % m).click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(Contactdate.year)

    def fill_annivdate_form(self, Contactdate):
        wd = self.wd
        d = Contactdate.day + 2
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[%s]" % d).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[%s]" % d).click()
        m = Contactdate.month + 1
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[%s]" % m).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[%s]" % m).click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(Contactdate.year)

    def fill_pic_form(self, path):
        wd = self.wd
        # photo
        wd.find_element_by_name("photo").click()
        wd.find_element_by_name("photo").send_keys(path)

    def confirm_contact_creation(self):
        wd = self.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
