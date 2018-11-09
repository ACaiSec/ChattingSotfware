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

class InfoStructure():
    # 消息传输
    def __init__(self, username, target_user, targetIP, data, userIP = None):
        self.operation_num = 2
        self.username = username
        self.userIP = userIP
        self.target_user = target_user
        self.targetIP = targetIP
        self.data = data

class UpdateStructure():
    # 在线检测
    def __init__(self, username, password, hashstring, userIP=None):
        self.operation_num = 3
        self.username = username
        self.password = password
        self.userIP = userIP
        self.hashstring = hashstring

class Focus():
    # 关注
    def __init__(self, username, target_user, userIP = None):
        self.operation_num = 4
        self.username = username
        self.userIP = userIP
        self.target_user = target_user

class Verify():
    # 对操作的确认
    def __init__(self, operation_num, verify):
        self.operation_num = operation_num
        self.verify = bool(verify)
class relogin():
    # 重复登录
    def __init__(self):
        self.operation_num = 6

class loopcheck():
    # 状态检测包
    def __init__(self):
        self.operation_num = 7

class attention():
    # 广播关注列表
    def __init__(self, attention):
        self.operation_num = 8
        self.attentionlist = attention

