import numpy as np
import cv2 as cv

# Load the image
chess = cv.imread("/home/rakshika/Documents/Computer-Vision_Project/Opencv_24_Nov/Camera_calibration/image.png")

if chess is None:
    print("Error: Unable to load image")
else:
    # Convert the image to grayscale (single channel)
    gray_chess = cv.cvtColor(chess, cv.COLOR_BGR2GRAY)

    # Convert to float32 (required for Harris Corner Detection)
    float_gray_chess = np.float32(gray_chess)

    # Perform Harris Corner Detection
    dst = cv.cornerHarris(src=float_gray_chess, blockSize=2, ksize=3, k=0.04)

    # Normalize and scale the response for better visualization
    dst = cv.dilate(dst, None)  # Optional: Dilation for better visibility
    chess[dst > 0.01 * dst.max()] = [0, 0, 255]  # Mark corners in red

    # Display the result
    cv.imshow("Harris Corners", chess)

    # Wait for a key press and close the window
    cv.waitKey(0)
    cv.destroyAllWindows()
