#captures video of the local machine
import cv2
x=cv2.VideoCapture(0)
while True:
    stat,photo=x.read()
    cv2.imshow('/tmp/photo.png',photo)
    if cv2.waitKey(1)==13:
        break
cv2.destroyAllWindows() 
x.release()    