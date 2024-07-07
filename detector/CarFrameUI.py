from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap

import numpy as np
import cv2 as cv


class CarDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(993, 696)
        Dialog.setObjectName("Dialog")
        Dialog.resize(993, 696)

        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(10, 120, 971, 571))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.video1 = QtWidgets.QLabel(self.frame)
        self.video1.setGeometry(QtCore.QRect(0, 0, 971, 571))  # Adjusted to match frame size
        self.video1.setObjectName("video1")
        self.video1.setScaledContents(True)

        self.frame_5 = QtWidgets.QFrame(Dialog)
        self.frame_5.setGeometry(QtCore.QRect(10, 69, 151, 41))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setGeometry(QtCore.QRect(10, 0, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame_6 = QtWidgets.QFrame(Dialog)
        self.frame_6.setGeometry(QtCore.QRect(170, 70, 221, 41))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.carnum = QtWidgets.QLabel(self.frame_6)
        self.carnum.setGeometry(QtCore.QRect(0, 0, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.carnum.setFont(font)
        self.carnum.setStyleSheet("color:red\n""")
        self.carnum.setObjectName("carnum")
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(170, 20, 631, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.video1.setText(_translate("Dialog", "TextLabel"))
        self.label.setText(_translate("Dialog", "车流量"))
        self.carnum.setText(_translate("Dialog", "0"))
        self.title.setText(_translate("Dialog", "人车流量检测系统"))

    def update_frame(self, frame):
        height, width, channel = frame.shape
        bytes_per_line = 3 * width
        q_img = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        self.video1.setPixmap(QPixmap.fromImage(q_img))

    def update_vehicle_count(self, num):
        self.carnum.setText(f"车辆数量: {num}")


