import os
import sys
import ctypes
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
from PhotoCropper.PhotoCropperApp import PhotoCropperApp
from qt_material import apply_stylesheet

if __name__ == "__main__":
    # Create the application
    app = QApplication([])

    # Set Windows App ID for taskbar icon
    if sys.platform.startswith('win'):
        myappid = 'isaiahsaclayan.photocropper'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    # Set application icon
    icon_path = os.path.join(os.path.dirname(__file__), '../resources/assets/icon.ico')
    app.setWindowIcon(QIcon(icon_path))

    # Create and show the main window
    window = PhotoCropperApp()
    apply_stylesheet(app, theme='dark_amber.xml')
    window.show()

    # Execute the application
    sys.exit(app.exec())