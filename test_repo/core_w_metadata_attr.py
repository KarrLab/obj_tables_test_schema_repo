""" Example schema for testing migration

:Author: Arthur Goldberg <Arthur.Goldberg@mssm.edu>
:Date: 2019-2-12
:Copyright: 2019, Karr Lab
:License: MIT
"""


from obj_model import SlugAttribute, StringAttribute, ManyToManyAttribute, TabularOrientation
import obj_model


class TestNew(obj_model.Model):
    id = SlugAttribute()
    name = StringAttribute(default='test')
    url = StringAttribute()
    branch = StringAttribute()
    revision = StringAttribute()
    existing_attr = StringAttribute(default='existing_attr_val')
    # comment on master branch
    references = ManyToManyAttribute('Reference', related_name='tests')

    class Meta(obj_model.Model.Meta):
        attribute_order = ('id', 'name', 'revision', 'existing_attr')
        tabular_orientation = TabularOrientation.column
_GIT_METADATA = (TestNew, ('url', 'branch', 'revision'))


class Reference(obj_model.Model):
    # comment on practice_branch
    id = SlugAttribute()
    value = StringAttribute()

    class Meta(obj_model.Model.Meta):
        attribute_order = ('id', 'value')

# comment

