import cv2
vcapture = cv2.VideoCapture(0) 
while True:
    ret, frame = vcapture.read()
    if ret == True:
        grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edge = cv2.Canny(grayscale, 75, 125)
        cv2.imshow('Edge frame', edge)
    if cv2.waitKey(20) == 13:
        break
    
vcapture.release()
cv2.destroyAllWindows()