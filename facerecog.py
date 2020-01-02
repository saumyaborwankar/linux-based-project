#image processing with scikit learn 2nd jan
#clicking 100 photos with cropped face
import cv2
x=cv2.VideoCapture(0)
i=0
while True:
    ret, photo=x.read()

    #drawing a rectangle with help of diagonal coordinates
    photo=cv2.cvtColor(photo,cv2.COLOR_RGB2GRAY)
    #using pretrained network haar cascade for face detection
    face_model=cv2.CascadeClassifier('frontface_default.com')
    #multi scale gives output as 2D as it detect all the faces and gives the coordinates of all the faces so first bracket 
    #tells us number of faces and inside bracket tells us the coordinates
    
    face_locate=face_model.detectMultiScale(photo)
   
    #prints number of faces
    if len(face_locate)==0:
        cv2.imshow('hello ji',photo)
        if cv2.waitKey(1)==13:
            continue
        
#    first position of array is first face, first number is x1, second position is y1
#    third position is length of x(length of photo) fourth is width of y. so x1+length=x2, and y1+width=y2  
    else :
        if i<100:
        
            #x1=face_locate[0][0]
            #y1=face_locate[0][1]
            #x2=face_locate[0][2]+x1
            #y2=face_locate[0][3]+y1
            x1=210
            y1=120

            x2=436
            y2=370

                #drawing a rectangle with help of diagonal coordinates using rectangle function
            cv2.rectangle(photo, (x1,y1), (x2,y2), (0,255,0),2)


                #displaying the photo/video
            cv2.imwrite("photo{}.jpeg".format(i),photo[y1:y2,x1:x2])
            #cv2.imshow('photo',photo[y1:y2,x1:x2])
            #if cv2.waitKey(1)==13:
            #   break
        else:
            break
    i=i+1        
cv2.destroyAllWindows()
x.release()