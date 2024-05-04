import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    # img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # cv2.imshow("Video5", img)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.Canny(img, 150, 150)
    kernel = np.ones( (5,5), np.uint8 )
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    cv2.imshow("Video5", img)
    cv2.waitKey(13)