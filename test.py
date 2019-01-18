import cv2
import numpy as np

imageIzzy = cv2.imread("france.jpg")
image = imageIzzy

# define range of blue color in HSV
lower_green = np.array([140,30,30])
upper_green = np.array([100, 255, 255])

lower_blue = np.array([70,50,0])
upper_blue = np.array([242,255,200])

lower_white = np.array([100,100,100])
upper_white = np.array([255,255,255])
"""
lower_white = np.array([30,0,0])
upper_white = np.array([180,30,255])
"""
lower_black = np.array([60,60,60])
upper_black = np.array([110,100,100])



# Convert BGR to RGB
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    
mask_w = cv2.inRange(hsv, lower_black, upper_black)
image[mask_w != 0] = [255,255,255]
hsv[mask_w != 0] = [255,255,255]
    
mask_w = cv2.inRange(hsv, lower_white, upper_white)
image[mask_w != 0] = [255,255,255]
hsv[mask_w != 0] = [255,255,255]
    
mask_g = cv2.inRange(hsv, lower_green, upper_green)
image[mask_g != 0] = [0,200,0]
hsv[mask_g != 0] = [0,200,0]
    

mask_b = cv2.inRange(hsv, lower_blue, upper_blue)
image[mask_b != 0] = [255,0,0]
hsv[mask_b != 0] = [255,0,0]
    
    
    
cv2.imshow("image avant traitement ", image)
cv2.imwrite("image avant traitement.jpg",image)

    
cv2.waitKey(0)
cv2.destroyAllWindows()