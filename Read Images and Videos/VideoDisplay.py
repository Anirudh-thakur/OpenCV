import cv2

#Capture video 
cap = cv2.VideoCapture("Sample data/CloakHarryPotter.mp4")

#Display video as sequence of images 

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    #press q to quit and waitkey decides the delay before diplaying next frame i.e. frame rate
    if cv2.waitKey(20) &  0xFF == ord('q'):
        break
