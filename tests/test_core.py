""" Test of test_repo.core

:Author: Arthur Goldberg <Arthur.Goldberg@mssm.edu>
:Date: 2019-2-12
:Copyright: 2019, Karr Lab
:License: MIT
"""

import unittest

from test_repo.core import TestNew, Reference


class TestCore(unittest.TestCase):

    def test_test(self):
        hi_dad = 'hi dad'
        reference = Reference(
            id='Reference_1',
            value=hi_dad
        )
        test = TestNew(
            id='Test_1',
            existing_attr='hi mom',
            references=[reference]
        )
        self.assertEqual(reference.value, hi_dad)
        self.assertEqual(test.references[0], reference)
        self.assertEqual(test.name, TestNew.Meta.local_attributes['name'].attr.default)
