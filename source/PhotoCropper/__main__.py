from PyQt6.QtWidgets import QApplication
from PhotoCropperApp import PhotoCropperApp
from qt_material import apply_stylesheet

if __name__ == "__main__":
    app = QApplication([])
    window = PhotoCropperApp()
    apply_stylesheet(app, theme='dark_medical.xml')
    window.show()
    app.exec()