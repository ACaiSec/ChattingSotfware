<<<<<<< HEAD
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QHBoxLayout, QVBoxLayout, QMessageBox, QHeaderView, QFontComboBox, QComboBox
from PyQt5.QtCore import pyqtSlot,Qt
=======
>>>>>>> b512c18efcbdcdb949266dfce7de3a701043cd0c
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QComboBox, QFontComboBox,
                             QHBoxLayout, QHeaderView, QMessageBox,
                             QVBoxLayout, QWidget)


class chat_Ui(QWidget):

    def __init__(self):
       
        super().__init__()
        self.initUI()

    def initUI(self):
        
        self.setStyleSheet("#ChatRoom{ background:rgb(255, 255, 255); }")
        self.setObjectName("ChatRoom")
        self.resize(598, 538)
        self.setMinimumSize(588, 528)
        self.setAcceptDrops(False)

        # 定义控件
<<<<<<< HEAD
        self.toolButton_bold = QtWidgets.QToolButton()
=======
        # self.toolButton_font = QtWidgets.QToolButton()
        self.toolButton_image = QtWidgets.QToolButton()
        self.toolButton_file = QtWidgets.QToolButton()
        self.toolButton_1 = QtWidgets.QToolButton()
>>>>>>> b512c18efcbdcdb949266dfce7de3a701043cd0c
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Image/B.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_bold.setIcon(icon1)
        self.toolButton_bold.setIconSize(QtCore.QSize(16, 16))
        self.toolButton_bold.setCheckable(True)
        self.toolButton_bold.setAutoRaise(True)
        self.toolButton_bold.setObjectName("boldToolButton")
        
        self.toolButton_italic = QtWidgets.QToolButton()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Image/I.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_italic.setIcon(icon2)
        self.toolButton_italic.setIconSize(QtCore.QSize(16, 16))
        self.toolButton_italic.setCheckable(True)
        self.toolButton_italic.setAutoRaise(True)
        self.toolButton_italic.setObjectName("italicToolButton")
        
        self.toolButton_underline = QtWidgets.QToolButton()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Image/U.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_underline.setIcon(icon3)
        self.toolButton_underline.setIconSize(QtCore.QSize(16, 16))
        self.toolButton_underline.setCheckable(True)
        self.toolButton_underline.setAutoRaise(True)
        self.toolButton_underline.setObjectName("underlineToolButton")
        
        self.toolButton_color = QtWidgets.QToolButton()
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Image/C.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_color.setIcon(icon4)
        self.toolButton_color.setIconSize(QtCore.QSize(16, 16))
        self.toolButton_color.setCheckable(True)
        self.toolButton_color.setAutoRaise(True)
        self.toolButton_color.setObjectName("colorToolButton")
        
        self.toolButton_image = QtWidgets.QToolButton()
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Image/Image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_image.setIcon(icon5)
        self.toolButton_image.setIconSize(QtCore.QSize(18, 18))
        self.toolButton_image.setCheckable(True)
        self.toolButton_image.setAutoRaise(True)
        self.toolButton_image.setObjectName("imageToolButton")

        self.toolButton_file = QtWidgets.QToolButton()
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Image/File.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_file.setIcon(icon6)
        self.toolButton_file.setIconSize(QtCore.QSize(18, 18))
        self.toolButton_file.setCheckable(True)
        self.toolButton_file.setAutoRaise(True)
        self.toolButton_file.setObjectName("fileToolButton")
        
        self.fontComboBox = QtWidgets.QFontComboBox()
        self.fontComboBox.setObjectName("fontComboBox")
        self.comboBox_size = QtWidgets.QComboBox()
        self.fontComboBox.setMaximumWidth(120)
        self.comboBox_size.setObjectName("sizeComboBox")
        self.comboBox_size.addItem("")
        self.comboBox_size.addItem("")
        self.comboBox_size.addItem("")
        self.comboBox_size.addItem("")
        self.comboBox_size.addItem("")
        self.comboBox_size.addItem("")
        self.comboBox_size.addItem("")
        self.comboBox_size.addItem("")
        self.comboBox_size.addItem("")
        self.comboBox_size.addItem("")
        self.comboBox_size.addItem("")
        self.comboBox_size.addItem("")
        self.comboBox_size.addItem("")
        
        self.pushButton_exit = QtWidgets.QPushButton()
        self.pushButton_exit.setObjectName("exitPushButton")
        self.pushButton_send = QtWidgets.QPushButton()
        self.pushButton_send.setObjectName("sendPushButton")
       
        self.textEdit_send = QtWidgets.QTextEdit()
        self.textEdit_send.setObjectName("sendTextEdit")
        self.textEdit_send.setFocus()
        self.textBrowser_show = QtWidgets.QTextBrowser()
        self.textBrowser_show.setObjectName("showTextBrowser")
        
        self.label_ulist = QtWidgets.QLabel()
        self.label_ulist.setObjectName("ulistLabel")
        self.tableWidget_ulist = QtWidgets.QTableWidget()
        self.tableWidget_ulist.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_ulist.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_ulist.setShowGrid(False)
        self.tableWidget_ulist.setObjectName("tableWidget_ulist")
        self.tableWidget_ulist.setColumnCount(2)
        self.tableWidget_ulist.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ulist.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ulist.setHorizontalHeaderItem(1, item)

        #定义布局
        self.h_box_tool = QHBoxLayout()
        self.h_box_send_exit = QHBoxLayout()
        self.h_box_all = QHBoxLayout()
        self.v_box_right = QVBoxLayout()
        self.v_box_left = QVBoxLayout()
        
        self.layout_ui()
        self.ui_translate()
        QtCore.QMetaObject.connectSlotsByName(self)
  
    def layout_ui(self):
        """
        设置控件布局
        """
<<<<<<< HEAD
        self.h_box_tool.addStretch(1)
        self.h_box_tool.addWidget(self.fontComboBox)
        self.h_box_tool.addWidget(self.comboBox_size)
        self.h_box_tool.addWidget(self.toolButton_bold)
        self.h_box_tool.addWidget(self.toolButton_italic)
        self.h_box_tool.addWidget(self.toolButton_underline)
        self.h_box_tool.addWidget(self.toolButton_color)
        self.h_box_tool.addWidget(self.toolButton_image)
        self.h_box_tool.addWidget(self.toolButton_file)
        self.h_box_send_exit.addStretch(1)
        self.h_box_send_exit.addWidget(self.pushButton_send)
        self.h_box_send_exit.addWidget(self.pushButton_exit)
=======
        self.h_box_1.addStretch(1)
        # self.h_box_1.addWidget(self.toolButton_font)
        self.h_box_1.addWidget(self.toolButton_image)
        self.h_box_1.addWidget(self.toolButton_file)
        self.h_box_font.addStretch(1)
        self.h_box_font.addWidget(self.fontComboBox)
        self.h_box_font.addWidget(self.comboBox_size)
        self.h_box_font.addWidget(self.toolButton_1)
        self.h_box_font.addWidget(self.toolButton_2)
        self.h_box_font.addWidget(self.toolButton_3)
        self.h_box_font.addWidget(self.toolButton_4)
        self.h_box_2.addStretch(1)
        self.h_box_2.addWidget(self.pushButton_send)
        self.h_box_2.addWidget(self.pushButton_exit)
>>>>>>> b512c18efcbdcdb949266dfce7de3a701043cd0c
        self.v_box_left.addWidget(self.textBrowser_show,3)
        self.v_box_left.addLayout(self.h_box_tool)

        self.v_box_left.addWidget(self.textEdit_send,1)
        self.v_box_left.addLayout(self.h_box_send_exit)
        self.v_box_right.addWidget(self.label_ulist)
        self.v_box_right.addWidget(self.tableWidget_ulist)

        self.h_box_all.addLayout(self.v_box_left,2)
        self.h_box_all.addLayout(self.v_box_right,1)
        
        self.setLayout(self.h_box_all)

    def ui_translate(self):
        """
        控件默认文字设置
        """
        self._translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(self._translate("ChatRoom", "ChatRoom"))
        self.comboBox_size.setCurrentText(self._translate("ChatRoom", "9"))
        self.comboBox_size.setItemText(0, self._translate("ChatRoom", "9"))
        self.comboBox_size.setItemText(1, self._translate("ChatRoom", "10"))
        self.comboBox_size.setItemText(2, self._translate("ChatRoom", "11"))
        self.comboBox_size.setItemText(3, self._translate("ChatRoom", "12"))
        self.comboBox_size.setItemText(4, self._translate("ChatRoom", "13"))
        self.comboBox_size.setItemText(5, self._translate("ChatRoom", "14"))
        self.comboBox_size.setItemText(6, self._translate("ChatRoom", "15"))
        self.comboBox_size.setItemText(7, self._translate("ChatRoom", "16"))
        self.comboBox_size.setItemText(8, self._translate("ChatRoom", "17"))
        self.comboBox_size.setItemText(9, self._translate("ChatRoom", "18"))
        self.comboBox_size.setItemText(10, self._translate("ChatRoom", "19"))
        self.comboBox_size.setItemText(11, self._translate("ChatRoom", "20"))
        self.comboBox_size.setItemText(12, self._translate("ChatRoom", "21"))
        self.comboBox_size.setItemText(13, self._translate("ChatRoom", "22"))
        self.toolButton_image.setToolTip(self._translate("ChatRoom", "发送图片"))
        self.toolButton_image.setText(self._translate("ChatRoom", "Image"))
        self.toolButton_file.setToolTip(self._translate("ChatRoom", "发送文件"))
        self.toolButton_file.setText(self._translate("ChatRoom", "File"))
        self.toolButton_bold.setToolTip(self._translate("ChatRoom", "加粗"))
        self.toolButton_bold.setText(self._translate("ChatRoom", "..."))
        self.toolButton_italic.setToolTip(self._translate("ChatRoom", "倾斜"))
        self.toolButton_italic.setText(self._translate("ChatRoom", "..."))
        self.toolButton_underline.setToolTip(self._translate("ChatRoom", "下划线"))
        self.toolButton_underline.setText(self._translate("ChatRoom", "..."))
        self.toolButton_color.setToolTip(self._translate("ChatRoom", "字体颜色"))
        self.toolButton_color.setText(self._translate("ChatRoom", "..."))
        self.pushButton_send.setText(self._translate("ChatRoom", "发送"))
        self.pushButton_exit.setText(self._translate("ChatRoom", "退出"))
        self.textEdit_send.setPlaceholderText("点击此处输入消息..")
        self.label_ulist.setText(self._translate("ChatRoom", "用户列表"))
        item = self.tableWidget_ulist.horizontalHeaderItem(0)
        item.setText(self._translate("ChatRoom", "用户名"))
        item = self.tableWidget_ulist.horizontalHeaderItem(1)
        item.setText(self._translate("ChatRoom", "IP地址"))
        self.tableWidget_ulist.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'QUIT', 'QUIT ?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()        
        else:
            event.ignore()

    @pyqtSlot()
    def on_exitPushButton_clicked(self):
        self.close()
'''
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = example()
    ex.initUI()
    ex.show()
    sys.exit(app.exec_())      
<<<<<<< HEAD
'''

    
=======
>>>>>>> b512c18efcbdcdb949266dfce7de3a701043cd0c
