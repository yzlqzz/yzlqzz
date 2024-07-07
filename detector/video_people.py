from PyQt5.QtCore import QThread, pyqtSignal
import cv2 as cv
from ai.car_people import pedestrian_detect


class VideoPeople(QThread):
    send = pyqtSignal(int, int, int, bytes, int, int)

    def __init__(self, video_id):
        super().__init__()
        self.th_id = 0
        if video_id == "D:\project1\data\qwe.mp4":
            self.th_id = 1
        self.dev = cv.VideoCapture(video_id)
        self.dev.open(video_id)

    def run(self):
        while True:
            ret, frame = self.dev.read()
            if not ret:
                print('No frame read')
                break
            frame, num = pedestrian_detect(frame)
            h, w, c = frame.shape
            img_bytes = frame.tobytes()
            self.send.emit(h, w, c, img_bytes, self.th_id, num)
            QThread.msleep(100)
