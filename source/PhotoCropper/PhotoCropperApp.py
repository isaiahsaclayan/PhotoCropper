import os.path
import cv2
import subprocess
from PyQt6.QtWidgets import QWidget, QPushButton, QFileDialog, QLabel, QGridLayout
from PyQt6.QtCore import Qt

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

        self.status_label = QLabel("Select source directory")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setStyleSheet("font-size: 16px; color: grey;")
        layout.addWidget(self.status_label, 0, 0, 1, 2)

        self.input_button = QPushButton("Select Source Directory")
        self.input_button.clicked.connect(self.open_input_file_dialog)
        layout.addWidget(self.input_button, 1, 0)

        self.output_button = QPushButton("Select Destination Directory")
        self.output_button.setEnabled(False)
        self.output_button.clicked.connect(self.open_output_file_dialog)
        layout.addWidget(self.output_button, 1, 1)

        self.input_label= QLabel("Input Directory:")
        layout.addWidget(self.input_label, 3, 0, 1, 2)

        self.output_label = QLabel("Output Directory:")
        layout.addWidget(self.output_label, 4, 0, 1, 2)

        self.crop_button = QPushButton("Crop Images")
        self.crop_button.clicked.connect(self.process_images)
        self.crop_button.setEnabled(False)
        layout.addWidget(self.crop_button, 5, 0, 1, 2)

        self.setLayout(layout)

    def open_input_file_dialog(self):
        path = QFileDialog.getExistingDirectory(self, "Select Source Directory", "")
        if path:
            self.input_dir = path
            self.input_label.setText(f"Input Directory: {self.input_dir}")
            self.status_label.setText("Select destination directory")
            self.output_button.setEnabled(True)

    def open_output_file_dialog(self):
        path = QFileDialog.getExistingDirectory(self, "Select Destination Directory", "")
        if path:
            self.output_dir = path
            self.output_label.setText(f"Output Directory: {self.output_dir}")
            self.status_label.setText("Ready to crop images")
            self.crop_button.setEnabled(True)

    def auto_crop(self, image_path, output_path):
        image = cv2.imread(image_path)
        if image is None:
            print(f"Error: Could not read {image_path}")
            return

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 240, 255, cv2.THRESH_BINARY_INV)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(largest_contour)
            padding = 10
            x = max(x - padding, 0)
            y = max(y - padding, 0)
            w = min(w + 2 * padding, image.shape[1] - x)
            h = min(h + 2 * padding, image.shape[0] - y)
            cropped_image = image[y:y + h, x:x + w]
            cv2.imwrite(output_path, cropped_image)
            print(f"Cropped image saved: {output_path}")
        else:
            print(f"No significant content found in {image_path}")

    def process_images(self):
        if not self.input_dir or not self.output_dir:
            print("Please select both input and output folders.")
            return

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        for filename in os.listdir(self.input_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                input_path = os.path.join(self.input_dir, filename)
                output_path = os.path.join(self.output_dir, filename + "_cropped.jpg")
                self.auto_crop(input_path, output_path)

        self.status_label.setText("Cropping complete!")
        self.status_label.setStyleSheet("font-size: 16px; color: green;")

        self.open_output_folder()

    def open_output_folder(self):
        if self.output_dir:
            if os.name == 'nt':
                os.startfile(self.output_dir)
            elif os.name == 'posix':
                subprocess.run(['xdg-open', self.output_dir])