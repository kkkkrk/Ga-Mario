# 04.pyqt_key_event.py
# Ptqt 키 이벤트
import sys
from  PyQt5.QtWidgets import QApplication, QWidget, QLabel

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1024,768)
        self.setWindowTitle('GA Mario')
        self.show()

        self.label_text = QLabel

    #키를 누를 때
    def keyPressEvent(self, event):
        key = event.key()
        self.label_text.setText(str(key) + ' press')
        self.label_text.setGeometry(200, 150, 50, 100)

    # 키를 뗄 때
    def keyReleaseEvent(self, event):
        key = event.key()
        print(str(key) + ' release')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())