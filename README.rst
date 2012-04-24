=================================
 pymigrate - Migration By Python
=================================

:Version: 0.1
:Download: http://pypi.python.org/pypi/pymigrate/
:Documentation: http://pymigrate.readthedocs.org/
:Source: http://github.com/nanfang/pymigrate/
:Keywords: Python, Migrate

Documentation
=============

`http://pymigrate.readthedocs.org/ <http://pymigrate.readthedocs.org/>`_


Install
=======

Use pip::

    pip install pymigrate

Use easy_install::

    easy_install pymigrate


Usage
=====

Migrate scripts should be in one folder and with a prefix in name as index. The index is the order of execution of the scripts. eg::

    MIGRATE_FOLDER/001_create_user_schema.py
                   002_create_group_schema.py
                   003_init_user_data.py

Then, run the migrate scripts by::

    pymigrate MIGRATE_FOLDER

After migration is done, we can show the trace by::

    pymigrate -t MIGRATE_FOLDER

When you have new change to apply to the system, just add more scripts into the MIGRATE_FOLDER, and use index for the execution order.
If you just clear the system(like drop the database and recreate) and want to re-run the migrate sequence, you need clear the trace::


    pymigrate -c MIGRATE_FOLDER

