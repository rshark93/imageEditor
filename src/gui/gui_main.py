# Created by Roman Sharkovich 4.02.2022

import sys

from PIL import Image, ImageQt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QVBoxLayout, QApplication
from PySide6.QtWidgets import QWidget, QLabel


class ImageViewer(QWidget):

    def __init__(self, image_path):
        QWidget.__init__(self)
        self.setWindowTitle("PyQt Image Viewer")
        self._image_path = image_path

        # Open up image in Pillow
        image = Image.open(self._image_path)
        qt_image = ImageQt.ImageQt(image)
        pixmap = QPixmap.fromImage(qt_image)

        self.image_label = QLabel('')
        self.image_label.setPixmap(pixmap)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.image_label)
        self.setLayout(self.main_layout)


if __name__ == "__main__":
    image_path = "test_img/Lenna_.png"
    app = QApplication(sys.argv)
    viewer = ImageViewer(image_path)
    viewer.show()
    app.exec_()
