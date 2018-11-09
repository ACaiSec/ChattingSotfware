from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QListWidgetItem, QHBoxLayout, QVBoxLayout, QTableWidgetItem, QWidget, QHeaderView,QMessageBox
from PyQt5.QtGui import QFont
import socket
from chatroom_UI import chat_Ui

class list_Ui(QWidget):


    def __init__(self, username):
       
        super().__init__()
        self.username = username
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
        icon1.addPixmap(QtGui.QPixmap("./Image/S.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_search.setIcon(icon1)
        self.toolButton_search.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_search.setAutoRaise(True)
        self.toolButton_search.setObjectName("searchButton")
        
        self.toolButton_add = QtWidgets.QToolButton()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./Image/A.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.userInfo.setText(self._translate("cList", "用户名:{} \n".format(self.username)))
        self.toolButton_search.setToolTip(self._translate("cList", "查找联系人"))
        self.toolButton_search.setText(self._translate("cList", "..."))
        self.toolButton_add.setToolTip(self._translate("cList", "新增联系人"))
        self.toolButton_add.setText(self._translate("cList", "..."))

    def addConcern(self, user):
        u = QListWidgetItem()
        u.chat = chat_Ui(user)
        font = QFont()
        font.setPointSize(16)
        u.setText(user)
        u.chat.tableWidget_ulist.insertRow(0)
        u.chat.tableWidget_ulist.setItem(0,0,QTableWidgetItem(self.username))
        u.chat.tableWidget_ulist.insertRow(1)
        u.chat.tableWidget_ulist.setItem(1,0,QTableWidgetItem(user))
        u.chat.tableWidget_ulist.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.listWidget.addItem(u)
    
    def listItemDoubleClick(self):
        item = self.listWidget.currentItem()
        item.chat.show()    

    def searchuser(self, username):
        if isinstance(username, str):
           for row in range(self.listWidget.count()):
                if self.listWidget.item(row).text() == username:
                    return row        
        return -1

    @pyqtSlot()
    def on_searchButton_clicked(self):
        username = self.lineEdit.text()
        if len(username) > 0:
            useritemrow = self.searchuser(username)
            if useritemrow >= 0:
                self.listWidget.setCurrentRow(useritemrow)
            else :
                QMessageBox.critical(self, "Notice", "查无此人", QMessageBox.Ok)
        self.lineEdit.clear()
        self.lineEdit.setFocus()

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv) 
    ui = list_Ui()
    ui.show()
    sys.exit(app.exec_())
