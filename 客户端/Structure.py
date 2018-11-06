import pickle


class RegisterStructure:
    # 注册
    def __init__(self, username, password, userIP=None):
        self.operation_num = 0
        self.username = username
        self.password = password
        self.userIP = userIP


class LoginStructure:
    # 登录
    def __init__(self, username, password, userIP=None):
        self.operation_num = 1
        self.username = username
        self.password = password
        self.userIP = userIP


class InfoStructure:
    # 消息传输
    def __init__(self, username, target_user, data, targetIP=None, userIP=None):
        self.operation_num = 2
        self.username = username
        self.userIP = userIP
        self.target_user = target_user
        self.targetIP = targetIP
        self.data = data


if __name__ == '__main__':
    i = RegisterStructure('123', '456')
    ii = pickle.dumps(i)
    print(type(ii))
    print(ii)

    k = pickle.loads(ii)
    print(type(k))
    print(k)
    print(k.username, k.password)
    '''
    i = InfoStructure('xuxu', 'xx', 'halou')
    ii = pickle.dumps(i)
    print(type(ii))
    print(ii)

    k = pickle.loads(ii)
    print(type(k))
    print(k.username, k.target_user, k.data)

    l = LoginStructure('123', '43434')
    print(l.operation_num)
    print(l.username)
    '''
