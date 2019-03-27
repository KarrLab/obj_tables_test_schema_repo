""" Generate test fixtures

:Author: Arthur Goldberg <Arthur.Goldberg@mssm.edu>
:Date: 2019-03-16
:Copyright: 2019, Karr Lab
:License: MIT
"""

import unittest
import os
from test_repo.core_w_metadata_attr import TestNew, Reference
from obj_model.utils import set_git_repo_metadata_from_path
import obj_model


@unittest.skip("not a test; use when fixture(s) need updating")
class TestMakeFixtureFiles(unittest.TestCase):

    def test_make_fixtures(self):

        ref_1 = Reference(id='ref_1', value='val_1')
        ref_2 = Reference(id='ref_2', value='val_2')
        test_new_1 = TestNew(
            id='test_new_1',
            existing_attr='x',
            references=[ref_1, ref_2]
        )
        test_new_2 = TestNew(
            id='test_new_2',
            existing_attr='x',
            references=[ref_1, ref_2]
        )
        set_git_repo_metadata_from_path(test_new_1)
        set_git_repo_metadata_from_path(test_new_2)

        fixtures_path = os.path.join(os.path.dirname(__file__), 'fixtures')
        fixture_file = os.path.join(fixtures_path, 'bad_data_file.xlsx')
        obj_model.io.Writer().run(fixture_file, [test_new_1, test_new_2], models=[TestNew, Reference])


from test_repo.core_w_clean_metadata_attr import Test, Foo
@unittest.skip("not a test; use when fixture(s) need updating")
class TestMakeFixtureFileUsingCleanMetadata(unittest.TestCase):

    def test_make_fixtures(self):

        test_new_1 = Test(
            id='test_new_1',
            existing_attr='x',
        )
        test_new_2 = Test(
            id='test_new_2',
            existing_attr='x',
        )
        set_git_repo_metadata_from_path(test_new_1)
        set_git_repo_metadata_from_path(test_new_2)

        foo = Foo(
            id='id_1'
        )

        fixtures_path = os.path.join(os.path.dirname(__file__), 'fixtures')
        fixture_file = os.path.join(fixtures_path, 'bad_data_file_2.xlsx')
        obj_model.io.Writer().run(fixture_file, [test_new_1, test_new_2, foo], models=[Test, Foo])
