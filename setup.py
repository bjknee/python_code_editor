from setuptools import setup

setup(
    name="codesender",
    version="0.0.0",
    author="G Team",
    description="Codesender project for COMP2005",
    url="https://github.com/MUN-CS2005/codesender-project-gteam",   # project home page, if any


    packages=['codesender'],
    # Check that a package for install is available from PyPI
    install_requires=[
        'Flask'
    ],
    package_data={
        # If any package contains *.txt or *.pdf files, include them:
        '': ['*.txt', '*.pdf'],
        # And everything in the test, doc, static and jinja folders:
        'codesender': ['docs/*','tests/*', 'static/*', 'templates/*'],
    },
    entry_points={
        'console_scripts': [
            'start-server = codesender.codesender:main'
        ]
    }
)
