import os
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
from PhotoCropper.PhotoCropperApp import PhotoCropperApp
from qt_material import apply_stylesheet

if __name__ == "__main__":
    app = QApplication([])
    icon_path = os.path.join(os.path.dirname(__file__), '../resources/assets/icon.ico')
    app.setWindowIcon(QIcon(icon_path))

    window = PhotoCropperApp()
    apply_stylesheet(app, theme='dark_amber.xml')
    window.show()

    app.exec()