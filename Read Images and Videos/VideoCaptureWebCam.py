import cv2

#capture from port 0 i.e. laptop's default webcam 
cap = cv2.VideoCapture(0)

#Set height and width (VGA)
cap.set(3,640)
cap.set(4,480)

#Adjust brightness 
cap.set(10,8)


#Display frame by frame
while True:
    success, img = cap.read()
    cv2.imshow("Web Cam",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

