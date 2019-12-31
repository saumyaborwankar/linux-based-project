import cv2
x=cv2.VideoCapture(0)
status, photo = x.read()
cv2.waitKey()
