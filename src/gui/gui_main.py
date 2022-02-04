# Created by Roman Sharkovich 4.02.2022

import sys

from PySide6.QtWidgets import QApplication
#from PySide6.examples.widgets.imageviewer.imageviewer import ImageViewer
from image_viewer import ImageViewer

if __name__ == "__main__":
    image_path = "test_img/Lenna_.png"
    app = QApplication(sys.argv)
    viewer = ImageViewer(image_path)
    viewer.show()
    app.exec_()
