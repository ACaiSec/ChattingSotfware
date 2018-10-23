import sys

from PyQt5.QtCore import QEvent, QRegExp, Qt
from PyQt5.QtGui import QKeyEvent, QKeySequence, QRegExpValidator
from PyQt5.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
                             QLineEdit, QPushButton, QVBoxLayout, QWidget)


class Register(QWidget):
    '''注册界面'''
    def __init__(self):
        super().__init__()
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

        self.setLayout(self.mainLayout)
        self.setFixedSize(350, 135)
        self.setWindowTitle('注册账号')
        self.show()        

    def eventFilter(self, object, event):
        if object == self.passEdit or object == self.confirmPassEdit:
            if event.type() == QEvent.MouseMove or event.type() == QEvent.MouseButtonDblClick:
                return True
            elif event.type() == QEvent.KeyPress:
                key = QKeyEvent(event)
                if key.matches(QKeySequence.SelectAll) or key.matches(QKeySequence.Copy):
                    return True
        return super().eventFilter(self, object, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('WindowsVista')
    ex = Register()
    sys.exit(app.exec_())

