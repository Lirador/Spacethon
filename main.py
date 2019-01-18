import cv2
import numpy as np



image = cv2.imread("test4.jpg")

height, width, channels = image.shape

def inRange(bvr,bvr1,bvr2):
    if(bvr[0]<=bvr2[0]and bvr[0]>=bvr1[0]and bvr[1]<=bvr2[1]and bvr[1]>=bvr1[1]and bvr[2]<=bvr2[2]and bvr[2]>=bvr1[2]):
        return True

def isInGray(bvr):
    ecart = 15
    if(bvr[0]<= bvr[1]+ecart and bvr[0]>= bvr[1]-ecart and bvr[0]<= bvr[2]+ecart and bvr[0]>= bvr[2]-ecart and bvr[1]<= bvr[0]+ecart and bvr[1]>= bvr[0]-ecart and bvr[1]<= bvr[2]+ecart and bvr[1]>= bvr[2]-ecart and bvr[2]<= bvr[0]+ecart and bvr[2]>= bvr[0]-ecart and bvr[2]<=bvr[1]+ecart and bvr[2]>= bvr[1]-ecart):
        return True
    



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
lower_black = np.array([60,60,60])
upper_black = np.array([110,100,100])
"""


# Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    


# Threshold the HSV image to get only blue colors
nbPixGray = 0
for i in range(0,height-1):
    for o in range(0,width-1):

        if(isInGray(image[i,o])):
            nbPixGray+=1
            image[i,o] = [0,0,255]
            
print((nbPixGray*100)/(height*width))
if((nbPixGray*100)/(height*width) >= 50):
    print("L'image est inutilisable")

        
            
"""
mask_w = cv2.inRange(hsv, lower_white, upper_white)
image[mask_w != 0] = [255,255,255]
hsv[mask_w != 0] = [255,255,255]

mask_g = cv2.inRange(hsv, lower_green, upper_green)
image[mask_g != 0] = [0,200,0]
hsv[mask_g != 0] = [0,200,0]

mask_b = cv2.inRange(hsv, lower_blue, upper_blue)
image[mask_b != 0] = [255,0,0]
hsv[mask_b != 0] = [255,0,0]
"""



# Algo inplane cloud or bad pixel remover




# Bitwise-AND mask and original image

#res_w = cv2.bitwise_and(image,image, mask=mask_w)

#res_b = cv2.bitwise_and(image, image, mask= mask_b)
#res_g = cv2.bitwise_and(image, image, mask= mask_g)



cv2.imshow("resultat", image)

cv2.imwrite( "result_mercator-projection.jpg", image);

#cv2.imwrite( "result/result_green.jpg", res_b);
#cv2.imwrite( "result/result_white.jpg", res_w);

cv2.waitKey(0)
cv2.destroyAllWindows()