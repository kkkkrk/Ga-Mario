# 03. pyqt_paint_event.py
# PyQt Paint Event
import sys
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(200, 300)
        self.setWindowTitle('GA Mario')
        self.show()

        self.button = QPushButton

    # 창이 업데이트 될 때마다 실행되는 함수
    def paintEvent(self, event):
        # 그리기 도구
        painter = QPainter()
        # 그리기 시작
        painter.begin(self)

        # 펜 설정 (테두리)
        painter.setPen(QPen(Qt.red, 2.0, Qt.SolidLine))
        # 선 그리기
        painter.drawLine(25, 175, 75, 275)

        # 펜 설정 (테두리)
        painter.setPen(QPen(Qt.blue, 2.0, Qt.SolidLine))
        # 선 그리기
        painter.drawLine(75, 201, 75, 275)

        # 펜 설정 (테두리)
        painter.setPen(QPen(Qt.red, 2.0, Qt.SolidLine))
        # 선 그리기
        painter.drawLine(125, 175, 75, 275)

        # RGB 색상으로 펜 설정
        painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))
        # 브러쉬 설정 (채우기)
        painter.setBrush(QBrush(Qt.blue))
        # 직사각형
        painter.drawRect(0, 0, 50, 50)

        # RGB 색상으로 펜 설정
        painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))
        # 브러쉬 설정 (채우기)
        painter.setBrush(QBrush(Qt.NoBrush))
        # 직사각형
        painter.drawRect(50, 0, 50, 50)

        # RGB 색상으로 펜 설정
        painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))
        # 브러쉬 설정 (채우기)
        painter.setBrush(QBrush(Qt.NoBrush))
        # 직사각형
        painter.drawRect(0, 50, 50, 50)

        # RGB 색상으로 펜 설정
        painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))
        # 브러쉬 설정 (채우기)
        painter.setBrush(QBrush(Qt.red))
        # 직사각형
        painter.drawRect(50, 50, 50, 50)

        painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))
        # RGB 색상으로 브러쉬 설정
        painter.setBrush(QBrush(QColor.fromRgb(64, 244, 208)))
        # 타원 그리기
        painter.drawEllipse(0, 150, 50, 50)

        painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))
        # RGB 색상으로 브러쉬 설정
        painter.setBrush(QBrush(QColor.fromRgb(64, 244, 208)))
        # 타원 그리기
        painter.drawEllipse(100, 150, 50, 50)

        painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))
        # RGB 색상으로 브러쉬 설정
        painter.setBrush(QBrush(Qt.NoBrush))
        # 타원 그리기
        painter.drawEllipse(50, 150, 50, 50)

        painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))
        # RGB 색상으로 브러쉬 설정
        painter.setBrush(QBrush(QColor.fromRgb(178, 178, 178)))
        # 타원 그리기
        painter.drawEllipse(50, 250, 50, 50)

        painter.setPen(QPen(Qt.cyan, 1.0, Qt.SolidLine))
        painter.setBrush(Qt.NoBrush)

        now = QDate.currentDate()

        self.button.setText(now.toString('d.M.yy'))
        self.button.setGeometry(100, 250, 100, 50)

        painter.end()
        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MyApp()
   sys.exit(app.exec_())