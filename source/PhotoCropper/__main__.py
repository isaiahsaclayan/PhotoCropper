from PyQt6.QtWidgets import QApplication
from PhotoCropperApp import PhotoCropperApp

if __name__ == "__main__":
    app = QApplication([])
    window = PhotoCropperApp()
    window.show()
    app.exec()