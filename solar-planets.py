import cv2
img = cv2.imread("PRO-104-Project-Image-main\solar-system.jpg")

cv2.putText(img,  
           "Sun",
           (20, 300),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Mercury",
           (100, 300),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Venus",
           (200, 300),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Earth",
           (300, 300),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Mars",
           (400, 300),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Jupiter",
           (500, 300),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Saturn",
           (700, 300),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Uranus",
           (950, 300),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Neptune",
           (1100, 300),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )





cv2.imshow("output",img)

cv2.waitKey(0)
cv2.imwrite("SolarSystemNames.jpg",img)