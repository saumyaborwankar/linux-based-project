#clicks a photo and saves the photo locally
import cv2
x=cv2.VideoCapture(0)
stat,photo=x.read()
cv2.imwrite('/tmp/photo.png',photo)
cv2.waitKey()
cv2.destroyAllWindows() 
x.release()    