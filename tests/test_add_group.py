# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, db, check_ui, json_group):
    group = json_group
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    for atr in group.__dict__:
        if group.__dict__[atr] is None:
            group.__dict__[atr] = ""
    group.id=None
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(map(app.group.clean, db.get_group_list()), key=Group.id_or_max) == sorted(
            app.group.get_group_list(), key=Group.id_or_max)

