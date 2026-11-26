from PyQt6.QtWidgets import *
from pathlib import Path
from yt_download import OutputFormat

class FilePathInput(QLineEdit):

    def __init__(self):
        super().__init__()

    def isValidFilePath(self):
        try:
            path = Path(self.text())
        except:
            return False
        
        if path.exists():
            return True
        else:
            return False


class OutputFileDirectory(FilePathInput):

    def __init__(self):
        super().__init__()
        self.default_path = "./output/"



    

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Zephyr")
        self.resize(300,250)

        layout = QVBoxLayout()

        input = FilePathInput()
        layout.addWidget(input)

        button = QPushButton("Test")
        button.clicked.connect(input.isValidFilePath)
        layout.addWidget(button)

        combo = QComboBox()
        for member in OutputFormat:
            combo.addItem(member.name)
        layout.addWidget(combo)

        widget = QWidget()
        widget.setLayout(layout)
        


        self.setCentralWidget(widget)
        self.show()



