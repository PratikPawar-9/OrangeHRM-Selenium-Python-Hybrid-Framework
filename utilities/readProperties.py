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