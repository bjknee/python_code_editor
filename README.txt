/codesender-project-gteam   // Main repo directory
└── /codesender             // Module directory
    │   ├──/templates       // Holds HTML templates
    │   │   └── index.html  // index.html
    │   ├──/static          // Holds static files
    │   │   └── styles.css  // Master style sheet
    │   ├──/tests           // Module directory for regression tests
    │   │   └── __init__.py // tests __init__
    │   ├── __init__.py     // codesender __init__
    │   └── codesender.py   // temporary codesender module
    ├── README.txt          // README
    └── setup.py            // Installation file

Installation:
    - Clone repository from github with command:
        ~$ git clone https://github.com/MUN-CS2005/codesender-project-gteam
    - In terminal, navigate to the codesender-project-gteam directory
    - Once inside codesender-project-gteam, initialize a virtual environment with command:
        ~$ python3 -m venv venv
    - Activate virtual environment with command:
        ~$ venv\Scripts\activate
    - Install codesender with command:
        ~$ pip install -e .
    - Code sender should now be installed

Launching the Server:
    - While still inside the virtual environment, launch server with command:
        ~$ start-server
        - if error occurs relaunch virtual environment:
            - make sure you are inside codesender directory
            - activate virtual environment with command:
                ~$ venv\Scripts\activate
            - try "start-server" command again
    - Open any web browser and navigate to:
        localhost:8080

Using the application:
    - Type python code into the text area and press "Run" to
      execute the code. You should see the output under the form
    - To save a code snippet, run your code to ensure it outputs
      correctly. Then press "Save Code Snippet", you should be
      notified in the text area that your code snippet has been
      saved.
    - To retrieve a code snippet, press "Pull Code Snippet". You
      should see the code snippet you saved in the previous step
      displayed above the form.

Known Limitations:

    - Currently "Save Code Snippet" only works as intended
      after pressing "Run". This is due to the HTML file not
      being updated until after the POST request sent by the
      "Run" button.


