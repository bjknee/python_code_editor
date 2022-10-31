/codesender-project-gteam
└── /code_server
    ├── /src
    │   └── /code_server
    │        └── __init__.py
    │        └── __main__.py
    │        └── /ALL ADDITIONAL MODULES PLACED IN THIS FOLDER
    ├── /templates
    │   └── index.html
    │
    └── setup.py

INSTRUCTIONS TO BE ADDED TO README
Installation:
    - Clone repository from github with command:
        ~$ git clone https://github.com/MUN-CS2005/codesender-project-gteam
    - In terminal, navigate to the code_server directory created from cloning the repository
    - Once inside code_server, run the command:
        ~$ pip install -e .
    - Code sender should now be installed

Launching the Server:
    - In terminal, execute the command:
        ~$ python3 -m code_server
    - Open any web browser and navigate to:
        localhost:8080

