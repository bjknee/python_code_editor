import shelve as sh

"""
The following code uses Shelf in order to store client information when using codeServer application,
so that user information can be retrieved on re-launching the application
"""


class serverStorage(sh):
    def checkUser(self, usrname, passkey):
        server = sh.open("codeServerDB.txt", flag='r', protocol=None, writeback=False)
        found_user = False
        while found_user is False:
            for key in server.keys():
                if server['username'] == usrname and server['password'] == passkey:
                    found_user = True
                else:
                    found_user = False
        return found_user

    def removeUser(self, usrname):
        pass

    def storeCode(self, usr, usrCode, tag=None):
        store = sh.open("codeServerDB.txt", flag='c', protocol=None, writeback=False)
        store['username'] = usr
        store['code segment'] = usrCode
        store.close()

    def retrieveCode(self, usr, tag=None):
        pass

