# 05. pyqt_timer.py
# pyqt 타이머 예제
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import QTimer

class MyApp(QWidget):
    time = int(0)
    def __init__(self):
        super().__init__()
        # 창 크기 고정
        self.setFixedSize(400, 300)
        # 창 제목 설정
        self.setWindowTitle('MyApp')

        # 타이머 생성
        qtimer = QTimer(self)
        # 타이머에 실행할 함수 연결
        qtimer.timeout.connect(self.timer)
        # 1초(=1000밀리초)마다 연결된 함수를 실행
        qtimer.start(1000)

        self.label_text = QLabel(self)
        # 창 띄우기 
        self.show()

    def timer(self):
        
        self.label_text.setText(self.time)
        self.label_text.setGeometry(0, 150, 50, 100)
        self.time += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())