# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './pyqtgraph/console/template.ui'
#
# Created: Mon Dec 23 10:10:53 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(710, 497)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.output = QtGui.QPlainTextEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.output.setFont(font)
        self.output.setReadOnly(True)
        self.output.setObjectName("output")
        self.verticalLayout.addWidget(self.output)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.input = CmdInput(self.layoutWidget)
        self.input.setObjectName("input")
        self.horizontalLayout.addWidget(self.input)
        self.historyBtn = QtGui.QPushButton(self.layoutWidget)
        self.historyBtn.setCheckable(True)
        self.historyBtn.setObjectName("historyBtn")
        self.horizontalLayout.addWidget(self.historyBtn)
        self.exceptionBtn = QtGui.QPushButton(self.layoutWidget)
        self.exceptionBtn.setCheckable(True)
        self.exceptionBtn.setObjectName("exceptionBtn")
        self.horizontalLayout.addWidget(self.exceptionBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.historyList = QtGui.QListWidget(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.historyList.setFont(font)
        self.historyList.setObjectName("historyList")
        self.exceptionGroup = QtGui.QGroupBox(self.splitter)
        self.exceptionGroup.setObjectName("exceptionGroup")
        self.gridLayout_2 = QtGui.QGridLayout(self.exceptionGroup)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.catchAllExceptionsBtn = QtGui.QPushButton(self.exceptionGroup)
        self.catchAllExceptionsBtn.setCheckable(True)
        self.catchAllExceptionsBtn.setObjectName("catchAllExceptionsBtn")
        self.gridLayout_2.addWidget(self.catchAllExceptionsBtn, 0, 1, 1, 1)
        self.catchNextExceptionBtn = QtGui.QPushButton(self.exceptionGroup)
        self.catchNextExceptionBtn.setCheckable(True)
        self.catchNextExceptionBtn.setObjectName("catchNextExceptionBtn")
        self.gridLayout_2.addWidget(self.catchNextExceptionBtn, 0, 0, 1, 1)
        self.onlyUncaughtCheck = QtGui.QCheckBox(self.exceptionGroup)
        self.onlyUncaughtCheck.setChecked(True)
        self.onlyUncaughtCheck.setObjectName("onlyUncaughtCheck")
        self.gridLayout_2.addWidget(self.onlyUncaughtCheck, 0, 2, 1, 1)
        self.exceptionStackList = QtGui.QListWidget(self.exceptionGroup)
        self.exceptionStackList.setAlternatingRowColors(True)
        self.exceptionStackList.setObjectName("exceptionStackList")
        self.gridLayout_2.addWidget(self.exceptionStackList, 2, 0, 1, 5)
        self.runSelectedFrameCheck = QtGui.QCheckBox(self.exceptionGroup)
        self.runSelectedFrameCheck.setChecked(True)
        self.runSelectedFrameCheck.setObjectName("runSelectedFrameCheck")
        self.gridLayout_2.addWidget(self.runSelectedFrameCheck, 3, 0, 1, 5)
        self.exceptionInfoLabel = QtGui.QLabel(self.exceptionGroup)
        self.exceptionInfoLabel.setObjectName("exceptionInfoLabel")
        self.gridLayout_2.addWidget(self.exceptionInfoLabel, 1, 0, 1, 5)
        self.clearExceptionBtn = QtGui.QPushButton(self.exceptionGroup)
        self.clearExceptionBtn.setEnabled(False)
        self.clearExceptionBtn.setObjectName("clearExceptionBtn")
        self.gridLayout_2.addWidget(self.clearExceptionBtn, 0, 4, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Console", None, QtGui.QApplication.UnicodeUTF8))
        self.historyBtn.setText(QtGui.QApplication.translate("Form", "History..", None, QtGui.QApplication.UnicodeUTF8))
        self.exceptionBtn.setText(
            QtGui.QApplication.translate("Form", "Exceptions..", None, QtGui.QApplication.UnicodeUTF8)
        )
        self.exceptionGroup.setTitle(
            QtGui.QApplication.translate("Form", "Exception Handling", None, QtGui.QApplication.UnicodeUTF8)
        )
        self.catchAllExceptionsBtn.setText(
            QtGui.QApplication.translate("Form", "Show All Exceptions", None, QtGui.QApplication.UnicodeUTF8)
        )
        self.catchNextExceptionBtn.setText(
            QtGui.QApplication.translate("Form", "Show Next Exception", None, QtGui.QApplication.UnicodeUTF8)
        )
        self.onlyUncaughtCheck.setText(
            QtGui.QApplication.translate("Form", "Only Uncaught Exceptions", None, QtGui.QApplication.UnicodeUTF8)
        )
        self.runSelectedFrameCheck.setText(
            QtGui.QApplication.translate(
                "Form", "Run commands in selected stack frame", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.exceptionInfoLabel.setText(
            QtGui.QApplication.translate("Form", "Exception Info", None, QtGui.QApplication.UnicodeUTF8)
        )
        self.clearExceptionBtn.setText(
            QtGui.QApplication.translate("Form", "Clear Exception", None, QtGui.QApplication.UnicodeUTF8)
        )


from .CmdInput import CmdInput
