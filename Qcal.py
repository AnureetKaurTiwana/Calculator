# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qcal.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(389, 230)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(30, 40, 308, 20))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Edit3 = QtWidgets.QLineEdit(self.widget)
        self.Edit3.setObjectName("Edit3")
        self.gridLayout.addWidget(self.Edit3, 0, 4, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 3, 1, 1)
        self.Edit1 = QtWidgets.QLineEdit(self.widget)
        self.Edit1.setObjectName("Edit1")
        self.gridLayout.addWidget(self.Edit1, 0, 0, 1, 1)
        self.Edit2_2 = QtWidgets.QLineEdit(self.widget)
        self.Edit2_2.setObjectName("Edit2_2")
        self.gridLayout.addWidget(self.Edit2_2, 0, 2, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(120, 110, 158, 25))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Clear = QtWidgets.QPushButton(self.widget1)
        self.Clear.setObjectName("Clear")
        self.horizontalLayout.addWidget(self.Clear)
        self.Calc = QtWidgets.QPushButton(self.widget1)
        self.Calc.setObjectName("Calc")
        self.horizontalLayout.addWidget(self.Calc)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 389, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.Clear.clicked.connect(self.Edit1.clear)
        self.Clear.clicked.connect(self.Edit3.clear)
        self.Clear.clicked.connect(self.Edit2_2.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.Calc.clicked.connect(self.cal)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "+"))
        self.comboBox.setItemText(1, _translate("MainWindow", "-"))
        self.comboBox.setItemText(2, _translate("MainWindow", "/"))
        self.comboBox.setItemText(3, _translate("MainWindow", "*"))
        self.label.setText(_translate("MainWindow", "="))
        self.Clear.setText(_translate("MainWindow", "clear"))
        self.Calc.setText(_translate("MainWindow", "calculate"))
    def cal(self):
        a=self.Edit1.text()
        b=self.Edit2_2.text()
        operator=self.comboBox.currentText()
        try:
            c=eval(a+ operator + b)
            self.Edit3.setText(str(c))
            self.Clear.setText('done')
        except:
            QtWidgets.QMessageBox.critical(MainWindow,'Error','invalid inputs',
            QtWidgets.QMessageBox.Ok)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
