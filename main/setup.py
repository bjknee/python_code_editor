from setuptools import setup, find_packages

setup(
    name='codeServer',
    version='0.1.0',
    packages=find_packages(include=['codesender-project-gteam', 'codesender-project-gteam.*']),
    install_requires=[
        # Needs additional requirements
        "pip",
        'PyYAML',
        'pandas==0.23.3',
        'numpy>=1.14.5',
        'Flask'
    ]
)