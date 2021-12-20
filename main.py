import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img_list = ['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg', 'image5.jpg']
# img3 = cv2.imread('image3.jpg', 0)
img3 = cv2.imread('text_noise.jpg', 0)
# img = cv2.imread(img_list[2])
#wygładzanie zdjęć
# img_3_filter = cv2.threshold(cv2.GaussianBlur(img3, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# img_3_filter = cv2.threshold(cv2.bilateralFilter(img3, 5, 75, 75), 0e, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
#
# img_3_filter = cv2.threshold(cv2.medianBlur(img3, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
#
# img_3_filter = cv2.adaptiveThreshold(cv2.GaussianBlur(img3, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
#
# img_3_filter = cv2.adaptiveThreshold(cv2.bilateralFilter(img3, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
#
# img_3_filter = cv2.adaptiveThreshold(cv2.medianBlur(img3, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

# ret, img_3_filter = cv2.threshold(img3, 120, 255, cv2.THRESH_BINARY +
#                                             cv2.THRESH_OTSU)
# thresh = cv2.threshold(img3, 150, 255, cv2.THRESH_BINARY_INV)[1]
#
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
# img_3_filter = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

thresh = cv2.threshold(img3, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Morph open to remove noise
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
img_3_filter = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)

img_3_filter = cv2.threshold(cv2.medianBlur(img_3_filter, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
img_3_filter = cv2.morphologyEx(img_3_filter, cv2.MORPH_OPEN, kernel, iterations=1)

filename = 'saved_image.jpg'
cv2.imwrite(filename, img_3_filter)
# cv2.imshow('saved_image.jpg')

def read_text(img):
    text = pytesseract.image_to_string(img)
    return text

a = read_text(cv2.imread('saved_image.jpg'))
print(a)