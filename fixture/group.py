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
        self.group_cache = None

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_first_group(self):
        wd = self.app.wd
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def edit_first_group(self, Group):
        wd = self.app.wd
        self.edit_group_by_index(0, Group)

    def edit_group_by_index(self, index, Group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        #init editing
        wd.find_element_by_name("edit").click()
        self.fill_group_form(Group)
        #submit editing
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def edit_group_by_id(self, id, Group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        #init editing
        wd.find_element_by_name("edit").click()
        self.fill_group_form(Group)
        #submit editing
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for el in wd.find_elements_by_css_selector("span.group"):
                text = el.text
                id = el.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

    def clean(self, group):
        return Group(id=group.id, name=group.name.strip())
