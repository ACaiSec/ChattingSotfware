import pickle

class RegisterStructure():
    # 注册
    def __init__(self, username, password, userIP = None):
        self.operation_num = 0
        self.username = username
        self.password = password
        self.userIP = userIP

class LoginStructure():
    # 登录
    def __init__(self, username, password, userIP = None):
        self.operation_num = 1
        self.username = username
        self.password = password
        self.userIP = userIP

class UpdateStructure():
    # 在线检测
    def __init__(self, username, password, hashstring, userIP = None):
        self.operation_num = 3
        self.username = username
        self.password = password
        self.userIP = userIP
        self.hashstring = hashstring

class InfoStructure():
    # 消息传输
    def __init__(self, username, target_user, targetIP, data, userIP = None):
        self.operation_num = 2
        self.username = username
        self.userIP = userIP
        self.target_user = target_user
        self.targetIP = targetIP
        self.data = data



