import cv2
import numpy as np

# Load images
image1 = cv2.imread('/home/rakshika/Documents/Computer-Vision_Project/Opencv_24_Nov/img-01.jpeg')
image2 = cv2.imread('/home/rakshika/Documents/Computer-Vision_Project/Opencv_24_Nov/img-01.jpeg')

if image1 is None or image2 is None:
    print("Error: Unable to load one or both images")
else:
    print("Images loaded successfully")

    # Example corresponding points (replace these with the manually picked points)
    pts1 = np.array([[100, 200], [200, 300], [300, 400], [400, 500]], dtype=np.float32)
    pts2 = np.array([[110, 210], [210, 310], [310, 410], [410, 510]], dtype=np.float32)

    # Compute the fundamental matrix
    F, mask = cv2.findFundamentalMat(pts1, pts2, method=cv2.FM_RANSAC)

    if F is None:
        print("Error: Fundamental matrix computation failed")
    else:
        print("Fundamental Matrix:\n", F)

        def draw_epipolar_lines(img1, img2, pts1, pts2, F):
            # Draw epipolar lines in both images
            for pt1, pt2 in zip(pts1, pts2):
                # Calculate the epipolar line in the second image
                line1 = np.dot(F, np.array([pt1[0], pt1[1], 1]))
                x0, y0 = 0, int(-line1[2] / line1[1])
                x1, y1 = img2.shape[1], int(-(line1[2] + line1[0] * img2.shape[1]) / line1[1])
                cv2.line(img2, (x0, y0), (x1, y1), (0, 255, 0), 1)

                # Similarly, calculate epipolar line for the second image and draw it on the first image
                line2 = np.dot(F.T, np.array([pt2[0], pt2[1], 1]))
                x0, y0 = 0, int(-line2[2] / line2[1])
                x1, y1 = img1.shape[1], int(-(line2[2] + line2[0] * img1.shape[1]) / line2[1])
                cv2.line(img1, (x0, y0), (x1, y1), (0, 255, 0), 1)

        # Example usage
        draw_epipolar_lines(image1, image2, pts1, pts2, F)
