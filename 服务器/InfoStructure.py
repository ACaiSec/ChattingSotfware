import pickle

class Register():
    # 注册
    def __init__(self, username, password):
        self.operation_num = 0
        self.username = username
        self.password = password

class LoginStructure(Register):
    # 登录
    def __init__(self, username, password):
        super().__init__(username, password)
        self.operation_num = 1
        '''
        self.username = username
        self.password = password
        '''

class InfoStructure():
    # 消息传输
    def __init__(self, username, userIP, target_user, targetIP, data):
        self.operation_num = 2
        self.username = username
        self.userIP = userIP
        self.target_user = target_user
        self.targetIP = targetIP
        self.data = data



if __name__ == '__main__':
    i = InfoStructure('xuxu', 'xx', 'halou')
    ii = pickle.dumps(i)
    print(type(ii))
    print(ii)

    k = pickle.loads(ii)
    print(type(k))
    print(k.username, k.target_user, k.data)

    l = LoginStructure('123', '43434')
    print(l.operation_num)