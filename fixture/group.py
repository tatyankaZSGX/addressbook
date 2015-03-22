__author__ = 'ZSGX'

from model.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/group.php")and len(wd.find_elements_by_name("new"))== 0:
            wd.find_element_by_link_text("groups").click()

    def fill_group_form(self, Group):
        wd = self.app.wd
        self.app.edit_field(field_name="group_name", text=Group.name)
        self.app.edit_field(field_name="group_header", text=Group.header)
        self.app.edit_field(field_name="group_footer", text=Group.footer)

    def create(self, Group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(Group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def edit_first_group(self, Group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        #init editing
        wd.find_element_by_name("edit").click()
        self.fill_group_form(Group)
        #submit editing
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_group_list(self):
        wd = self.app.wd
        self.open_groups_page()
        gr_list = []
        for el in wd.find_elements_by_css_selector("span.group"):
            text = el.text
            id = el.find_element_by_name("selected[]").get_attribute("value")
            gr_list.append(Group(name=text, id=id))
        return gr_list