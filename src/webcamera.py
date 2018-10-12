import os
import cv2
import numpy as np
def capture_camera(mirror=False):
    cap = cv2.VideoCapture(0) 

    while True:
        ret, frame = cap.read()

        if mirror is True:
            frame = frame[:,::-1]

        frame = cv2.resize(frame, (600, 200))
        line_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        line_preprocessed = cv2.GaussianBlur(line_gray, (5, 5), 0)
         
        _, line_binary = cv2.threshold(line_preprocessed, 60, 255, cv2.THRESH_BINARY)
        left_sum = np.sum(line_binary.T[0:299])
        right_sum = np.sum(line_binary.T[300:599])

        print(frame)
        if left_sum > right_sum:
            print("右へ進め")
        elif left_sum < right_sum:
            print("左へ進め")
        else:
            print("分からない")

        if !os.environ['HOME'] == "/home/pi": 
            cv2.imshow('camera capture', line_gray)

        k = cv2.waitKey(1) 
        if k == 27: 
            break
    if !os.environ['HOME'] == "/home/pi":
        cap.release()
        cv2.destroyAllWindows()

capture_camera()
