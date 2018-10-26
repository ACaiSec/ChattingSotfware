import sys

from PyQt5.QtCore import QEvent, QRegExp, Qt
from PyQt5.QtGui import QKeyEvent, QKeySequence, QRegExpValidator
from PyQt5.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
                             QLineEdit, QMessageBox, QPushButton, QVBoxLayout,
                             QWidget)
from Client2 import *



class Register(QWidget):
    '''注册界面'''
    def __init__(self, client):
        super().__init__()
        self.client = client
        self.initUI()

    def initUI(self):

        # 创建控件
        self.userName = QLabel('账号')
        self.userEdit = QLineEdit()
        self.password = QLabel('密码')
        self.passEdit = QLineEdit()
        self.confirmPassword = QLabel('确认密码')
        self.confirmPassEdit = QLineEdit()
        self.register = QPushButton('注册')

        # 依旧是密码输入框的骚操作，后面重构会单独处理成一个类
        # 为两个密码输入框建立事件过滤器
        self.passEdit.installEventFilter(self.passEdit)
        self.confirmPassEdit.installEventFilter(self.confirmPassEdit)
        # 暂不确定是否需要屏蔽输入框的选中，暂时省略
        pass
        # 设置输入框中的提示文本
        self.passEdit.setPlaceholderText('')
        self.confirmPassEdit.setPlaceholderText('')
        # 将密码显示为圆黑点
        self.passEdit.setEchoMode(QLineEdit.Password)
        self.confirmPassEdit.setEchoMode(QLineEdit.Password)
        # 运用正则表示限定密码输入框字符的接收条件
        regx = QRegExp("^[a-zA-Z][0-9A-Za-z]{14}$")
        validator1 = QRegExpValidator(regx, self.passEdit)
        self.passEdit.setValidator(validator1)
        validator2 = QRegExpValidator(regx, self.confirmPassEdit)
        self.passEdit.setValidator(validator2)

        # 设置布局
        # 设置上方的表单布局
        self.inputLayout = QFormLayout()
        self.inputLayout.setWidget(0, QFormLayout.LabelRole, self.userName)
        self.inputLayout.setWidget(0, QFormLayout.FieldRole, self.userEdit)
        self.inputLayout.setWidget(1, QFormLayout.LabelRole, self.password)
        self.inputLayout.setWidget(1, QFormLayout.FieldRole, self.passEdit)
        self.inputLayout.setWidget(2, QFormLayout.LabelRole, self.confirmPassword)
        self.inputLayout.setWidget(2, QFormLayout.FieldRole, self.confirmPassEdit)

        self.registerLayout = QHBoxLayout()
        self.registerLayout.addWidget(self.register)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.inputLayout)
        self.mainLayout.addLayout(self.registerLayout)

        self.register.clicked.connect(self.buttonclicked)

        self.setLayout(self.mainLayout)
        self.setFixedSize(350, 135)
        self.setWindowTitle('注册账号')       

    def eventFilter(self, object, event):
        if object == self.passEdit or object == self.confirmPassEdit:
            if event.type() == QEvent.MouseMove or event.type() == QEvent.MouseButtonDblClick:
                return True
            elif event.type() == QEvent.KeyPress:
                key = QKeyEvent(event)
                if key.matches(QKeySequence.SelectAll) or key.matches(QKeySequence.Copy):
                    return True
        return super().eventFilter(self, object, event)

    def buttonclicked(self):
        '''注册按键事件'''
        if not self.userEdit.text():
            # 如果注册用户名为空
            QMessageBox.information(self, '注册失败', '用户名不能为空')
        elif len(self.passEdit.text()) < 6:
            # 如果密码长度小于6
            QMessageBox.information(self, '注册失败', '密码长度过短')
        elif self.passEdit.text() != self.confirmPassEdit.text():
            # 两次密码不一致
            QMessageBox.information(self, '注册失败', '两次输入密码不一致')
        else:
            signal = self.client.Register(userEdit.text(),passEdit.text())
            if signal:
                # 返回值为真
                QMessageBox.about(self, '注册成功', '欢迎使用本聊天室')
                self.close()
            else:
                QMessageBox.information(self, '注册失败', '该用户名已被占用！')
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('WindowsVista')
    ex = Register()
    sys.exit(app.exec_())
