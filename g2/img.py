import cv2


img  = cv2.imread("cv2_g1_g2/face.jpg")
img = cv2.resize(img, (img.shape[1], img.shape[0]))
# img = cv2.GaussianBlur(img,(23,23), 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.Canny(img, 100, 100)


cv2.imshow("Cat", img)

cv2.waitKey(0)

