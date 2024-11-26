import cv2
import numpy as np

image = cv2.imread("flag.png")
print(image.shape)
cv2.imshow("Flag",image)
cv2.waitKey(0)
cv2.destroyAllWindow()