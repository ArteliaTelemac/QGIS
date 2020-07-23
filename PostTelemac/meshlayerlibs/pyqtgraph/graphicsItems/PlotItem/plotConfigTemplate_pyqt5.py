# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './pyqtgraph/graphicsItems/PlotItem/plotConfigTemplate.ui'
#
# Created: Wed Mar 26 15:09:28 2014
#      by: PyQt5 UI code generator 5.0.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(481, 840)
        self.averageGroup = QtWidgets.QGroupBox(Form)
        self.averageGroup.setGeometry(QtCore.QRect(0, 640, 242, 182))
        self.averageGroup.setCheckable(True)
        self.averageGroup.setChecked(False)
        self.averageGroup.setObjectName("averageGroup")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.averageGroup)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.avgParamList = QtWidgets.QListWidget(self.averageGroup)
        self.avgParamList.setObjectName("avgParamList")
        self.gridLayout_5.addWidget(self.avgParamList, 0, 0, 1, 1)
        self.decimateGroup = QtWidgets.QFrame(Form)
        self.decimateGroup.setGeometry(QtCore.QRect(10, 140, 191, 171))
        self.decimateGroup.setObjectName("decimateGroup")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.decimateGroup)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.clipToViewCheck = QtWidgets.QCheckBox(self.decimateGroup)
        self.clipToViewCheck.setObjectName("clipToViewCheck")
        self.gridLayout_4.addWidget(self.clipToViewCheck, 7, 0, 1, 3)
        self.maxTracesCheck = QtWidgets.QCheckBox(self.decimateGroup)
        self.maxTracesCheck.setObjectName("maxTracesCheck")
        self.gridLayout_4.addWidget(self.maxTracesCheck, 8, 0, 1, 2)
        self.downsampleCheck = QtWidgets.QCheckBox(self.decimateGroup)
        self.downsampleCheck.setObjectName("downsampleCheck")
        self.gridLayout_4.addWidget(self.downsampleCheck, 0, 0, 1, 3)
        self.peakRadio = QtWidgets.QRadioButton(self.decimateGroup)
        self.peakRadio.setChecked(True)
        self.peakRadio.setObjectName("peakRadio")
        self.gridLayout_4.addWidget(self.peakRadio, 6, 1, 1, 2)
        self.maxTracesSpin = QtWidgets.QSpinBox(self.decimateGroup)
        self.maxTracesSpin.setObjectName("maxTracesSpin")
        self.gridLayout_4.addWidget(self.maxTracesSpin, 8, 2, 1, 1)
        self.forgetTracesCheck = QtWidgets.QCheckBox(self.decimateGroup)
        self.forgetTracesCheck.setObjectName("forgetTracesCheck")
        self.gridLayout_4.addWidget(self.forgetTracesCheck, 9, 0, 1, 3)
        self.meanRadio = QtWidgets.QRadioButton(self.decimateGroup)
        self.meanRadio.setObjectName("meanRadio")
        self.gridLayout_4.addWidget(self.meanRadio, 3, 1, 1, 2)
        self.subsampleRadio = QtWidgets.QRadioButton(self.decimateGroup)
        self.subsampleRadio.setObjectName("subsampleRadio")
        self.gridLayout_4.addWidget(self.subsampleRadio, 2, 1, 1, 2)
        self.autoDownsampleCheck = QtWidgets.QCheckBox(self.decimateGroup)
        self.autoDownsampleCheck.setChecked(True)
        self.autoDownsampleCheck.setObjectName("autoDownsampleCheck")
        self.gridLayout_4.addWidget(self.autoDownsampleCheck, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 2, 0, 1, 1)
        self.downsampleSpin = QtWidgets.QSpinBox(self.decimateGroup)
        self.downsampleSpin.setMinimum(1)
        self.downsampleSpin.setMaximum(100000)
        self.downsampleSpin.setProperty("value", 1)
        self.downsampleSpin.setObjectName("downsampleSpin")
        self.gridLayout_4.addWidget(self.downsampleSpin, 1, 1, 1, 1)
        self.transformGroup = QtWidgets.QFrame(Form)
        self.transformGroup.setGeometry(QtCore.QRect(0, 0, 154, 79))
        self.transformGroup.setObjectName("transformGroup")
        self.gridLayout = QtWidgets.QGridLayout(self.transformGroup)
        self.gridLayout.setObjectName("gridLayout")
        self.fftCheck = QtWidgets.QCheckBox(self.transformGroup)
        self.fftCheck.setObjectName("fftCheck")
        self.gridLayout.addWidget(self.fftCheck, 0, 0, 1, 1)
        self.logXCheck = QtWidgets.QCheckBox(self.transformGroup)
        self.logXCheck.setObjectName("logXCheck")
        self.gridLayout.addWidget(self.logXCheck, 1, 0, 1, 1)
        self.logYCheck = QtWidgets.QCheckBox(self.transformGroup)
        self.logYCheck.setObjectName("logYCheck")
        self.gridLayout.addWidget(self.logYCheck, 2, 0, 1, 1)
        self.pointsGroup = QtWidgets.QGroupBox(Form)
        self.pointsGroup.setGeometry(QtCore.QRect(10, 550, 234, 58))
        self.pointsGroup.setCheckable(True)
        self.pointsGroup.setObjectName("pointsGroup")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.pointsGroup)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.autoPointsCheck = QtWidgets.QCheckBox(self.pointsGroup)
        self.autoPointsCheck.setChecked(True)
        self.autoPointsCheck.setObjectName("autoPointsCheck")
        self.verticalLayout_5.addWidget(self.autoPointsCheck)
        self.gridGroup = QtWidgets.QFrame(Form)
        self.gridGroup.setGeometry(QtCore.QRect(10, 460, 221, 81))
        self.gridGroup.setObjectName("gridGroup")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridGroup)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.xGridCheck = QtWidgets.QCheckBox(self.gridGroup)
        self.xGridCheck.setObjectName("xGridCheck")
        self.gridLayout_2.addWidget(self.xGridCheck, 0, 0, 1, 2)
        self.yGridCheck = QtWidgets.QCheckBox(self.gridGroup)
        self.yGridCheck.setObjectName("yGridCheck")
        self.gridLayout_2.addWidget(self.yGridCheck, 1, 0, 1, 2)
        self.gridAlphaSlider = QtWidgets.QSlider(self.gridGroup)
        self.gridAlphaSlider.setMaximum(255)
        self.gridAlphaSlider.setProperty("value", 128)
        self.gridAlphaSlider.setOrientation(QtCore.Qt.Horizontal)
        self.gridAlphaSlider.setObjectName("gridAlphaSlider")
        self.gridLayout_2.addWidget(self.gridAlphaSlider, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridGroup)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.alphaGroup = QtWidgets.QGroupBox(Form)
        self.alphaGroup.setGeometry(QtCore.QRect(10, 390, 234, 60))
        self.alphaGroup.setCheckable(True)
        self.alphaGroup.setObjectName("alphaGroup")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.alphaGroup)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.autoAlphaCheck = QtWidgets.QCheckBox(self.alphaGroup)
        self.autoAlphaCheck.setChecked(False)
        self.autoAlphaCheck.setObjectName("autoAlphaCheck")
        self.horizontalLayout.addWidget(self.autoAlphaCheck)
        self.alphaSlider = QtWidgets.QSlider(self.alphaGroup)
        self.alphaSlider.setMaximum(1000)
        self.alphaSlider.setProperty("value", 1000)
        self.alphaSlider.setOrientation(QtCore.Qt.Horizontal)
        self.alphaSlider.setObjectName("alphaSlider")
        self.horizontalLayout.addWidget(self.alphaSlider)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.averageGroup.setToolTip(
            _translate(
                "Form",
                "Display averages of the curves displayed in this plot. The parameter list allows you to choose parameters to average over (if any are available).",
            )
        )
        self.averageGroup.setTitle(_translate("Form", "Average"))
        self.clipToViewCheck.setToolTip(
            _translate(
                "Form",
                "Plot only the portion of each curve that is visible. This assumes X values are uniformly spaced.",
            )
        )
        self.clipToViewCheck.setText(_translate("Form", "Clip to View"))
        self.maxTracesCheck.setToolTip(
            _translate(
                "Form",
                "If multiple curves are displayed in this plot, check this box to limit the number of traces that are displayed.",
            )
        )
        self.maxTracesCheck.setText(_translate("Form", "Max Traces:"))
        self.downsampleCheck.setText(_translate("Form", "Downsample"))
        self.peakRadio.setToolTip(
            _translate(
                "Form",
                "Downsample by drawing a saw wave that follows the min and max of the original data. This method produces the best visual representation of the data but is slower.",
            )
        )
        self.peakRadio.setText(_translate("Form", "Peak"))
        self.maxTracesSpin.setToolTip(
            _translate(
                "Form",
                'If multiple curves are displayed in this plot, check "Max Traces" and set this value to limit the number of traces that are displayed.',
            )
        )
        self.forgetTracesCheck.setToolTip(
            _translate(
                "Form",
                "If MaxTraces is checked, remove curves from memory after they are hidden (saves memory, but traces can not be un-hidden).",
            )
        )
        self.forgetTracesCheck.setText(_translate("Form", "Forget hidden traces"))
        self.meanRadio.setToolTip(_translate("Form", "Downsample by taking the mean of N samples."))
        self.meanRadio.setText(_translate("Form", "Mean"))
        self.subsampleRadio.setToolTip(
            _translate(
                "Form", "Downsample by taking the first of N samples. This method is fastest and least accurate."
            )
        )
        self.subsampleRadio.setText(_translate("Form", "Subsample"))
        self.autoDownsampleCheck.setToolTip(
            _translate(
                "Form",
                "Automatically downsample data based on the visible range. This assumes X values are uniformly spaced.",
            )
        )
        self.autoDownsampleCheck.setText(_translate("Form", "Auto"))
        self.downsampleSpin.setToolTip(_translate("Form", "Downsample data before plotting. (plot every Nth sample)"))
        self.downsampleSpin.setSuffix(_translate("Form", "x"))
        self.fftCheck.setText(_translate("Form", "Power Spectrum (FFT)"))
        self.logXCheck.setText(_translate("Form", "Log X"))
        self.logYCheck.setText(_translate("Form", "Log Y"))
        self.pointsGroup.setTitle(_translate("Form", "Points"))
        self.autoPointsCheck.setText(_translate("Form", "Auto"))
        self.xGridCheck.setText(_translate("Form", "Show X Grid"))
        self.yGridCheck.setText(_translate("Form", "Show Y Grid"))
        self.label.setText(_translate("Form", "Opacity"))
        self.alphaGroup.setTitle(_translate("Form", "Alpha"))
        self.autoAlphaCheck.setText(_translate("Form", "Auto"))
