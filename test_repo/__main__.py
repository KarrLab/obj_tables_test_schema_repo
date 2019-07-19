""" Command line programs for testing

:Author: Arthur Goldberg <Arthur.Goldberg@mssm.edu>
:Date: 2019-07-19
:Copyright: 2019, Karr Lab
:License: MIT
"""

from obj_model.migrate import data_repo_migration_controllers
import cement


class BaseController(cement.Controller):
    """ Base controller for command line application """

    class Meta:
        label = 'base'
        description = "Test repo"
        help = "Test repo"
        arguments = [
            (['-v', '--version'], dict(action='version', version=wc_sim.__version__)),
        ]

    @cement.ex(hide=True)
    def _default(self):
        self._parser.print_help()


class App(cement.App):
    """ Command line application """
    class Meta:
        label = 'test-repo'
        base_controller = 'base'
        handlers = [BaseController] + data_repo_migration_controllers


def main():
    with App() as app:
        app.run()
