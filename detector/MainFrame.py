# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from detector.MainUI import Ui_MainWindow
from detector.carFrame import CarFrame
from detector.peopleFrame import PeopleFrame


class MainFrame(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 设置主窗口背景色为浅灰色
        self.setStyleSheet("background-color: #f0f0f0;")

        # 创建 QLabel 用于显示背景文字
        self.label = QtWidgets.QLabel(self.centralWidget())
        self.label.setAlignment(QtCore.Qt.AlignCenter)  # 文字居中对齐
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)

        self.label.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.Resize and source == self:
            self.on_resize(event)
        return super().eventFilter(source, event)

    def on_resize(self, event):

        self.label.setGeometry(0, 0, event.size().width(), event.size().height())

    def goin(self):

        print("车流量检测按钮 clicked!")  # 添加调试信息
        try:
            self.car_dialog = CarFrame()  # 创建新窗口对象，确保导入了 DetectorDialog
            self.car_dialog.show()  # 显示新窗口
            print("New window should be shown.")  # 添加调试信息
        except Exception as e:
            print(f"Error: {e}")  # 打印异常信息

    def goin_people(self):
        print("人流量检测按钮 clicked!")  # 调试信息
        try:
            self.people_dialog = PeopleFrame()
            self.people_dialog.show()
            print("New window should be shown.")
            pass
        except Exception as e:
            print(f"Error: {e}")  # 打印异常信息
