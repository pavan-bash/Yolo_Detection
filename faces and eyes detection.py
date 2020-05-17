"""import cv2
#img=cv2.imread("C:\\Users\\kanth\\OneDrive\\Desktop\\open cv\\pic.jpg",1)
#print(img)
#cv2.imshow('image',img)
cap=cv2.VideoCapture(0);
while True:
    ret,frame=cap.read()
   # gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
       break
cap.release()
cv2.destroyAllWindows()"""
import cv2
import numpy as np
face_cascade=cv2.CascadeClassifier('D:\yolo_detection\haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('D:\yolo_detection\haarcascade_eye.xml')
#watch_cascade=cv2.CascadeClassifier('C:/Users/kanth/Downloads/opencv-4.0.1-vc14_vc15/data/haarcascades/watch-cascade-12stages.xml')
cap=cv2.VideoCapture(0);
while True:
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    #watches=watch_cascade.detectMultiScale(gray,50,50)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray)
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        cv2.imshow('img',img)
        if cv2.waitKey(1)==27:
        #& 0xFF==ord('s'):
            break
cap.release()
cv2.destroyAllWindows()
