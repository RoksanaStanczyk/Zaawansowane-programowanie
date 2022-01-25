import cv2
import imutils
from detect import detect


def detectByPathImage(path):
    image = cv2.imread(path)
    image = imutils.resize(image, width=min(800, image.shape[1]))
    result_image = detect(image)
    return result_image
