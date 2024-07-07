import numpy as np
from PyQt5.QtWidgets import QDialog, QApplication
from detector.PeopleFrameUI import PeopleDialog
from detector.video_people import VideoPeople
import sys


class PeopleFrame(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = PeopleDialog()
        self.ui.setupUi(self)

        self.video_thread = VideoPeople('D:\project1\data\qwe.mp4')
        self.video_thread.send.connect(self.show_image_and_count)
        self.video_thread.start()

    def show_image_and_count(self, h, w, c, b, th_id, num):
        frame = np.frombuffer(b, dtype=np.uint8).reshape(h, w, c)
        self.ui.update_frame(frame)
        self.ui.update_people_count(num)


