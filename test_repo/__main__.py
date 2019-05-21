""" Test remote use of cement Controllers

:Author: Arthur Goldberg <Arthur.Goldberg@mssm.edu>
:Date: 2019-05-18
:Copyright: 2019, Karr Lab
:License: MIT
"""

import cement
from obj_model.migrate import CementControllers, MigratorError
import test_repo


class BaseController(cement.Controller):
    """ Base controller for command line application """

    class Meta:
        label = 'base'
        description = "Test remote use of cement Controllers"

    @cement.ex(hide=True)
    def _default(self):
        self._parser.print_help()


class TestRepo(cement.App):
    """ Command line application """

    class Meta:
        label = 'test_repo'
        base_controller = 'base'
        '''
        # todo: get version working
        arguments = [
            (['-v', '--version'], dict(action='version', version=test_repo.__version__))
        ]
        '''
        handlers = [
            CementControllers.SchemaChangesTemplateController,
            CementControllers.AutomatedMigrationConfigController,
            CementControllers.TestMigrationController,
            CementControllers.MigrateController,
            CementControllers.MigrateFileController
        ]
        # call sys.exit() on close
        close_on_exit = True


def main():
    with TestRepo() as app:
        try:
            app.run()
        except MigratorError as e:
            print("MigratorError > {}".format(e.args[0]))
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()


if __name__ == '__main__':
    main()
