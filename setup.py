from setuptools import setup

# Run "pip install -e ." in an activated virtual environment to run setup.py
# and install the codesender package
setup(
    #
    name="codesender",
    version="0.0.0",
    author="G Team",
    description="Codesender project for COMP2005",
    url="https://github.com/MUN-CS2005/codesender-project-gteam",

    # Package and requirement meta data
    packages=['codesender'],
    install_requires=[
        'Flask',
        'lxml',
        'requests',
    ],
    package_data={
        '': ['*.txt', '*.pdf'],
        'codesender': ['docs/*','tests/*', 'static/*', 'templates/*'],
    },
    # Creates a command that can be executed from inside the virtual environment
    # to launch the server
    entry_points={
        'console_scripts': [
            'start-server = codesender.codesender:serverStorage'
        ]
    }
)
