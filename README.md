# This should be edited!

This is a example package for showing distribution using pip and including a flask module.

The package includes:

## Ass5_comp2005_description - description of this module.
- takeQuiz - a module for taking a quiz
- flask_takeQuiz - a flask front-end for the takeQuiz module
- templates - jinja templates folder for flask
- static - folder for static elements (just some css for jinja at the moment)
- docs - an empty folder for docs and team members sign-off
- tests - folder for the unit test examples.
-       TO RUN THE TESTS: the unit tests can be run with 'python3 -m unittest', 
        but must be run from inside the install directory, since the modules are not exported.
        The package __init__.py files could be changed to export the modules,
        but this was not covered in class or tutorials.

## TO RUN THE FLASK APPLICATION:
    with flask installed the shell commands are:
        $ pip3 --upgrade
        $ pip3 install Flask
        $ export FLASK_APP=flask_takeQuiz.py
        $ flask run
