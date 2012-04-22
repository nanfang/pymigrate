import glob
import os
import sys
import optparse
import json

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
        trace_file = self.trace_file()
        if os.path.exists(trace_file):
            with open(trace_file, 'w') as fp:
                json.dump([], fp)
        print('All migrate trace cleared.')


    def run(self):
        if not self.to_execute:
            print('Your system is up to date.')
            return
        for script in self.to_execute:
            print('Executing: %s' % script)
            try:
                if script.endswith('.py'):
                    status = os.system('python %s' % os.path.join(self.directory, script))
                else:
                    status = os.system(os.path.join(self.directory, script))
            except Exception as ex:
                print('Fail to execute %s because: %s' %(script, ex))
                self.exit_run(-1)
            if status:
                print('Fail to execute %s' % script)
                self.exit_run(status)
            self.executed.append(script)
        self.exit_run(0)

    def exit_run(self, status):
        with open(self.trace_file(), 'w') as fp:
            json.dump(self.executed, fp)
        sys.exit(status)

    def trace_file(self):
        return '%s/.pymigrate' % (os.getenv('USERPROFILE') or os.getenv('HOME'))

    def load_trace(self):
        trace_file = self.trace_file()
        if not os.path.exists(trace_file):
            self.executed = []
            with open(trace_file, 'w') as fp:
                json.dump([], fp)
        else:
            with open(trace_file, 'r') as fp:
                self.executed = json.load(fp)

        self.to_execute = [os.path.basename(path) for path in glob.glob(os.path.join(self.directory, '*'))
                           if os.path.isfile(path) and os.path.basename(path) not in self.executed]
        self.to_execute.sort(cmp=_sort_script)


def _sort_script(name1, name2):
    index1 = _script_index(name1)
    index2 = _script_index(name2)
    if index1 == index2:
        return cmp(name1, name2)
    if index1 is not None and index2 is not None:
        return index1 - index2
    if index1 is not None:
        return 1
    if index2 is not None:
        return -1


def _script_index(name):
    pos = name.find('_')

    if pos > 0 and name[:pos].isdigit():
        return int(name[:pos])
    return None


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