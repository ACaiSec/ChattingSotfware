from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QMessageBox, QHeaderView

import sys


class example(QWidget):

    signal_write_msg = QtCore.pyqtSignal(str)

    def __init__(self):
       
        super(example, self).__init__()
        self._translate = QtCore.QCoreApplication.translate

        self.setObjectName("ChatRoom")
        self.resize(598, 538)
        self.setMinimumSize(588,528)
        self.setAcceptDrops(False)

        # 定义控件
        self.pushButton_1 = QtWidgets.QPushButton()
        self.pushButton_2 = QtWidgets.QPushButton()
        self.pushButton_exit = QtWidgets.QPushButton()
        self.pushButton_send = QtWidgets.QPushButton()

       
        self.textEdit_send = QtWidgets.QTextEdit()
        self.textBrowser_show = QtWidgets.QTextBrowser()
        self.label_ulist = QtWidgets.QLabel()

        self.tableWidget_ulist = QtWidgets.QTableWidget()
        self.tableWidget_ulist.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_ulist.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_ulist.setShowGrid(False)
        self.tableWidget_ulist.setObjectName("tableWidget_ulist")
        self.tableWidget_ulist.setColumnCount(3)
        self.tableWidget_ulist.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ulist.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ulist.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ulist.setHorizontalHeaderItem(2, item)

        #定义布局
        self.h_box_1 = QHBoxLayout()
        self.h_box_2 = QHBoxLayout()
        self.h_box_all = QHBoxLayout()
        self.v_box_es = QVBoxLayout()
        self.v_box_right = QVBoxLayout()
        self.v_box_left = QVBoxLayout()

        self.textEdit_send.setFocus()
        
        self.layout_ui()
        self.ui_translate()
        self.connect()
    
    def layout_ui(self):
        """
        设置控件布局
        """
        self.v_box_es.addWidget(self.pushButton_send)
        self.v_box_es.addWidget(self.pushButton_exit)
        self.h_box_1.addStretch(1)
        self.h_box_1.addWidget(self.pushButton_1)
        self.h_box_1.addWidget(self.pushButton_2)
        self.h_box_2.addStretch(1)
        self.h_box_2.addLayout(self.v_box_es)
        self.v_box_left.addWidget(self.textBrowser_show,3)
        self.v_box_left.addLayout(self.h_box_1)
        self.v_box_left.addWidget(self.textEdit_send,1)
        self.v_box_left.addLayout(self.h_box_2)
        self.v_box_right.addWidget(self.label_ulist)
        self.v_box_right.addWidget(self.tableWidget_ulist)

        self.h_box_all.addLayout(self.v_box_left,3)
        self.h_box_all.addLayout(self.v_box_right,1)
        
        self.setLayout(self.h_box_all)

    def ui_translate(self):
        """
        控件默认文字设置
        """
        self.setWindowTitle(self._translate("ChatRoom", "ChatRoom"))
        self.pushButton_1.setText(self._translate("ChatRoom", "工具1"))
        self.pushButton_2.setText(self._translate("ChatRoom", "工具2"))
        self.pushButton_send.setText(self._translate("ChatRoom", "发送"))
        self.pushButton_exit.setText(self._translate("ChatRoom", "退出"))
        self.textEdit_send.setPlaceholderText("点击此处输入消息..")
        self.label_ulist.setText(self._translate("ChatRoom", "用户列表"))
        item = self.tableWidget_ulist.horizontalHeaderItem(0)
        item.setText(self._translate("ChatRoom", "用户名"))
        item = self.tableWidget_ulist.horizontalHeaderItem(1)
        item.setText(self._translate("ChatRoom", "IP地址"))
        item = self.tableWidget_ulist.horizontalHeaderItem(2)
        item.setText(self._translate("ChatRoom", "端口号"))
        self.tableWidget_ulist.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def connect(self):
        """
        控件信号-槽的设置
        """
        self.signal_write_msg.connect(self.write_msg)
        self.pushButton_exit.clicked.connect(QtCore.QCoreApplication.instance().quit)
    
    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'QUIT', 'QUIT ?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()        
        else:
            event.ignore()
    
    def write_msg(self, msg):
        # signal_write_msg信号会触发这个函数
        """
        功能函数，向接收区写入数据的方法
        信号-槽触发
        """
        self.textBrowser_send.insertPlainText(msg)
        self.textBrowser_send.moveCursor(QtGui.QTextCursor.End)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = example()
    ex.show()
    app.exec_()      


    
