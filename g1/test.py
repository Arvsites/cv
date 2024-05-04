import cv2
import numpy as np

img = np.zeros((500,500,3), dtype='uint8')

# img [100:150, 300:380] = 193,149,68
cv2.rectangle(img, (30,70), (100,100), (255,100,50), thickness=1)
cv2.rectangle(img, (130,170), (200,200), (200,50,50), thickness=cv2.FILLED)

cv2.line(img, (30,70), (200,200), (0,0,255), thickness=1)
cv2.circle(img, (90,90), 90, (0,255,0), thickness=1)
cv2.putText(img, "My text", (100,200), cv2.FONT_HERSHEY_TRIPLEX, 1, (0,0,255), 1)

cv2.imshow("IMG", img)
cv2.waitKey(0)
