import cv2
import numpy as np
image = cv2.imread("red_panda.jpg")


blue = (255,0,0)
red = (0,0,255)
green = (0,255,0)
violet = (180,180,0)
yellow = (0,100,100)
white = (255,255,255)
cv2.line(image,(50,30),(450,35),blue,thickness=5)
cv2.circle(image,(240,205),23,red,-1)
cv2.rectangle(image,(50,60),(450,95),green,-1)
cv2.ellipse(image,(250,150),(100,50),0,0,360,violet,-1)
points = np.array([[140,230],[380,230],[320,250],[250,280]],np.int32)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.polylines(image,[points],True,yellow,thickness=3)

cv2.putText(image,"Panda",[20,100],font,3,white,thickness=3)




# shape = image.shape
# print(shape)
cv2.imshow("red panda",image)
cv2.waitKey(0)
cv2.destroyAllWindows()