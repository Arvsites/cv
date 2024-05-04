import cv2


cap = cv2.VideoCapture("cv2_g1_g2/istockphoto-1258621982-640_adpp_is.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("asdfasjldfjasj1235kd2134hfkashdf", img)

    if cv2.waitKey(1) and 0xFF == ord("q"):
        break