import cv2

#Read image
img = cv2.imread("Sample data/1.jpg")

#Show image
cv2.imshow("Output",img)


#wait for key press to close the image 
cv2.waitKey(0)
