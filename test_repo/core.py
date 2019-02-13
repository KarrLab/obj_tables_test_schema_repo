""" Example schema for testing migration

:Author: Arthur Goldberg <Arthur.Goldberg@mssm.edu>
:Date: 2019-2-12
:Copyright: 2019, Karr Lab
:License: MIT
"""


from obj_model import (BooleanAttribute, EnumAttribute, FloatAttribute, IntegerAttribute,
                       PositiveIntegerAttribute, RegexAttribute, SlugAttribute, StringAttribute, LongStringAttribute,
                       UrlAttribute, OneToOneAttribute, ManyToOneAttribute, ManyToManyAttribute, OneToManyAttribute,
                       TabularOrientation)
import obj_model


class Test(obj_model.Model):
    id = SlugAttribute()
    name = StringAttribute(default='test')
    revision = StringAttribute(default='0.0')
    existing_attr = StringAttribute(default='existing_attr_val')
    # comment on practice_branch
    references = ManyToManyAttribute('Reference', related_name='tests')

    class Meta(obj_model.Model.Meta):
        attribute_order = ('id', 'name', 'revision', 'existing_attr')
        tabular_orientation = TabularOrientation.column


class Reference(obj_model.Model):
    id = SlugAttribute()
    value = StringAttribute()

    class Meta(obj_model.Model.Meta):
        attribute_order = ('id', 'value')
