import sys

from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
                             QPushButton, QWidget, QCheckBox, QFormLayout,
                             QVBoxLayout)


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        user_name = QLabel('账号')
        passWord = QLabel('密码')

        userEdit = QLineEdit()
        passEdit = QLineEdit()

        rem_password = QCheckBox('记住密码')
        auto_login = QCheckBox('自动登录')

        login = QPushButton('登录')

        self.input_Field = QFormLayout()
        self.input_Field.setWidget(0, QFormLayout.LabelRole, user_name)
        self.input_Field.setWidget(0, QFormLayout.FieldRole, userEdit)
        self.input_Field.setWidget(1, QFormLayout.LabelRole, passWord)
        self.input_Field.setWidget(1, QFormLayout.FieldRole, passEdit)

        self.checkpoint = QHBoxLayout()
        self.checkpoint.addWidget(rem_password)
        self.checkpoint.addWidget(auto_login)

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.input_Field)
        self.main_layout.addLayout(self.checkpoint)
        self.main_layout.addWidget(login)

        self.setLayout(self.main_layout)
        self.setFixedSize(350, 135)
        self.setWindowTitle('login')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('WindowsVista')
    ex = Example()
    sys.exit(app.exec_())
