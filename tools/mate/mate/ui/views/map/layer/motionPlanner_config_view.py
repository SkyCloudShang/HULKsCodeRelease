# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/mate/ui/views/map/layer/motionPlanner_config_view.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MotionPlannerConfig(object):
    def setupUi(self, MotionPlannerConfig):
        MotionPlannerConfig.setObjectName("MotionPlannerConfig")
        MotionPlannerConfig.resize(591, 613)
        self.verticalLayout = QtWidgets.QVBoxLayout(MotionPlannerConfig)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(MotionPlannerConfig)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -89, 559, 654))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(4, 4, 4, 4)
        self.formLayout.setObjectName("formLayout")
        self.nameMotionPlannerEdit = QtWidgets.QLineEdit(self.groupBox)
        self.nameMotionPlannerEdit.setObjectName("nameMotionPlannerEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameMotionPlannerEdit)
        self.centerLabel = QtWidgets.QLabel(self.groupBox)
        self.centerLabel.setObjectName("centerLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.centerLabel)
        self.centerWidget = QtWidgets.QWidget(self.groupBox)
        self.centerWidget.setObjectName("centerWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centerWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_center_x = QtWidgets.QLabel(self.centerWidget)
        self.label_center_x.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_center_x.setObjectName("label_center_x")
        self.horizontalLayout_2.addWidget(self.label_center_x)
        self.spin_center_x = QtWidgets.QDoubleSpinBox(self.centerWidget)
        self.spin_center_x.setMinimum(-99.99)
        self.spin_center_x.setObjectName("spin_center_x")
        self.horizontalLayout_2.addWidget(self.spin_center_x)
        self.label_center_y = QtWidgets.QLabel(self.centerWidget)
        self.label_center_y.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_center_y.setObjectName("label_center_y")
        self.horizontalLayout_2.addWidget(self.label_center_y)
        self.spin_center_y = QtWidgets.QDoubleSpinBox(self.centerWidget)
        self.spin_center_y.setMinimum(-99.99)
        self.spin_center_y.setObjectName("spin_center_y")
        self.horizontalLayout_2.addWidget(self.spin_center_y)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.centerWidget)
        self.enabledLabel = QtWidgets.QLabel(self.groupBox)
        self.enabledLabel.setObjectName("enabledLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.enabledLabel)
        self.enabledCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.enabledCheckBox.setChecked(True)
        self.enabledCheckBox.setObjectName("enabledCheckBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.enabledCheckBox)
        self.nameLabel = QtWidgets.QLabel(self.groupBox)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.translationLabel = QtWidgets.QLabel(self.groupBox)
        self.translationLabel.setObjectName("translationLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.translationLabel)
        self.translationWidget = QtWidgets.QWidget(self.groupBox)
        self.translationWidget.setObjectName("translationWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.translationWidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.cbx_TransformationKey = QtWidgets.QComboBox(self.translationWidget)
        self.cbx_TransformationKey.setEditable(True)
        self.cbx_TransformationKey.setObjectName("cbx_TransformationKey")
        self.verticalLayout_6.addWidget(self.cbx_TransformationKey)
        self.label_4 = QtWidgets.QLabel(self.translationWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.edit_TransformationKeyLambda = QtWidgets.QTextEdit(self.translationWidget)
        self.edit_TransformationKeyLambda.setMaximumSize(QtCore.QSize(16777215, 80))
        self.edit_TransformationKeyLambda.setTabStopWidth(16)
        self.edit_TransformationKeyLambda.setObjectName("edit_TransformationKeyLambda")
        self.verticalLayout_6.addWidget(self.edit_TransformationKeyLambda)
        self.label_3 = QtWidgets.QLabel(self.translationWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.translationWidget)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setContentsMargins(4, 4, 4, 4)
        self.formLayout_2.setObjectName("formLayout_2")
        self.keyLambdaWidget = QtWidgets.QWidget(self.groupBox_2)
        self.keyLambdaWidget.setObjectName("keyLambdaWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.keyLambdaWidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.cbx_MotionPlannerKey = QtWidgets.QComboBox(self.keyLambdaWidget)
        self.cbx_MotionPlannerKey.setEditable(True)
        self.cbx_MotionPlannerKey.setObjectName("cbx_MotionPlannerKey")
        self.verticalLayout_4.addWidget(self.cbx_MotionPlannerKey)
        self.label = QtWidgets.QLabel(self.keyLambdaWidget)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.edit_MotionPlannerKeyLambda = QtWidgets.QTextEdit(self.keyLambdaWidget)
        self.edit_MotionPlannerKeyLambda.setMaximumSize(QtCore.QSize(16777215, 80))
        self.edit_MotionPlannerKeyLambda.setTabStopWidth(16)
        self.edit_MotionPlannerKeyLambda.setObjectName("edit_MotionPlannerKeyLambda")
        self.verticalLayout_4.addWidget(self.edit_MotionPlannerKeyLambda)
        self.label_2 = QtWidgets.QLabel(self.keyLambdaWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.keyLambdaWidget)
        self.targetCircleDiameter = QtWidgets.QLabel(self.groupBox_2)
        self.targetCircleDiameter.setObjectName("targetCircleDiameter")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.targetCircleDiameter)
        self.spin_targetCircleDiameter = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.spin_targetCircleDiameter.setObjectName("spin_targetCircleDiameter")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spin_targetCircleDiameter)
        self.targetColorWidget = QtWidgets.QWidget(self.groupBox_2)
        self.targetColorWidget.setObjectName("targetColorWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.targetColorWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.targetColorLabel = QtWidgets.QLabel(self.targetColorWidget)
        self.targetColorLabel.setObjectName("targetColorLabel")
        self.horizontalLayout_3.addWidget(self.targetColorLabel)
        self.edit_targetColor = QtWidgets.QLineEdit(self.targetColorWidget)
        self.edit_targetColor.setObjectName("edit_targetColor")
        self.horizontalLayout_3.addWidget(self.edit_targetColor)
        self.btn_targetColor = QtWidgets.QPushButton(self.targetColorWidget)
        self.btn_targetColor.setFlat(False)
        self.btn_targetColor.setObjectName("btn_targetColor")
        self.horizontalLayout_3.addWidget(self.btn_targetColor)
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.targetColorWidget)
        self.KeyLabel = QtWidgets.QLabel(self.groupBox_2)
        self.KeyLabel.setObjectName("KeyLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.KeyLabel)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAccept = QtWidgets.QPushButton(MotionPlannerConfig)
        self.btnAccept.setObjectName("btnAccept")
        self.horizontalLayout.addWidget(self.btnAccept)
        self.btnDiscard = QtWidgets.QPushButton(MotionPlannerConfig)
        self.btnDiscard.setObjectName("btnDiscard")
        self.horizontalLayout.addWidget(self.btnDiscard)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(MotionPlannerConfig)
        QtCore.QMetaObject.connectSlotsByName(MotionPlannerConfig)
        MotionPlannerConfig.setTabOrder(self.nameMotionPlannerEdit, self.spin_center_x)
        MotionPlannerConfig.setTabOrder(self.spin_center_x, self.spin_center_y)
        MotionPlannerConfig.setTabOrder(self.spin_center_y, self.enabledCheckBox)
        MotionPlannerConfig.setTabOrder(self.enabledCheckBox, self.edit_MotionPlannerKeyLambda)
        MotionPlannerConfig.setTabOrder(self.edit_MotionPlannerKeyLambda, self.spin_targetCircleDiameter)
        MotionPlannerConfig.setTabOrder(self.spin_targetCircleDiameter, self.btnAccept)
        MotionPlannerConfig.setTabOrder(self.btnAccept, self.btnDiscard)
        MotionPlannerConfig.setTabOrder(self.btnDiscard, self.scrollArea)

    def retranslateUi(self, MotionPlannerConfig):
        _translate = QtCore.QCoreApplication.translate
        MotionPlannerConfig.setWindowTitle(_translate("MotionPlannerConfig", "Form"))
        self.groupBox.setTitle(_translate("MotionPlannerConfig", "General:"))
        self.centerLabel.setText(_translate("MotionPlannerConfig", "Center"))
        self.label_center_x.setText(_translate("MotionPlannerConfig", "X:"))
        self.label_center_y.setText(_translate("MotionPlannerConfig", "Y:"))
        self.enabledLabel.setText(_translate("MotionPlannerConfig", "Enabled:"))
        self.nameLabel.setText(_translate("MotionPlannerConfig", "Name:"))
        self.translationLabel.setText(_translate("MotionPlannerConfig", "TransformationKey:"))
        self.label_4.setText(_translate("MotionPlannerConfig", "def parse(input):"))
        self.label_3.setText(_translate("MotionPlannerConfig", "return output"))
        self.groupBox_2.setTitle(_translate("MotionPlannerConfig", "MotionPlan:"))
        self.label.setText(_translate("MotionPlannerConfig", "def parse(input):"))
        self.label_2.setText(_translate("MotionPlannerConfig", "return output"))
        self.targetCircleDiameter.setText(_translate("MotionPlannerConfig", "targetCircleDiameter:"))
        self.targetColorLabel.setText(_translate("MotionPlannerConfig", "targetColor:"))
        self.btn_targetColor.setText(_translate("MotionPlannerConfig", "Pick"))
        self.KeyLabel.setText(_translate("MotionPlannerConfig", "Key:"))
        self.btnAccept.setText(_translate("MotionPlannerConfig", "Accept"))
        self.btnDiscard.setText(_translate("MotionPlannerConfig", "Discard"))

