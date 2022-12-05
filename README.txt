/codesender-project-gteam                           // Main repo directory
└── /codesender                                     // Module directory
    │   ├──/static                                  // Holds static files
    │   │   └── styles.css                          // Master style sheet
    │   │   └── upload.js                           // Javascript file for uploading code segments
    │   │   └── download.js                         // Javascript file for downloading code segments
    │   ├──/templates                               // Holds HTML templates
    │   │   └── base.html                           // base.html for html templating solution
    │   │   └── index.html                          // index.html extends base.html
    │   │   └── login.html                          // login.html extends base.html
    │   │   └── profileOne.hmtl                     // profileOne.html extends base.html
    │   │   └── profileTwo.html                     // profileTwo.html extends base.html
    │   │   └── profileThree.html                   // profileThree.html extends base.html
    │   ├──/tests                                   // Module directory for regression tests
    │   │   └── __init__.py                         // tests __init__
    │   ├── __init__.py                             // codesender __init__
    │   ├── codesender.py                           // Main application file
    │   ├── recoverWork.py                          // Old recoverWork file (Has been refactored into codesender.py)
    │   └── serverDB.py                             // Database and Application init
    ├── /documentation                              // Documentation directory for all additional documentation
    │       └── /User Stories                       // Directory to hold all user stories for submission 5
    │               ├── user_story_brian.txt        // Brian's User Story
    │               ├── user_story_Gizem.txt        // Gizem's User Story
    │               ├── user_story_jalen.txt        // Jalen's User Story
    │               └── user_story_kayla.txt        // Kayla's User Story
    │        ├── Documentation_Jalen_Sub6           // Jalens Submission 6 Documentation
    │        ├── Submission 6 Documentation         // Submission 6 Documentation
    │        ├── Team Evaluation - Submission 6.txt // Team evaluation for submission 6
    │        ├── Team evaluation - Submission 5.txt // Team evaluation for submission 5
    │        ├── documentation for submission 5.txt // Documentation for submission 5
    │        ├── flask endpoint routing documentation // Flask documentation
    │        ├── save-revert documentation          // Save-Revert documentation
    │        ├── template module                    // HTML templating solution documentation
    │        └── upload_download documentation      // Upload/Download documentation
    ├── /instance                                   // database table directory
    │        └── users.db                           // Database file for Users table
    ├── README.txt                                  // README
    └── setup.py                                    // Installation file


Installation:
    - Clone repository from github at:
        https://github.com/MUN-CS2005/codesender-project-gteam
    - In terminal, navigate to the codesender-project-gteam directory
    - Once inside the codesender-project-gteam directory, initialize a virtual environment with command:
        ~$ virtualenv -p python3 env
    - Activate the virtual environment with the command:
        ~$ source env/bin/activate
    - Run setup.py with command:
        ~$ pip install -e .

Launching the Server:
    - While still inside the virtual environment, launch server with command:
        ~$ start-server
    - Open any web browser and navigate to:
        localhost:5000

Using the application:
    - Type python code into the text area and press "Run" to
      execute the code. You should see the output under the form.
    - To save a code snippet, run your code to ensure it outputs
      correctly. Then press "Save Code Snippet", you should be
      notified in the text area that your code snippet has been
      saved.
    - To retrieve a code snippet, press "Pull Code Snippet". You
      should see the code snippet you saved in the previous step
      displayed above the forms

