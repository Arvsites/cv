import cv2

img = cv2.imread('img/2.jpg')
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = cv2.CascadeClassifier('eye.xml')
results = faces.detectMultiScale(img2, scaleFactor=1.1, minNeighbors=4)

print(results)

for (x,y,w,h) in results:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), thickness=3)

cv2.imshow("Face", img)
cv2.waitKey(0)