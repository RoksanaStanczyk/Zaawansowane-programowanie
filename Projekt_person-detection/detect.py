import datetime
import cv2

HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


def detect(frame):
    bounding_box_cordinates, weights = HOGCV.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.05)
    start = datetime.datetime.now()
    person = 0
    for x, y, w, h in bounding_box_cordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        person += 1

    cv2.imshow('Person detection', frame)
    print(f'Znaleziono {person} osób na zdjęciu')
    print("Czas detekcji: {}s".format(
        (datetime.datetime.now() - start).total_seconds()))
    return frame
