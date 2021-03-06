# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'striker_config_view.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StrikerConfig(object):
    def setupUi(self, StrikerConfig):
        StrikerConfig.setObjectName("StrikerConfig")
        StrikerConfig.resize(272, 454)
        self.verticalLayout = QtWidgets.QVBoxLayout(StrikerConfig)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(StrikerConfig)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 264, 428))
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
        self.nameLabel = QtWidgets.QLabel(self.groupBox)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.edit_name = QtWidgets.QLineEdit(self.groupBox)
        self.edit_name.setObjectName("edit_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.edit_name)
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
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.enabledLabel)
        self.enabledCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.enabledCheckBox.setChecked(True)
        self.enabledCheckBox.setObjectName("enabledCheckBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.enabledCheckBox)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.kickRatingChunksLabel = QtWidgets.QLabel(self.groupBox_2)
        self.kickRatingChunksLabel.setObjectName("kickRatingChunksLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.kickRatingChunksLabel)
        self.cbx_kickRatingChunksKey = QtWidgets.QComboBox(self.groupBox_2)
        self.cbx_kickRatingChunksKey.setEditable(True)
        self.cbx_kickRatingChunksKey.setObjectName("cbx_kickRatingChunksKey")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cbx_kickRatingChunksKey)
        self.kickRatingChunkWeightsLabel = QtWidgets.QLabel(self.groupBox_2)
        self.kickRatingChunkWeightsLabel.setObjectName("kickRatingChunkWeightsLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.kickRatingChunkWeightsLabel)
        self.cbx_kickRatingChunkWeightsKey = QtWidgets.QComboBox(self.groupBox_2)
        self.cbx_kickRatingChunkWeightsKey.setEditable(True)
        self.cbx_kickRatingChunkWeightsKey.setObjectName("cbx_kickRatingChunkWeightsKey")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cbx_kickRatingChunkWeightsKey)
        self.rateKickLabel = QtWidgets.QLabel(self.groupBox_2)
        self.rateKickLabel.setObjectName("rateKickLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.rateKickLabel)
        self.cbx_rateKick = QtWidgets.QComboBox(self.groupBox_2)
        self.cbx_rateKick.setEditable(True)
        self.cbx_rateKick.setObjectName("cbx_rateKick")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cbx_rateKick)
        self.hitPointsLabel = QtWidgets.QLabel(self.groupBox_2)
        self.hitPointsLabel.setObjectName("hitPointsLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.hitPointsLabel)
        self.cbx_hitPointsKey = QtWidgets.QComboBox(self.groupBox_2)
        self.cbx_hitPointsKey.setEditable(True)
        self.cbx_hitPointsKey.setObjectName("cbx_hitPointsKey")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cbx_hitPointsKey)
        self.teamBallPositionLabel = QtWidgets.QLabel(self.groupBox_2)
        self.teamBallPositionLabel.setObjectName("teamBallPositionLabel")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.teamBallPositionLabel)
        self.cbx_teamBallPositionKey = QtWidgets.QComboBox(self.groupBox_2)
        self.cbx_teamBallPositionKey.setEditable(True)
        self.cbx_teamBallPositionKey.setObjectName("cbx_teamBallPositionKey")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.cbx_teamBallPositionKey)
        self.firstShadowPointLabel = QtWidgets.QLabel(self.groupBox_2)
        self.firstShadowPointLabel.setObjectName("firstShadowPointLabel")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.firstShadowPointLabel)
        self.cbx_firstShadowPointKey = QtWidgets.QComboBox(self.groupBox_2)
        self.cbx_firstShadowPointKey.setEditable(True)
        self.cbx_firstShadowPointKey.setObjectName("cbx_firstShadowPointKey")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.cbx_firstShadowPointKey)
        self.secondShadowPointLabel = QtWidgets.QLabel(self.groupBox_2)
        self.secondShadowPointLabel.setObjectName("secondShadowPointLabel")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.secondShadowPointLabel)
        self.cbx_secondShadowPointKey = QtWidgets.QComboBox(self.groupBox_2)
        self.cbx_secondShadowPointKey.setEditable(True)
        self.cbx_secondShadowPointKey.setObjectName("cbx_secondShadowPointKey")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.cbx_secondShadowPointKey)
        self.firstShadowPointAfterLabel = QtWidgets.QLabel(self.groupBox_2)
        self.firstShadowPointAfterLabel.setObjectName("firstShadowPointAfterLabel")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.firstShadowPointAfterLabel)
        self.cbx_firstShadowPointAfterKey = QtWidgets.QComboBox(self.groupBox_2)
        self.cbx_firstShadowPointAfterKey.setEditable(True)
        self.cbx_firstShadowPointAfterKey.setObjectName("cbx_firstShadowPointAfterKey")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.cbx_firstShadowPointAfterKey)
        self.secondShadowPointAfterLabel = QtWidgets.QLabel(self.groupBox_2)
        self.secondShadowPointAfterLabel.setObjectName("secondShadowPointAfterLabel")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.secondShadowPointAfterLabel)
        self.cbx_secondShadowPointAfterKey = QtWidgets.QComboBox(self.groupBox_2)
        self.cbx_secondShadowPointAfterKey.setEditable(True)
        self.cbx_secondShadowPointAfterKey.setObjectName("cbx_secondShadowPointAfterKey")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.cbx_secondShadowPointAfterKey)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAccept = QtWidgets.QPushButton(StrikerConfig)
        self.btnAccept.setObjectName("btnAccept")
        self.horizontalLayout.addWidget(self.btnAccept)
        self.btnDiscard = QtWidgets.QPushButton(StrikerConfig)
        self.btnDiscard.setObjectName("btnDiscard")
        self.horizontalLayout.addWidget(self.btnDiscard)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(StrikerConfig)
        QtCore.QMetaObject.connectSlotsByName(StrikerConfig)
        StrikerConfig.setTabOrder(self.edit_name, self.spin_center_x)
        StrikerConfig.setTabOrder(self.spin_center_x, self.spin_center_y)
        StrikerConfig.setTabOrder(self.spin_center_y, self.enabledCheckBox)
        StrikerConfig.setTabOrder(self.enabledCheckBox, self.btnAccept)
        StrikerConfig.setTabOrder(self.btnAccept, self.btnDiscard)
        StrikerConfig.setTabOrder(self.btnDiscard, self.scrollArea)

    def retranslateUi(self, StrikerConfig):
        _translate = QtCore.QCoreApplication.translate
        StrikerConfig.setWindowTitle(_translate("StrikerConfig", "Form"))
        self.groupBox.setTitle(_translate("StrikerConfig", "General:"))
        self.nameLabel.setText(_translate("StrikerConfig", "Name:"))
        self.centerLabel.setText(_translate("StrikerConfig", "Center"))
        self.label_center_x.setText(_translate("StrikerConfig", "X:"))
        self.label_center_y.setText(_translate("StrikerConfig", "Y:"))
        self.enabledLabel.setText(_translate("StrikerConfig", "Enabled:"))
        self.groupBox_2.setTitle(_translate("StrikerConfig", "Keys"))
        self.kickRatingChunksLabel.setText(_translate("StrikerConfig", "kickRatingChunks"))
        self.kickRatingChunkWeightsLabel.setText(_translate("StrikerConfig", "kickRatingChunkWeights"))
        self.rateKickLabel.setText(_translate("StrikerConfig", "rateKick"))
        self.hitPointsLabel.setText(_translate("StrikerConfig", "hitPoints"))
        self.teamBallPositionLabel.setText(_translate("StrikerConfig", "teamBallPosition"))
        self.firstShadowPointLabel.setText(_translate("StrikerConfig", "firstShadowPoint"))
        self.secondShadowPointLabel.setText(_translate("StrikerConfig", "secondShadowPoint"))
        self.firstShadowPointAfterLabel.setText(_translate("StrikerConfig", "firstShadowPointAfter"))
        self.secondShadowPointAfterLabel.setText(_translate("StrikerConfig", "secondShadowPointAfter"))
        self.btnAccept.setText(_translate("StrikerConfig", "Accept"))
        self.btnDiscard.setText(_translate("StrikerConfig", "Discard"))

