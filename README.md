Web2py Intellisense
===================

Adds (fake) auto completion and hints to web2py global objects (such as db, request etc...) when working with an editor which provides Python code completion (such as [PyScripter](https://code.google.com/p/pyscripter/)).

###Why?

Because auto completion and hints makes writing code so much faster! 

Unfortnately in web2py what we really want code completion on are the models (db.my_table.my_field etc...) but these are built up dynamically at every request (as opposed to in django where they are class definitions) so that's just not possible.

Unless we cheat :)

###How?



By using a live instance of db object, we can write dummy class definitions mimicking the tables & fields to a file. 

We can then fake import that file:

        if 0:
            import autocomplete_fakes.py

Which is usually enough to trick an editor into importing the definitions without actually importing that into running code.

We then get code completion on the __db__ object all the way down to table's field's attributes:

        db.
        db.my_table.
        db.my_table.my_field.
        db.my_table.my_field.represent

The generated file also creates other global variables like "response" and "request" but just intsantiates them to an empty object.

##Setup Instructions:

1. Copy the file __auto_completion_support.py__ into the modules folder of a web2py application.
2. Import the module and call __generate_auto_completion_file(db, file)__ from any place in your web2py app so long as the models have all been processed. (I call it from a function in a test controller in which I have imported the module)
3. The file parameter is where you want the dummy classes to be written to (file contents will be overwritten).
4. Fake import that file into any source file (controller, module) in which you want auto completion, like so:

        if 0:
            import autocomplete_fakes.py
            from ide_code_completion import *
            
I add that second line to get code completion and hints on things like __SQLForm__ which is useful.

You may need to adjust your IDE settings to include an extra python path to point to the file's location, and also include path to web2py source.

##Getting help:

This has only been tested on [PyScripter](https://code.google.com/p/pyscripter/) on Windows, should work for other IDEs, but that's up to you to figure out as each one is different.

Feel free to improve and send me a pull request!
