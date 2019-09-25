""" Example schema for testing migration

:Author: Arthur Goldberg <Arthur.Goldberg@mssm.edu>
:Date: 2019-2-12
:Copyright: 2019, Karr Lab
:License: MIT
"""


from obj_tables import SlugAttribute, StringAttribute, ManyToManyAttribute, TableFormat
import obj_tables


class TestNew(obj_tables.Model):
    id = SlugAttribute()
    name = StringAttribute(default='test')
    url = StringAttribute()
    branch = StringAttribute()
    revision = StringAttribute()
    existing_attr = StringAttribute(default='existing_attr_val')
    # comment on master branch
    references = ManyToManyAttribute('Reference', related_name='tests')

    class Meta(obj_tables.Model.Meta):
        attribute_order = ('id', 'name', 'revision', 'existing_attr')
        tabular_orientation = TableFormat.column


class Reference(obj_tables.Model):
    # comment on practice_branch
    id = SlugAttribute()
    value = StringAttribute()

    class Meta(obj_tables.Model.Meta):
        attribute_order = ('id', 'value')

# comment
# another
# change after merge


