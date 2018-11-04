# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tools/mate/src/mate/ui/views/camera_calib/camera_calib_view.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CameraCalibration(object):
    def setupUi(self, CameraCalibration):
        CameraCalibration.setObjectName("CameraCalibration")
        CameraCalibration.resize(537, 554)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalWidget = QtWidgets.QWidget(self.dockWidgetContents)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(6, 6, 6, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnCalibrate = QtWidgets.QPushButton(self.verticalWidget)
        self.btnCalibrate.setMinimumSize(QtCore.QSize(0, 0))
        self.btnCalibrate.setObjectName("btnCalibrate")
        self.horizontalLayout_3.addWidget(self.btnCalibrate)
        self.btnShowResults = QtWidgets.QPushButton(self.verticalWidget)
        self.btnShowResults.setEnabled(False)
        self.btnShowResults.setObjectName("btnShowResults")
        self.horizontalLayout_3.addWidget(self.btnShowResults)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.resultWidget = QtWidgets.QWidget(self.verticalWidget)
        self.resultWidget.setObjectName("resultWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.resultWidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.checkSaveBotInt = QtWidgets.QCheckBox(self.resultWidget)
        self.checkSaveBotInt.setEnabled(False)
        self.checkSaveBotInt.setObjectName("checkSaveBotInt")
        self.gridLayout_4.addWidget(self.checkSaveBotInt, 0, 3, 1, 1)
        self.checkSaveBotExt = QtWidgets.QCheckBox(self.resultWidget)
        self.checkSaveBotExt.setEnabled(False)
        self.checkSaveBotExt.setObjectName("checkSaveBotExt")
        self.gridLayout_4.addWidget(self.checkSaveBotExt, 1, 3, 1, 1)
        self.checkSaveTopExt = QtWidgets.QCheckBox(self.resultWidget)
        self.checkSaveTopExt.setEnabled(False)
        self.checkSaveTopExt.setObjectName("checkSaveTopExt")
        self.gridLayout_4.addWidget(self.checkSaveTopExt, 1, 2, 1, 1)
        self.btnSave = QtWidgets.QPushButton(self.resultWidget)
        self.btnSave.setEnabled(False)
        self.btnSave.setObjectName("btnSave")
        self.gridLayout_4.addWidget(self.btnSave, 0, 0, 1, 1)
        self.checkSaveTopInt = QtWidgets.QCheckBox(self.resultWidget)
        self.checkSaveTopInt.setEnabled(False)
        self.checkSaveTopInt.setObjectName("checkSaveTopInt")
        self.gridLayout_4.addWidget(self.checkSaveTopInt, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.resultWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.resultWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 1, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_4)
        self.txtResult = QtWidgets.QPlainTextEdit(self.resultWidget)
        self.txtResult.setReadOnly(True)
        self.txtResult.setPlainText("")
        self.txtResult.setObjectName("txtResult")
        self.verticalLayout_4.addWidget(self.txtResult)
        self.verticalLayout.addWidget(self.resultWidget)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(4, 8, 4, 2)
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setVerticalSpacing(4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnConfAndManualMode = QtWidgets.QPushButton(self.verticalWidget)
        self.btnConfAndManualMode.setObjectName("btnConfAndManualMode")
        self.gridLayout_2.addWidget(self.btnConfAndManualMode, 3, 0, 1, 1)
        self.btnCapture = QtWidgets.QPushButton(self.verticalWidget)
        self.btnCapture.setObjectName("btnCapture")
        self.gridLayout_2.addWidget(self.btnCapture, 1, 3, 1, 1)
        self.btnProjectMarkers = QtWidgets.QPushButton(self.verticalWidget)
        self.btnProjectMarkers.setObjectName("btnProjectMarkers")
        self.gridLayout_2.addWidget(self.btnProjectMarkers, 1, 2, 1, 1)
        self.checkBoxCalibModeEnable = QtWidgets.QCheckBox(self.verticalWidget)
        self.checkBoxCalibModeEnable.setObjectName("checkBoxCalibModeEnable")
        self.gridLayout_2.addWidget(self.checkBoxCalibModeEnable, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnPlayMotionSeq = QtWidgets.QPushButton(self.verticalWidget)
        self.btnPlayMotionSeq.setObjectName("btnPlayMotionSeq")
        self.horizontalLayout.addWidget(self.btnPlayMotionSeq)
        self.btnStopMotion = QtWidgets.QPushButton(self.verticalWidget)
        self.btnStopMotion.setEnabled(False)
        self.btnStopMotion.setObjectName("btnStopMotion")
        self.horizontalLayout.addWidget(self.btnStopMotion)
        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnClearCaptures = QtWidgets.QPushButton(self.verticalWidget)
        self.btnClearCaptures.setEnabled(True)
        self.btnClearCaptures.setObjectName("btnClearCaptures")
        self.horizontalLayout_2.addWidget(self.btnClearCaptures)
        self.btnDownload = QtWidgets.QPushButton(self.verticalWidget)
        self.btnDownload.setObjectName("btnDownload")
        self.horizontalLayout_2.addWidget(self.btnDownload)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 3, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.configWidget = QtWidgets.QWidget(self.verticalWidget)
        self.configWidget.setObjectName("configWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.configWidget)
        self.gridLayout.setContentsMargins(-1, 0, 2, 0)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(4)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBoxIntrinsicTop = QtWidgets.QCheckBox(self.configWidget)
        self.checkBoxIntrinsicTop.setObjectName("checkBoxIntrinsicTop")
        self.gridLayout.addWidget(self.checkBoxIntrinsicTop, 1, 2, 1, 1)
        self.txtPosV = QtWidgets.QLineEdit(self.configWidget)
        self.txtPosV.setEnabled(False)
        self.txtPosV.setMinimumSize(QtCore.QSize(80, 0))
        self.txtPosV.setPlaceholderText("0")
        self.txtPosV.setObjectName("txtPosV")
        self.gridLayout.addWidget(self.txtPosV, 5, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        self.txtPitch = QtWidgets.QLineEdit(self.configWidget)
        self.txtPitch.setMinimumSize(QtCore.QSize(80, 0))
        self.txtPitch.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.txtPitch.setPlaceholderText("0")
        self.txtPitch.setClearButtonEnabled(False)
        self.txtPitch.setObjectName("txtPitch")
        self.gridLayout.addWidget(self.txtPitch, 4, 2, 1, 1)
        self.checkBoxIntrinsicBottom = QtWidgets.QCheckBox(self.configWidget)
        self.checkBoxIntrinsicBottom.setObjectName("checkBoxIntrinsicBottom")
        self.gridLayout.addWidget(self.checkBoxIntrinsicBottom, 1, 3, 1, 1)
        self.checkBoxExtrinsicBottom = QtWidgets.QCheckBox(self.configWidget)
        self.checkBoxExtrinsicBottom.setChecked(True)
        self.checkBoxExtrinsicBottom.setObjectName("checkBoxExtrinsicBottom")
        self.gridLayout.addWidget(self.checkBoxExtrinsicBottom, 3, 3, 1, 1)
        self.checkBoxExtrinsicTop = QtWidgets.QCheckBox(self.configWidget)
        self.checkBoxExtrinsicTop.setChecked(True)
        self.checkBoxExtrinsicTop.setObjectName("checkBoxExtrinsicTop")
        self.gridLayout.addWidget(self.checkBoxExtrinsicTop, 3, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.configWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.txtYaw = QtWidgets.QLineEdit(self.configWidget)
        self.txtYaw.setMinimumSize(QtCore.QSize(80, 0))
        self.txtYaw.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.txtYaw.setPlaceholderText("0")
        self.txtYaw.setObjectName("txtYaw")
        self.gridLayout.addWidget(self.txtYaw, 4, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.configWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.txtRotV = QtWidgets.QLineEdit(self.configWidget)
        self.txtRotV.setEnabled(False)
        self.txtRotV.setMinimumSize(QtCore.QSize(80, 0))
        self.txtRotV.setPlaceholderText("0")
        self.txtRotV.setObjectName("txtRotV")
        self.gridLayout.addWidget(self.txtRotV, 5, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.configWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.configWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.btnManualMove = QtWidgets.QPushButton(self.configWidget)
        self.btnManualMove.setObjectName("btnManualMove")
        self.gridLayout.addWidget(self.btnManualMove, 7, 2, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 6, 2, 1, 1)
        self.label_6.raise_()
        self.checkBoxExtrinsicTop.raise_()
        self.label_2.raise_()
        self.checkBoxExtrinsicBottom.raise_()
        self.checkBoxIntrinsicTop.raise_()
        self.txtPitch.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.btnManualMove.raise_()
        self.txtPosV.raise_()
        self.txtRotV.raise_()
        self.checkBoxIntrinsicBottom.raise_()
        self.txtYaw.raise_()
        self.verticalLayout.addWidget(self.configWidget)
        self.gridLayout_5.addWidget(self.verticalWidget, 0, 0, 1, 1)
        self.lblStatus = QtWidgets.QLabel(self.dockWidgetContents)
        self.lblStatus.setText("")
        self.lblStatus.setObjectName("lblStatus")
        self.gridLayout_5.addWidget(self.lblStatus, 2, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.dockWidgetContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 517, 68))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.canvasTopCam = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvasTopCam.sizePolicy().hasHeightForWidth())
        self.canvasTopCam.setSizePolicy(sizePolicy)
        self.canvasTopCam.setText("")
        self.canvasTopCam.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.canvasTopCam.setObjectName("canvasTopCam")
        self.verticalLayout_2.addWidget(self.canvasTopCam)
        self.canvasBottomCam = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvasBottomCam.sizePolicy().hasHeightForWidth())
        self.canvasBottomCam.setSizePolicy(sizePolicy)
        self.canvasBottomCam.setText("")
        self.canvasBottomCam.setObjectName("canvasBottomCam")
        self.verticalLayout_2.addWidget(self.canvasBottomCam)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_5.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.scrollArea.raise_()
        self.lblStatus.raise_()
        self.verticalWidget.raise_()
        CameraCalibration.setWidget(self.dockWidgetContents)

        self.retranslateUi(CameraCalibration)
        QtCore.QMetaObject.connectSlotsByName(CameraCalibration)
        CameraCalibration.setTabOrder(self.checkBoxCalibModeEnable, self.btnCapture)
        CameraCalibration.setTabOrder(self.btnCapture, self.btnProjectMarkers)
        CameraCalibration.setTabOrder(self.btnProjectMarkers, self.btnCalibrate)
        CameraCalibration.setTabOrder(self.btnCalibrate, self.btnConfAndManualMode)
        CameraCalibration.setTabOrder(self.btnConfAndManualMode, self.checkBoxIntrinsicTop)
        CameraCalibration.setTabOrder(self.checkBoxIntrinsicTop, self.checkBoxIntrinsicBottom)
        CameraCalibration.setTabOrder(self.checkBoxIntrinsicBottom, self.checkBoxExtrinsicTop)
        CameraCalibration.setTabOrder(self.checkBoxExtrinsicTop, self.checkBoxExtrinsicBottom)
        CameraCalibration.setTabOrder(self.checkBoxExtrinsicBottom, self.txtPitch)
        CameraCalibration.setTabOrder(self.txtPitch, self.txtYaw)
        CameraCalibration.setTabOrder(self.txtYaw, self.txtPosV)
        CameraCalibration.setTabOrder(self.txtPosV, self.txtRotV)
        CameraCalibration.setTabOrder(self.txtRotV, self.btnManualMove)
        CameraCalibration.setTabOrder(self.btnManualMove, self.scrollArea)

    def retranslateUi(self, CameraCalibration):
        _translate = QtCore.QCoreApplication.translate
        CameraCalibration.setWindowTitle(_translate("CameraCalibration", "Camera Calibration"))
        self.btnCalibrate.setText(_translate("CameraCalibration", "Calibrate"))
        self.btnShowResults.setText(_translate("CameraCalibration", "Results"))
        self.checkSaveBotInt.setText(_translate("CameraCalibration", "Bottom"))
        self.checkSaveBotExt.setText(_translate("CameraCalibration", "Bottom"))
        self.checkSaveTopExt.setText(_translate("CameraCalibration", "Top"))
        self.btnSave.setText(_translate("CameraCalibration", "Save"))
        self.checkSaveTopInt.setText(_translate("CameraCalibration", "Top"))
        self.label_3.setText(_translate("CameraCalibration", "Intrinsic"))
        self.label_7.setText(_translate("CameraCalibration", "Extrinsic"))
        self.btnConfAndManualMode.setText(_translate("CameraCalibration", "Config and manual mode"))
        self.btnCapture.setText(_translate("CameraCalibration", "Capture"))
        self.btnProjectMarkers.setText(_translate("CameraCalibration", "Project Markers"))
        self.checkBoxCalibModeEnable.setText(_translate("CameraCalibration", "Calib Mode"))
        self.btnPlayMotionSeq.setText(_translate("CameraCalibration", "Play"))
        self.btnStopMotion.setText(_translate("CameraCalibration", "Stop"))
        self.btnClearCaptures.setText(_translate("CameraCalibration", "Clear"))
        self.btnDownload.setText(_translate("CameraCalibration", "Download"))
        self.checkBoxIntrinsicTop.setText(_translate("CameraCalibration", "Top"))
        self.txtPosV.setToolTip(_translate("CameraCalibration", "Pitch"))
        self.txtPitch.setToolTip(_translate("CameraCalibration", "Pitch"))
        self.checkBoxIntrinsicBottom.setText(_translate("CameraCalibration", "Bottom"))
        self.checkBoxExtrinsicBottom.setText(_translate("CameraCalibration", "Bottom"))
        self.checkBoxExtrinsicTop.setText(_translate("CameraCalibration", "Top"))
        self.label_2.setText(_translate("CameraCalibration", "Intrinsic"))
        self.txtYaw.setToolTip(_translate("CameraCalibration", "Yaw"))
        self.label_5.setText(_translate("CameraCalibration", "Head : Pitch & Yaw"))
        self.txtRotV.setToolTip(_translate("CameraCalibration", "Yaw"))
        self.label_4.setText(_translate("CameraCalibration", "Extrinsic"))
        self.label_6.setText(_translate("CameraCalibration", "Torso : PosV, RotV"))
        self.btnManualMove.setText(_translate("CameraCalibration", "Move"))
