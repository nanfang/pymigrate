import glob
import os
import sys


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



def main():
    print(sys.argv[1])


