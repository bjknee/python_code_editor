import shelve as sh

"""
Author: Kayla Malcolm
Group: G Team
Date: November 2, 2022
The following code uses Shelve in order to store client information when using codeServer application,
so that user information can be retrieved on re-launching the application or requesting stored information
"""


class serverStorage:
    def checkUser(self, usrname):
        server = sh.open("codeServerDB.txt", flag='r', protocol=None, writeback=False)
        found_user = False
        while found_user is False:
            for key in server.keys():
                if server['username'] == usrname:
                    found_user = True
                else:
                    found_user = False
        server.close()
        return found_user

    def storeCode(self, usrCode, usr="admin", tag=None):
        # will remove admin default in later submission
        store = sh.open("codeServerDB.txt", flag='c', protocol=None, writeback=False)
        store['username'] = usr
        store['code segment'] = usrCode
        store.close()

    def retrieveCode(self, usr="admin", tag=None):
        # will remove admin default in later submission
        retrieve = sh.open("codeServerDB.txt", flag='c', protocol=None, writeback=False)
        code_snippet = retrieve['code segment']
        retrieve.close()
        return code_snippet
