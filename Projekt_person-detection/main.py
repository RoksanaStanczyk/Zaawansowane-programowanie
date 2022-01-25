import glob
import cv2
from detectByPathImage import detectByPathImage

for path in glob.glob('.\\images\\*'):
    print(path)
    detectByPathImage(path)
    cv2.waitKey(0)
