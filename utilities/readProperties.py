import configparser

config = configparser.ConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info','username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info','password')
        return password

    @staticmethod
    def setUser():
        user = config.get('common info','user')
        return user

    @staticmethod
    def setRole():
        role = config.get('common info', 'role')
        return role

    @staticmethod
    def setAddNewRole():
        newRole = config.get('common info', 'addNewRole')
        return newRole

    @staticmethod
    def setNewUserStatus():
        newStatus = config.get('common info', 'AddNewUserStatus')
        return newStatus

    @staticmethod
    def getNewUserPassword():
        newPassword = config.get('common info', 'newUserPassword')
        return newPassword

    @staticmethod
    def getNewEmployeeName():
        newEmployeeName = config.get('common info', 'newEmployeeName')
        return newEmployeeName

    @staticmethod
    def getNewUserName():
        newUserName = config.get('common info', 'newUserName')
        return newUserName

    @staticmethod
    def getNewUserConfirmPwd():
        newUserConfirmPwd = config.get('common info', 'newUserConfirmPwd')
        return newUserConfirmPwd