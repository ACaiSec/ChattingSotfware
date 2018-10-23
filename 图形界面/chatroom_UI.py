from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QMessageBox, QHeaderView, QFontComboBox, QComboBox
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
        #self.toolButton_font = QtWidgets.QToolButton()
        self.toolButton_image = QtWidgets.QToolButton()
        self.toolButton_file = QtWidgets.QToolButton()
        self.toolButton_1 = QtWidgets.QToolButton()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Image/B.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_1.setIcon(icon1)
        self.toolButton_1.setIconSize(QtCore.QSize(16, 16))
        self.toolButton_1.setCheckable(True)
        self.toolButton_1.setAutoRaise(True)
        self.toolButton_1.setObjectName("boldToolButton")
        self.toolButton_2 = QtWidgets.QToolButton()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Image/I.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon2)
        self.toolButton_2.setIconSize(QtCore.QSize(16, 16))
        self.toolButton_2.setCheckable(True)
        self.toolButton_2.setAutoRaise(True)
        self.toolButton_2.setObjectName("italicToolButton")
        self.toolButton_3 = QtWidgets.QToolButton()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Image/U.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon3)
        self.toolButton_3.setIconSize(QtCore.QSize(16, 16))
        self.toolButton_3.setCheckable(True)
        self.toolButton_3.setAutoRaise(True)
        self.toolButton_3.setObjectName("underlineToolButton")
        self.toolButton_4 = QtWidgets.QToolButton()
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Image/C.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon4)
        self.toolButton_4.setIconSize(QtCore.QSize(16, 16))
        self.toolButton_4.setCheckable(True)
        self.toolButton_4.setAutoRaise(True)
        self.toolButton_4.setObjectName("colorToolButton")
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
        self.h_box_font = QHBoxLayout()
        self.h_box_all = QHBoxLayout()
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
        self.h_box_1.addStretch(1)
        #self.h_box_1.addWidget(self.toolButton_font)
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
        self.v_box_left.addWidget(self.textBrowser_show,3)
        self.v_box_left.addLayout(self.h_box_font)
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
        #self.toolButton_font.setToolTip(self._translate("ChatRoom", "字体"))
        #self.toolButton_font.setText(self._translate("ChatRoom", "A"))
        self.toolButton_image.setToolTip(self._translate("ChatRoom", "发送图片"))
        self.toolButton_image.setText(self._translate("ChatRoom", "Image"))
        self.toolButton_file.setToolTip(self._translate("ChatRoom", "发送文件"))
        self.toolButton_file.setText(self._translate("ChatRoom", "File"))
        self.toolButton_1.setToolTip(self._translate("ChatRoom", "加粗"))
        self.toolButton_1.setText(self._translate("ChatRoom", "..."))
        self.toolButton_2.setToolTip(self._translate("ChatRoom", "倾斜"))
        self.toolButton_2.setText(self._translate("ChatRoom", "..."))
        self.toolButton_3.setToolTip(self._translate("ChatRoom", "下划线"))
        self.toolButton_3.setText(self._translate("ChatRoom", "..."))
        self.toolButton_4.setToolTip(self._translate("ChatRoom", "字体颜色"))
        self.toolButton_4.setText(self._translate("ChatRoom", "..."))
        self.pushButton_send.setText(self._translate("ChatRoom", "发送"))
        self.pushButton_exit.setText(self._translate("ChatRoom", "退出"))
        self.textEdit_send.setPlaceholderText("点击此处输入消息..")
        self.label_ulist.setText(self._translate("ChatRoom", "用户列表"))
        item = self.tableWidget_ulist.horizontalHeaderItem(0)
        item.setText(self._translate("ChatRoom", "用户名"))
        item = self.tableWidget_ulist.horizontalHeaderItem(1)
        item.setText(self._translate("ChatRoom", "主机名"))
        item = self.tableWidget_ulist.horizontalHeaderItem(2)
        item.setText(self._translate("ChatRoom", "IP地址"))
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
    sys.exit(app.exec_())      


    
