import glob
import json
import os
import sys
import optparse
import json

class MigrateTrace(object):
    # make sure migrate tracing storage are ready
    def init(self):
        raise NotImplementedError()

    def clear_last_error(self):
        raise NotImplementedError()

    def run(self, script):
        raise NotImplementedError()

    def error(self, script, err):
        raise NotImplementedError()


class FileMigrateTrace(MigrateTrace):
    def init(self):
        # TODO load migrate trace from .pymigrate file
        pass

    def clear_last_error(self):
        # TODO ?
        pass

    def run(self, script):
        # TODO just run the script, and save the migrate trace
        os.system(script)
        pass

    def error(self, script, err):
        # TODO print error and break migrate
        pass

_default_migrate_trace= FileMigrateTrace()


def migrate(script_path, migrate_trace=_default_migrate_trace):
    print('Begin to migrate ...')
    migrate_trace.init()
    migrate_trace.clear_last_error()

    all_scripts = [script for script in glob.glob(os.path.join(script_path, '*.*'))]
    # TODO sort by index
    all_scripts.sort()
    for script in all_scripts:
        if script not in migrate_trace.executed():
            try:
                migrate_trace.run(script)
            except Exception as ex:
                migrate_trace.error(script, ex.message)
                raise
    print('System is up to date')


class Migrator(object):
    def __init__(self, directory):
        super(Migrator, self).__init__()
        self.directory = directory
        self.load_trace()

    def show_trace(self):
        print('Executed:')
        for script in self.executed:
            print(' %s' % script)
        print('')
        print('To execute:')
        for script in self.to_execute:
            print(' %s' % script)

    def clear_trace(self):
        pass

    def run(self):
        pass

    def load_trace(self):
        home = os.getenv('USERPROFILE') or os.getenv('HOME')
        trace_file = '%s/.pymigrate' % home
        if not os.path.exists(trace_file):
            self.executed = []
            with open(trace_file, 'w') as fp:
                json.dump({}, fp)
        else:
            with open(trace_file, 'r') as fp:
                self.executed = json.load(fp).get(self.directory, [])

        self.to_execute = [os.path.basename(path) for path in glob.glob(os.path.join(self.directory, '*'))
                      if os.path.isfile(path) and os.path.basename(path) not in self.executed]


def _option_parser():
    usage = "usage: %prog [options] directory"
    parser = optparse.OptionParser(usage)
    parser.add_option("-t", "--trace",
        action="store_true",
        dest="trace",
        default=False,
        help="show migrate trace information and exit",
    )
    parser.add_option("-c", "--clear",
        action="store_true",
        dest="clear",
        default=False,
        help="clear migrate trace and exit",
    )
    return parser


def main():
    parser = _option_parser()
    options, args = parser.parse_args()
    if not args:
        print(parser.print_help())
        return
    directory = args[0]
    if not os.path.exists(directory) or not os.path.isdir(directory):
        print("'%s' is  not a valid directory" % directory)
        return

    migrator = Migrator(directory)
    if options.trace:
        migrator.show_trace()
    elif options.clear:
        migrator.clear_trace()
    else:
        migrator.run()


if __name__ == '__main__':
    main()