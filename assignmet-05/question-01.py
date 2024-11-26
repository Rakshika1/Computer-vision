import cv2
import numpy as np

# Load images
image1 = cv2.imread('/home/rakshika/Documents/Computer-Vision_Project/Opencv_24_Nov/Camera_calibration/image.png')
image2 = cv2.imread('/home/rakshika/Documents/Computer-Vision_Project/Opencv_24_Nov/Camera_calibration/image.png')

if image1 is None or image2 is None:
    print("Error: Unable to load one or both images")
else:
    print("Images loaded successfully")

    # Example corresponding points (replace these with the manually picked points)
    pts1 = np.array([[100, 200], [200, 300], [300, 400], [400, 500]], dtype=np.float32)
    pts2 = np.array([[110, 210], [210, 310], [310, 410], [410, 510]], dtype=np.float32)

    # Compute the fundamental matrix
    F, mask = cv2.findFundamentalMat(pts1, pts2, method=cv2.FM_RANSAC)

    print("Fundamental Matrix:\n", F)
