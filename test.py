import sys
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow

app = QApplication(sys.argv)

window = QMainWindow()
window.setFixedSize(QSize(1200, 700))
window.setWindowTitle("Fineas - financial assistant")
window.show()

app.exec()

