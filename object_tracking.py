import cv2
cap=cv2.VideoCapture(0)
ret1,frame1= cap.read()
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
gray1 = cv2.GaussianBlur(gray1, (21, 21), 0)
cv2.imshow('window',frame1)
while(True):
    ret2,frame2=cap.read()
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)
    
    deltaframe=cv2.absdiff(gray1,gray2)
    cv2.imshow('delta',deltaframe)
    threshold = cv2.threshold(deltaframe, 25, 255, cv2.THRESH_BINARY)[1]
    threshold = cv2.dilate(threshold,None)
    cv2.imshow('threshold',threshold)
    countour,heirarchy = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i in countour:
        if cv2.contourArea(i) > 10000:
            continue
    
        (x, y, w, h) = cv2.boundingRect(i)
        cv2.rectangle(frame2, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    cv2.imshow('window',frame2)
    
    if cv2.waitKey(20) == 13:
        break
cap.release()
cv2.destroyAllWindows()