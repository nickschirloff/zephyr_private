from PyQt6.QtWidgets import *
from pathlib import Path
from yt_download import OutputFormat
from dl_options import DLOptions, default_options
from yt_download import VideoDL
options = default_options
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

class DownloadWidget(QWidget):

    has_link_error = False
    has_output_folder_error = False

    def __init__(self):
        super().__init__()

        #has_error

        layout = QVBoxLayout()

        link_input = QLineEdit()
        link_error_label = QLabel("Error with Link")
        link_error_label.setStyleSheet("color: red")
        layout.addWidget(link_input)
        layout.addWidget(link_error_label)

        output_folder_input = FilePathInput()
        output_folder_error_label = QLabel("Error with output directory")
        output_folder_error_label.setStyleSheet("color: red")
        layout.addWidget(output_folder_input)
        layout.addWidget(output_folder_error_label)

        self.setLayout(layout)



class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Zephyr")
        self.resize(650,550)

        layout = QVBoxLayout()

        dl_widget = DownloadWidget()
        layout.addWidget(dl_widget)


        input = FilePathInput()
        layout.addWidget(input)

        button = QPushButton("Test")
        button.clicked.connect(input.isValidFilePath)
        layout.addWidget(button)

        button2 = QPushButton("Test2")
        button2.clicked.connect(self.download_vid)
        layout.addWidget(button2)

        combo = QComboBox()
        for member in OutputFormat:
            combo.addItem(member.name)
        layout.addWidget(combo)

        self.check = QCheckBox(text="test")
        self.check.stateChanged.connect(self.onStateChanged)
        layout.addWidget(self.check)

        widget = QWidget()
        widget.setLayout(layout)
        


        self.setCentralWidget(widget)
        self.show()

    def download_vid(self):
        temp = VideoDL(options)
        temp.download("https://www.youtube.com/watch?v=5FV8sHNUTAI")
        print("done")

    def onStateChanged(self):
        if self.check.isChecked():
            options["noplaylist"] = True
            self.check.setText("Checked")
        else:
            self.check.setText("Unchecked")
            options["noplaylist"] = False

        print(options)


