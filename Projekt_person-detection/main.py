import glob
import cv2
import imutils as imutils
import datetime
from detectByPathImage import detectByPathImage

for path in glob.glob('.\\images\\*'):
    print(path)
    detectByPathImage(path)
    cv2.waitKey(0)
