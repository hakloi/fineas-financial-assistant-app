from PyQt6.QtWidgets import QApplication
from main_window import MainWindow

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.setStyleSheet("QMainWindow {background: 'white';}")
    window.show()
    app.exec()
