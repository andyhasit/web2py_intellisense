

def generate_auto_completion_file(db, file_path):
    """
    This function generates a .py file with dummy class definitions mimicking
    a number of fake global variables commonly used in web2py, so that you can get
    auto-completion support in IDEs which support that (e.g. Pyscripter).
    
    For the "db" object it provides fakes all the way down to table's field attributes:

        db.
        db.my_table.
        db.my_table.my_field.
        db.my_table.my_field.represent

    For other objects like "response" and "request" you get what you get.
    To use get autocomplete in a controller or model, do a fake import:
    
    if 0:
        import autocomplete_fakes.py # or whatever your file is called.
    This is usually enough to trick the IDE.
    
    Be sure to call this function after all the tables have been defined on 'db' 
    i.e. after all the models have executed.
    """
    
    import os
    f = open(file_path, 'w')
    for line in [
        '#!/usr/bin/python',
        '#-*- coding: utf-8 -*-',
        '#  This file defines a number of fake global variables commonly used in web2py,',
        '#  simply to provide auto-completion support in an IDE.',
        '#  For the "db" oject it provides fakes all the way down to table\'s field\'s attributes:',
        '#  db.my_table.my_field.represent',
        '#  For other objects like "response" and "request" you get what you get.',
        '#  It is rebuilt from a running copy of db by the function generate_auto_completion_file()',
        '#  which is most likely in the auto_completion_support.py file in modules.',
        '#',
        'from gluon import *',
        'from gluon.globals import *',
        ]:
        f.write('%s\n' % line)
    f.write('\n\n')
    tables = []
    for table in db.tables:
        tables.append(table)
        f.write('\nclass %s:\n' % table.capitalize())
        f.write('    def  __init__(self):\n')
        for field in db[table].fields:
            f.write('        self.%s = Field("dummy")\n' % field)
        f.write('\n    def insert(self, %s):\n' % ', '.join(['%s=None' % field for field in db[table].fields]))
        f.write('        pass\n\n')

    f.write('\nclass FakeDAL(DAL):\n')
    f.write('    def  __init__(self):\n')
    for table in tables:
        f.write('        self.%s = %s()\n' % (table,  table.capitalize()))
    f.write('\n')
    fake_globals = ['session', 'response', 'request', 'auth']
    for i in fake_globals:
        f.write('\nclass Fake%s(%s):\n' % (i.capitalize(), i.capitalize()))
        f.write('    def  __init__(self):\n')
        f.write('        pass\n')
        f.write('%s = Fake%s()\n' % (i, i.capitalize()))
    for line in [
        'db = FakeDAL()',
        "__all__ = ['db',%s]" % ''.join([" '%s'," % i for i in fake_globals]),
        ]:
        f.write('\n%s\n' % line)
    f.close()



