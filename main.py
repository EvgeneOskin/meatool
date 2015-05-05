import sys
import logging
from cliff.app import App
from cliff.commandmanager import CommandManager


class PushBulletApp(App):

    log = logging.getLogger(__name__)

    def __init__(self):
        super(PushBulletApp, self).__init__(
            description='cliff demo app',
            version='0.1',
            command_manager=CommandManager('pn_pytool'),
            )

    def initialize_app(self, argv):
        self.log.debug('initialize_app')

    def prepare_to_run_command(self, cmd):
        self.log.debug('prepare_to_run_command %s', cmd.__class__.__name__)

    def clean_up(self, cmd, result, err):
        self.log.debug('clean_up %s', cmd.__class__.__name__)
        if err:
            self.log.debug('got an error: %s', err)


def main(argv=sys.argv[1:]):
    myapp = PushBulletApp()
    return myapp.run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))