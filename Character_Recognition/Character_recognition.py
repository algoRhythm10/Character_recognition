import cv2
import pytesseract
import numpy as np


#accessing the image that is to be converted to text
img = cv2.imread('C:\\Users\\Rhythm\\OneDrive\\Desktop\\Character_Recognition\\Test_images\\sample.png')


# Alternatively: can be skipped if you have a Blackwhite image
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
gray, img_bin = cv2.threshold(gray,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
gray = cv2.bitwise_not(img_bin)


#np.ones() method returns a new array of given shape and type, filled with ones
kernel = np.ones((2, 1), np.uint8)


#cv2.erode() method is used to perform erosion on the image
img = cv2.erode(gray, kernel, iterations=1)


#cv2.dilate() method is used to detach two connected objects etc.
img = cv2.dilate(img, kernel, iterations=1)


#accessing tesseract from its location 
pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\Rhythm\AppData\\Local\\Tesseract-OCR\\tesseract.exe'


#using tesseract to convert the text from image to a string value and printing it
out_below = pytesseract.image_to_string(img)


print("OUTPUT:",out_below)