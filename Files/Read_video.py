import cv2 
import numpy as np
cap = cv2.VideoCapture("red_panda_snow.mp4")
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("flipped_red_panda.avi",fourcc,25,(640,360))
try:
    while True:
        ret,frame = cap.read()
        print(frame.shape)
        frame2 = cv2.flip(frame,1)
        cv2.imshow("frame2",frame2)

        out.write(frame2)
        # gray_scale = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # cv2.imshow("frame",frame)
        # cv2.imshow("frame",gray_scale)
        key=cv2.waitKey(30)
        if key == 27:
            break
finally:
    out.realse()
    cap.release()
    cv2.destroyAllWindows()

