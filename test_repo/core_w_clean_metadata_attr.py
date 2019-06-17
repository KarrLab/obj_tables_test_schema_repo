""" Example schema for testing migration

:Author: Arthur Goldberg <Arthur.Goldberg@mssm.edu>
:Date: 2019-2-12
:Copyright: 2019, Karr Lab
:License: MIT
"""


from obj_model import SlugAttribute, StringAttribute, ManyToManyAttribute, TabularOrientation
import obj_model


class Test(obj_model.Model):
    id = SlugAttribute()
    name = StringAttribute(default='test')
    url = StringAttribute()
    branch = StringAttribute()
    revision = StringAttribute()
    existing_attr = StringAttribute(default='existing_attr_val')
    # comment on master branch

    class Meta(obj_model.Model.Meta):
        attribute_order = ('id', 'name', 'revision', 'existing_attr')
        tabular_orientation = TabularOrientation.column


class Foo(obj_model.Model):
    id = SlugAttribute()
