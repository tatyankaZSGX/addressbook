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

def test_edit_rand_group(app, db, check_ui, json_group):
    group = json_group
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    edgroup = random.choice(old_groups)
    group.id = edgroup.id
    app.group.edit_group_by_id(edgroup.id, group)
    new_groups = db.get_group_list()
    old_groups.remove(edgroup)
    for atr in group.__dict__:
        if group.__dict__[atr] is not None:
            edgroup.__dict__[atr] = group.__dict__[atr]
    old_groups.append(edgroup)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(map(app.group.clean, db.get_group_list()), key=Group.id_or_max) == sorted(
            app.group.get_group_list(), key=Group.id_or_max)