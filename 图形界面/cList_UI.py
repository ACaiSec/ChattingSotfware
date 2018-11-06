from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import socket
from chatroom_UI import chat_Ui
userlist = [['xx', ('127.0.0.2', 10188), 'xxasd'], ['gx', ('127.0.0.3', 10189), 'xasfeefdfdf'], ['abcd', ('127.4.5.6', 12345), 'sasasa']]
class list_Ui(QWidget):

    def __init__(self):
       
        super().__init__()
        self.username = socket.getfqdn(socket.gethostname())
        self.userip = socket.gethostbyname(self.username)
        self.initUI()

    def initUI(self):

        self.setStyleSheet("#cList{ background:rgb(255, 255, 255); }")
        self.setObjectName("cList")
        self.resize(255, 678)
        self.setMinimumSize(245, 539)
        self.setMaximumSize(280, 768)
        
        self.userInfo = QtWidgets.QLabel()
        self.userInfo.setObjectName("userInfo")
        
        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit.setObjectName("lineEdit")
        
        self.toolButton_search = QtWidgets.QToolButton()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Image/S.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_search.setIcon(icon1)
        self.toolButton_search.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_search.setAutoRaise(True)
        self.toolButton_search.setObjectName("searchButton")
        
        self.toolButton_add = QtWidgets.QToolButton()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Image/A.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_add.setIcon(icon2)
        self.toolButton_add.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_add.setAutoRaise(True)
        self.toolButton_add.setObjectName("addButton")
        
        self.listWidget = QtWidgets.QListWidget()
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet("QListWidget{border:1px solid gray; color:black; }"
                        "QListWidget::Item{padding-top:20px; padding-bottom:4px; }"
                        "QListWidget::Item:hover{background:skyblue; }"
                        "QListWidget::item:selected:!active{border-width:0px; background:lightgreen; }"
                        )
        self.listWidget.itemDoubleClicked.connect(self.listItemDoubleClick)
        for user in userlist:
            u = QListWidgetItem()
            u.username = user[0]
            u.userip = user[1][0]
            u.userport = user[1][1]
            font = QFont()
            font.setPointSize(16)
            u.setText(u.username)
            self.listWidget.addItem(u)            

        self.h_box_search_add = QtWidgets.QHBoxLayout()
        self.h_box_search_add.setObjectName("h_box_search_add")
        self.h_box_search_add.addWidget(self.lineEdit)
        self.h_box_search_add.addWidget(self.toolButton_search)
        self.h_box_search_add.addWidget(self.toolButton_add)
                 
        self.v_box_all = QtWidgets.QVBoxLayout()
        self.v_box_all.setObjectName("v_box_all")
        self.v_box_all.addWidget(self.userInfo)
        self.v_box_all.addLayout(self.h_box_search_add)
        self.v_box_all.addWidget(self.listWidget)

        self.setLayout(self.v_box_all)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self._translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(self._translate("cList", "关注列表"))
        self.userInfo.setText(self._translate("cList", "用户名:{} \nIP:{}".format(self.username, self.userip)))
        self.toolButton_search.setToolTip(self._translate("cList", "查找联系人"))
        self.toolButton_search.setText(self._translate("cList", "..."))
        self.toolButton_add.setToolTip(self._translate("cList", "新增联系人"))
        self.toolButton_add.setText(self._translate("cList", "..."))

    def listItemDoubleClick(self):
        item = self.listWidget.currentItem()
        item.chat = chat_Ui()
        item.chat.tableWidget_ulist.insertRow(0)
        item.chat.tableWidget_ulist.setItem(0,0,QTableWidgetItem(self.username))
        item.chat.tableWidget_ulist.setItem(0,1,QTableWidgetItem(self.userip))
        item.chat.tableWidget_ulist.insertRow(1)
        item.chat.tableWidget_ulist.setItem(1,0,QTableWidgetItem(item.username))
        item.chat.tableWidget_ulist.setItem(1,1,QTableWidgetItem(item.userip + ':' + str(item.userport)))
        item.chat.tableWidget_ulist.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        item.chat.show()    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv) 
    ui = list_Ui()
    ui.show()
    sys.exit(app.exec_())
