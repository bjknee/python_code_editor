from setuptools import setup
"""
Author: Brian Knee
Group: G Team
Date: November 3, 2022
The following code uses setup from setuptools to install all of the codesender requirements
into a virtual environment. Creates an entry point script so after installation the server 
can be launched with the "start-server" command while in the virtual environment.
"""

# Run "pip install -e ." in an activated virtual environment to run setup.py
# and install the codesender package

setup(
    name="codesender",
    version="1.0.0",
    author="G Team",
    description="Codesender project for COMP2005",
    url="https://github.com/MUN-CS2005/codesender-project-gteam",

    # Package and requirement meta data
    packages=['codesender', 'codesender.serverStorage'],
    install_requires=[
        'Flask',
        'flask_sqlalchemy'
    ],
    package_data={
        '': ['*.txt', '*.pdf', '*.py'],
        'codesender': ['docs/*', 'tests/*', 'static/*', 'templates/*'],
    },
    # Creates a command that can be executed from inside the virtual environment
    # to launch the server
    py_modules = ['codesender.serverStorage'],
    entry_points={
        'console_scripts': [
            'start-server = codesender.codesender:main'
        ]
    }
)
