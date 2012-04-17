import glob
import os
import sys

def migrate(script_path, migrate_trace=_default_migrate_trace):
    print('Begin to migrate ...')
    migrate_trace.init()
    migrate_trace.clear_last_error()

    all_scripts = [script for script in glob.glob(os.path.join(script_path, '*.*'))]
    all_scripts.sort()
    for script in all_scripts:
        if script not in migrate_trace.executed():
            try:
                migrate_trace.run(script)
            except Exception as ex:
                migrate_trace.error(script, ex.message)
                raise
    print('System is up to date')


class MigrateTrace(object):

    # make sure migrate tracing storage are ready
    def init(self):
        pass
    
    def clear_last_error(self):
        pass

    def run(self, script):
        pass

    def error(self, script, err):
        pass


class FileMigrateTrace(MigrateTrace):
    pass

_default_migrate_trace= FileMigrateTrace()


if __name__ == '__main__':
    migrate(sys.argv[1])

