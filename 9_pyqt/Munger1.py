# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Munger.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QAxContainer import *

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        # 제목
        MainWindow.setWindowTitle('Munger version-22.0.1')
        # MainWindow.setObjectName("Munger version-22.0.1")
        MainWindow.resize(968, 599)
        # self.MainWindow.setText(_translate("MainWindow", "combobox 연관"))
        # 아이콘
        self.setWindowIcon(QIcon('c:/workspace/Munger/PyQt/Owlicon.png'))
        self.setGeometry(300,300,300,200)

        # 날짜 date 정의
        self.date = QDate.currentDate()
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 250, 241, 51))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(540, 20, 101, 16))
        self.label_13.setObjectName("label_13")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(530, 50, 401, 441))
        self.textBrowser.setObjectName("textBrowser")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 463, 74))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 0, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 7, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_10.setEnabled(False)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 0, 8, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 2, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 1, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 4, 1, 2)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 1, 6, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 7, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_11.setEnabled(False)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout.addWidget(self.lineEdit_11, 1, 8, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 2, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_8.setEnabled(False)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 2, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 4, 1, 2)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_9.setEnabled(False)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 2, 6, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 7, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_12.setEnabled(False)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout.addWidget(self.lineEdit_12, 2, 8, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 0, 6, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 968, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuOption = QtWidgets.QMenu(self.menubar)
        self.menuOption.setObjectName("menuOption")
        MainWindow.setMenuBar(self.menubar)
        
        # 상태창 날짜 띄우기
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate)) # 날짜표시
        #self.statusbar = QtWidgets.QStatusBar(MainWindow)
        #self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)
        
        # 메뉴바
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")

        # 닫기 창 
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        CloseAction = QAction(QIcon('c:/workspace/Munger/PyQt/exit.png'), 'Exit', self)
        CloseAction.setShortcut('Ctrl+Q')
        CloseAction.setStatusTip('Close application')
        CloseAction.triggered.connect(qApp.quit)

        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuOption.menuAction())
    
        self.retranslateUi(MainWindow)
        self.lineEdit.textChanged.connect(self.setDollarIndex)
        self.lineEdit_2.textChanged.connect(self.setUS10Y)
        self.lineEdit_3.textChanged.connect(self.setUS2Y)
        self.lineEdit_4.textChanged.connect(self.setCrudeOIi)
        self.lineEdit_6.textChanged.connect(self.setGold)
        self.lineEdit_8.textChanged.connect(self.setVix)
        self.lineEdit_5.textChanged.connect(self.setSNP500)
        self.lineEdit_7.textChanged.connect(self.setNasdaq)
        self.lineEdit_9.textChanged.connect(self.setRussell)
        self.lineEdit_10.textChanged.connect(self.setBitcoin)
        self.lineEdit_11.textChanged.connect(self.setEthereum)
        self.lineEdit_12.textChanged.connect(self.setKOSPI)
        self.comboBox.highlighted.connect(self.setClick)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "KOSPI 저 PER 종목"))
        self.comboBox.setItemText(1, _translate("MainWindow", "KOSPI 저 PBR 종목"))
        self.comboBox.setItemText(2, _translate("MainWindow", "KOSPI 저 PSR 종목"))
        self.comboBox.setItemText(3, _translate("MainWindow", "KOSPI 저 PCR 종목"))
        self.comboBox.setItemText(4, _translate("MainWindow", "KOSDAQ 저 PER 종목"))
        self.comboBox.setItemText(5, _translate("MainWindow", "KOSDAQ 저 PBR 종목"))
        self.comboBox.setItemText(6, _translate("MainWindow", "KOSDAQ 저 PSR 종목"))
        self.comboBox.setItemText(7, _translate("MainWindow", "KOSDAQ 저 PCR 종목"))
        self.comboBox.setItemText(8, _translate("MainWindow", "ROE 지수 5개년 11이상 종목"))
        self.comboBox.setItemText(9, _translate("MainWindow", "반도체 뉴스 감성분석"))
        self.comboBox.setItemText(10, _translate("MainWindow", "시뮬레이션(미래주가흐름)"))
        self.label_13.setText(_translate("MainWindow", "combobox 연관"))
        self.label_3.setText(_translate("MainWindow", "Dollar Index"))
        self.label_6.setText(_translate("MainWindow", "WTI"))
        self.label_12.setText(_translate("MainWindow", "S&P500"))
        self.label_4.setText(_translate("MainWindow", "Bitcoin"))
        self.label_5.setText(_translate("MainWindow", "U.S. 10Y:"))
        self.label_8.setText(_translate("MainWindow", "Gold"))
        self.label_9.setText(_translate("MainWindow", "Nasdaq"))
        self.label_7.setText(_translate("MainWindow", "Ethereum"))
        self.label_2.setText(_translate("MainWindow", "U.S. 2Y:"))
        self.label.setText(_translate("MainWindow", "VIX"))
        self.label_11.setText(_translate("MainWindow", "Rusell2000"))
        self.label_10.setText(_translate("MainWindow", "KOSPI"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuOption.setTitle(_translate("MainWindow", "Option"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
    
    def setDollarIndex(self):
        pass
    
    def setUS10Y(self):
        pass
    
    def setUS2Y(self):
        pass
    
    def setCrudeOIi(self):
        pass
    
    def setGold(self):
        pass
    
    def setVix(self):
        pass
    
    def setSNP500(self):
        pass
    
    def setNasdaq(self):
        pass
    
    def setRussell(self):
        pass
    
    def setBitcoin(self):
        pass
    
    def setEthereum(self):
        pass
    
    def setKOSPI(self):
        pass
    def setClick(self):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

