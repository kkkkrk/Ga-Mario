#화면 넓히기
import retro
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt, QTimer

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.press_buttons = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
        # 새 게임 시작
        self.env.reset()

        # 화면 가져오기
        self.screen = self.env.get_screen()

        # 창 크기 고정
        self.setFixedSize(self.screen.shape[0]*2 + 600, self.screen.shape[1]*2)
        # 창 제목 설정
        self.setWindowTitle('MyApp')

        self.label_image = QLabel(self)

        # image = self.screen
        # qimage = QImage(image, image.shape[1], image.shape[0], QImage.Format_RGB888)
        # pixmap = QPixmap(qimage)
        # pixmap = pixmap.scaled(self.screen.shape[0]*2, self.screen.shape[1]*2, Qt.IgnoreAspectRatio)
        #
        # label_image.setPixmap(pixmap)
        self.label_image.setGeometry(0, 0, self.screen.shape[0]*2, self.screen.shape[1]*2)

        # 타이머 생성
        qtimer = QTimer(self)
        # 타이머에 실행할 함수 연결
        qtimer.timeout.connect(self.timer)
        # 1초(=1000밀리초)마다 연결된 함수를 실행
        qtimer.start(int(1000/60))

        # 창 띄우기
        self.show()

    def timer(self):
        # 키 배열: B, NULL, SELECT, START, U, D, L R, A
        self.env.step(self.press_buttons)
        self.screen = self.env.get_screen()
        image = self.screen
        qimage = QImage(image, image.shape[1], image.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(qimage)
        pixmap = pixmap.scaled(self.screen.shape[0] * 2, self.screen.shape[1] * 2, Qt.IgnoreAspectRatio)

        self.label_image.setPixmap(pixmap)

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_B:
            self.press_buttons[0] = 1
        elif key == Qt.Key_I:
            self.press_buttons[4] = 1
        elif key == Qt.Key_K:
            self.press_buttons[5] = 1
        elif key == Qt.Key_J:
            self.press_buttons[6] = 1
        elif key == Qt.Key_L:
            self.press_buttons[7] = 1
        elif key == Qt.Key_A:
            self.press_buttons[8] = 1

        # 키를 뗄 때
    def keyReleaseEvent(self, event):
        key = event.key()
        if key == Qt.Key_B:
            self.press_buttons[0] = 0
        elif key == Qt.Key_I:
            self.press_buttons[4] = 0
        elif key == Qt.Key_K:
            self.press_buttons[5] = 0
        elif key == Qt.Key_J:
            self.press_buttons[6] = 0
        elif key == Qt.Key_L:
            self.press_buttons[7] = 0
        elif key == Qt.Key_A:
            self.press_buttons[8] = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())