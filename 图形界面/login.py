import sys

from PyQt5.QtCore import QEvent, QRegExp, Qt
from PyQt5.QtGui import QKeyEvent, QKeySequence, QRegExpValidator
from PyQt5.QtWidgets import (QApplication, QCheckBox, QDialog, QFormLayout,
                             QHBoxLayout, QLabel, QLineEdit, QPushButton,
                             QVBoxLayout, QWidget, QMessageBox)
from register import Register


class Login(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        '''创建界面'''

        # 生成控件实例
        self.user_name = QLabel('账号')
        self.passWord = QLabel('密码')
        self.userEdit = QLineEdit()
        self.passEdit = QLineEdit()
        self.rem_password = QCheckBox('记住密码')
        self.auto_login = QCheckBox('自动登录')
        self.login = QPushButton('登录')
        self.register = QPushButton('注册')
        self.clean = QPushButton('清除')

        # 按键连接到信号槽
        self.clean.clicked.connect(self.cleanPassword)

        # 设置账户输入框的提示文本
        self.userEdit.setPlaceholderText('还没有账号？请按左边。')
        # 密码输入框的骚操作
        # 为密码输入框安装事件过滤器
        self.passEdit.installEventFilter(self.passEdit)
        # 屏蔽密码输入框的选中
        self.passEdit.setContextMenuPolicy(Qt.NoContextMenu)
        # 设置输入框中的提示文本
        self.passEdit.setPlaceholderText('6~15位的密码')
        # 将密码显示为圆黑点
        self.passEdit.setEchoMode(QLineEdit.Password)
        # 运用正则表达式限定密码输入框字符接收的条件
        regx = QRegExp("^[a-zA-Z][0-9A-Za-z]{14}$")
        validator = QRegExpValidator(regx, self.passEdit)
        self.passEdit.setValidator(validator)

        # 生成一个表单布局
        self.input_Field = QFormLayout()
        self.input_Field.setWidget(0, QFormLayout.LabelRole, self.user_name)
        self.input_Field.setWidget(0, QFormLayout.FieldRole, self.userEdit)
        self.input_Field.setWidget(1, QFormLayout.LabelRole, self.passWord)
        self.input_Field.setWidget(1, QFormLayout.FieldRole, self.passEdit)

        # 生成一个容纳注册按钮和清楚密码按钮的垂直布局
        self.buttonLayout = QVBoxLayout()
        self.buttonLayout.addWidget(self.register)
        self.buttonLayout.addWidget(self.clean)

        # pass
        self.inputLayout = QHBoxLayout()
        self.inputLayout.addLayout(self.input_Field)
        self.inputLayout.addLayout(self.buttonLayout)

        # 生成一个容纳复选框的水平布局
        self.checkpoint = QHBoxLayout()
        self.checkpoint.addWidget(self.rem_password)
        self.checkpoint.addWidget(self.auto_login)

        # 主布局，用来容纳前面所有的子布局
        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.inputLayout)
        self.main_layout.addLayout(self.checkpoint)
        self.main_layout.addWidget(self.login)

        self.setLayout(self.main_layout)
        # 锁定界面大小
        self.setFixedSize(350, 135)
        # 设置窗口标题
        self.setWindowTitle('login')
        # 显示窗口
        self.userEdit.setFocus()

    def eventFilter(self, Object, event):
        if Object == self.passEdit:
            if event.type() == QEvent.MouseMove or event.type() == QEvent.MouseButtonDblClick:
                return True
            elif event.type() == QEvent.KeyPress:
                key = QKeyEvent(event)
                if key.matches(QKeySequence.SelectAll) or key.matches(QKeySequence.Copy):
                    return True
        return super().eventFilter(self, Object, QEvent)

    def cleanPassword(self):
        self.passEdit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('WindowsVista')
    ex = Login()
    ex.show()
    sys.exit(app.exec_())
