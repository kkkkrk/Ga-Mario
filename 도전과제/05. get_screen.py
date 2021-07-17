import retro
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt 

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
        # 새 게임 시작
        env.reset()

        # 화면 가져오기
        screen = env.get_screen()

        # 창 크기 고정
        self.setFixedSize(screen.shape[0], screen.shape[1])
        # 창 제목 설정
        self.setWindowTitle('MyApp')

        label_image = QLabel(self)

        image = screen
        qimage = QImage(image, image.shape[1], image.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(qimage)
        pixmap = pixmap.scaled(screen.shape[0], screen.shape[1], Qt.IgnoreAspectRatio)

        label_image.setPixmap(pixmap)
        label_image.setGeometry(0, 0, screen.shape[0], screen.shape[1])

        # 창 띄우기
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())