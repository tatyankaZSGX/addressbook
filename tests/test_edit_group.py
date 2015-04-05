__author__ = 'ZSGX'
from model.group import Group
from random import randrange
import random
import string
import pytest

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("", 10), header=random_string("header", 10),footer=random_string("footer", 10))
    for i in range(3)
]

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "test"))
    old_groups = app.group.get_group_list()
    group = Group(name="firstgroup", header="", footer="")
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

@pytest.mark.parametrize("group", testdata, ids=[str(x) for x in testdata])
def test_edit_rand_group(app, group):
    if app.group.count() == 0:
        app.group.create(Group(name = "test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
