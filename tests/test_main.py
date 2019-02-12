""" Tests of test_repo command line interface (test_repo.__main__)

:Author: Name <email>
:Date: 2019-2-12
:Copyright: 2019, Karr Lab
:License: MIT
"""

from test_repo import __main__
import test_repo
import capturer
import mock
import unittest


class TestMain(unittest.TestCase):

    def test_cli(self):
        with mock.patch('sys.argv', ['test_repo', '--help']):
            with self.assertRaises(SystemExit) as context:
                __main__.main()
                self.assertRegexpMatches(context.Exception, 'usage: test_repo')

    def test_help(self):
        with self.assertRaises(SystemExit):
            with __main__.App(argv=['--help']) as app:
                app.run()

    def test_version(self):
        with __main__.App(argv=['-v']) as app:
            with capturer.CaptureOutput(merged=False, relay=False) as captured:
                with self.assertRaises(SystemExit):
                    app.run()
                self.assertEqual(captured.stdout.get_text(), test_repo.__version__)
                self.assertEqual(captured.stderr.get_text(), '')

        with __main__.App(argv=['--version']) as app:
            with capturer.CaptureOutput(merged=False, relay=False) as captured:
                with self.assertRaises(SystemExit):
                    app.run()
                self.assertEqual(captured.stdout.get_text(), test_repo.__version__)
                self.assertEqual(captured.stderr.get_text(), '')

    @unittest.skip("failing auto-generated code from 'karr_lab_build_utils setup-repository --dirname ./test_repo --dependency obj_model test_repo'")
    def test_command_1(self):
        with capturer.CaptureOutput(merged=False, relay=False) as captured:
            with __main__.App(argv=['command-1']) as app:
                # run app
                app.run()

                # test that the CLI produced the correct output
                self.assertEqual(captured.stdout.get_text(), 'command_1 output')
                self.assertEqual(captured.stderr.get_text(), '')

    @unittest.skip("failing auto-generated code from 'karr_lab_build_utils setup-repository --dirname ./test_repo --dependency obj_model test_repo'")
    def test_command_2(self):
        with capturer.CaptureOutput(merged=False, relay=False) as captured:
            with __main__.App(argv=['command-2']) as app:
                # run app
                app.run()

                # test that the CLI produced the correct output
                self.assertEqual(captured.stdout.get_text(), 'command_2 output')
                self.assertEqual(captured.stderr.get_text(), '')

    @unittest.skip("failing auto-generated code from 'karr_lab_build_utils setup-repository --dirname ./test_repo --dependency obj_model test_repo'")
    def test_command_3(self):
        with capturer.CaptureOutput(merged=False, relay=False) as captured:
            with __main__.App(argv=['command-3',
                                    'arg-1 value',
                                    'arg-2 value',
                                    '--opt-arg-3', 'opt-arg-3 value',
                                    '--opt-arg-4', 'opt-arg-4 value']) as app:
                # run app
                app.run()

                # test that the arguments to the CLI were correctly parsed
                self.assertTrue(app.pargs.arg_1)
                self.assertTrue(app.pargs.arg_2)
                self.assertTrue(app.pargs.opt_arg_3)
                self.assertTrue(app.pargs.opt_arg_4)

                # test that the CLI produced the correct output
                self.assertEqual(captured.stdout.get_text(), '...')
                self.assertEqual(captured.stderr.get_text(), '...')