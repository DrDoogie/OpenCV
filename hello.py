import cv2
print(cv2.__version__)


import cv2
import matplotlib.pyplot as plt

img = cv2.imread('dog.jpg')
cv2.imshow('img', img)
key = cv2.waitKey(0)  # Wait for any key press
print(key)
cv2.destroyAllWindows()