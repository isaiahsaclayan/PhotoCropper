import sys
import random
from PyQt6.QtWidgets import QWidget, QPushButton, QFileDialog, QVBoxLayout, QLabel, QGridLayout


class PhotoCropperApp(QWidget):
    def __init__(self):
        super().__init__()

        self.input_dir = ""
        self.output_dir = ""

        self.initializeUI()

    def initializeUI(self):
        self.setWindowTitle("Scan Cropper")
        self.setGeometry(100, 100, 400, 200)

        layout = QGridLayout()

        self.input_button = QPushButton("Select Source Directory")
        self.input_button.clicked.connect(self.open_input_file_dialog)
        layout.addWidget(self.input_button, 0, 0)

        self.output_button = QPushButton("Select Destination Directory")
        self.output_button.clicked.connect(self.open_output_file_dialog)
        layout.addWidget(self.output_button, 0, 1)

        self.input_label= QLabel("Input Directory:")
        layout.addWidget(self.input_label, 1, 0, 1, 2)

        self.output_label = QLabel("Output Directory:")
        layout.addWidget(self.output_label, 2, 0, 1, 2)

        self.crop_button = QPushButton("Crop Images")
        layout.addWidget(self.crop_button, 3, 0, 1, 2)

        self.setLayout(layout)

    def open_input_file_dialog(self):
        path = QFileDialog.getExistingDirectory(self, "Select Source Directory", "")
        if path:
            self.input_dir = path
            self.input_label.setText(f"Input Directory: {self.input_dir}")

    def open_output_file_dialog(self):
        path = QFileDialog.getExistingDirectory(self, "Select Destination Directory", "")
        if path:
            self.output_dir = path
            self.output_label.setText(f"Output Directory: {self.output_dir}")

