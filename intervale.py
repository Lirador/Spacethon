import cv2
import numpy as np

def isInColorRange(bvr,b1,v1,r1,b2,v2,r2):
    if(bvr[0]<=b2 and bvr[0]>=b1 and bvr[1]<=v2 and bvr[1]>=v1 and bvr[2]<=r2 and bvr[2]>=r1):
        return True
    else :
        return False


imageBrut = cv2.imread("test9.jpg")


image = imageBrut[0:320, 110:513]

height, width, channels = image.shape       

"""
nbPixel=0
lowPixel=228
lineLowPixel = 0

blackPixLeft= 0
blackPixRight=0
for o in range(0,width):
    if(isInColorRange(image[160,o],0,0,0,45,45,45)):
        if(o < width/2):
            blackPixLeft+=1
        if(o >width/2):
            blackPixRight+=1
    
"""  
"""
for i in range(0,height): 
    for o in range(0,width):
        if(isInColorRange(image[i,o],0,0,0,45,45,45)):
            nbPixel +=1
            image[i,o] = [0,255,0]
        if(o == width-1):
            print("Ligne : " + str(i) + " nbPixel : "+ str(nbPixel))
            if(lowPixel > nbPixel):
                lowPixel = nbPixel
                lineLowPixel = i
            nbPixel=0   
        
    """

"""
lower_limit = np.array([90,90,90])
upper_limit = np.array([90,90,90])
for i in range(0,20):
    for o in range(0,20):
        if(image[i,o][0] < lower_limit[0]):
            lower_limit[0] = image[i,o][0]
        
        elif(image[i,o][0] > upper_limit[0]):
            upper_limit[0] = image[i,o][0]
        
        if(image[i,o][1] < lower_limit[1]):
            lower_limit[1] = image[i,o][1]
        elif(image[i,o][1] > upper_limit[1]):
            upper_limit[1] = image[i,o][1]
        
        if(image[i,o][2] < lower_limit[2]):
            lower_limit[2] = image[i,o][2]
        elif(image[i,o][2] > upper_limit[2]):
            upper_limit[2] = image[i,o][2]  

        
        
        
        print(image[i,o][0])
            
    
print("Upper_limit = "+ str(upper_limit))
print("lower_limit = "+ str(lower_limit))


# define range of blue color in HSV
lower_green = np.array([0,8,5])
upper_green = np.array([90, 255, 255])

lower_blue = np.array([70,50,0])
upper_blue = np.array([242,255,200])

lower_white = np.array([30,0,0])
upper_white = np.array([180,30,255])

upper_black = np.array([50,70,30])
lower_black = np.array([0,0,0])

"""
"""
lower_black = np.array([60,60,60])
upper_black = np.array([110,100,100])
"""
"""

# Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    


# Threshold the HSV image to get only blue colors


mask_g = cv2.inRange(hsv, lower_green, upper_green)
image[mask_g != 0] = [0,200,0]
hsv[mask_g != 0] = [0,200,0]

mask_b = cv2.inRange(hsv, lower_blue, upper_blue)
image[mask_b != 0] = [255,0,0]
hsv[mask_b != 0] = [255,0,0]

mask_w = cv2.inRange(hsv, lower_white, upper_white)
image[mask_w != 0] = [255,255,255]
hsv[mask_w != 0] = [255,255,255]



# Algo inplane cloud or bad pixel remover




# Bitwise-AND mask and original image

#res_w = cv2.bitwise_and(image,image, mask=mask_w)

#res_b = cv2.bitwise_and(image, image, mask= mask_b)
#res_g = cv2.bitwise_and(image, image, mask= mask_g)
"""


cv2.imshow("resultat", image)

cv2.imwrite( "result_mercator-projection.jpg", image);

#cv2.imwrite( "result/result_green.jpg", res_b);
#cv2.imwrite( "result/result_white.jpg", res_w);

cv2.waitKey(0)
cv2.destroyAllWindows()