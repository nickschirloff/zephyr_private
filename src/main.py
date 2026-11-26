from PyQt6.QtWidgets import QApplication
from window import Window

if __name__ == "__main__":
    app = QApplication([])
    app_window = Window()
    app.exec()