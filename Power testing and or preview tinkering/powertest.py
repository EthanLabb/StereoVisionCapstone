from PyQt6.QtWidgets import QApplication
import sys

screen = QApplication(sys.argv).primaryScreen()
size = screen.size()
width = size.width()
height = size.height()

from picamera2 import Picamera2, Preview
from libcamera import Transform
#cam 1 preview with test width+heights,idk
cam1 = Picamera2(0)
cam1.start_preview(Preview.QTGL, x=0, y=0, width=width*2/3, height=height*1/3)
cam1.start()

#cam 2 preview with test width+heights,idk
cam2 = Picamera2(1)
cam2.start_preview(Preview.QTGL, x=width*2/3, y=height*1/3, width=width*2/3, height=height*1/3)
cam2.start()
