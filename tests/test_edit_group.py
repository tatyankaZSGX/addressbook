__author__ = 'ZSGX'
from model.group import Group
import random

#def test_edit_first_group(app, data_group):
#    group = data_group
#    if app.group.count() == 0:
#        app.group.create(Group(name = "test"))
#    old_groups = app.group.get_group_list()
#    group.id = old_groups[0].id
#    app.group.edit_first_group(group)
#    assert len(old_groups) == app.group.count()
#    new_groups = app.group.get_group_list()
#    old_groups[0] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_edit_rand_group(app, db, json_group):
    group = json_group
    if app.group.count() == 0:
        app.group.create(Group(name = "test"))
    old_groups = db.get_group_list()
    edgroup = random.choice(old_groups)
    group.id = edgroup.id
    app.group.edit_group_by_id(edgroup.id, group)
    new_groups = db.get_group_list()
    old_groups.remove(edgroup)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
