import cv2
import os
import time
import numpy as np
import Adafruit_PCA9685
import RPi.GPIO as GPIO

# 0 1 2 sorvp
# 3 ~ A dc motor
# 3 right-front front

# 6 left-front back
# 7 right-back back
# 8 right-back front
# 9 left-back front
# 10(A) left-back back
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

cap = cv2.VideoCapture(0) 

def go_stright(val):
    pwm.set_pwm(8, 0, val)
    time.sleep(0.5)
    pwm.set_pwm(9, 0, val)
    time.sleep(0.5)

def go_left(val):
    pwm.set_pwm(8, 0, val)
    time.sleep(0.5)
    pwm.set_pwm(9, 0, 0)
    time.sleep(0.5)

def go_right(val):
    pwm.set_pwm(9, 0, val)
    time.sleep(0.5)
    pwm.set_pwm(8, 0, 0)
    time.sleep(0.5)
    
while True:
    #val = int(input("> "))
    #pwm.set_pwm(0, 0, 600)
   # time.sleep(1)
    #pwm.set_pwm(1, 0, 100)
    ret, frame = cap.read()

    frame = cv2.resize(frame, (600, 200))
    line_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    line_preprocessed = cv2.GaussianBlur(line_gray, (5, 5), 0)
     
    _, line_binary = cv2.threshold(line_preprocessed, 60, 255, cv2.THRESH_BINARY)
    left_sum = np.sum(line_binary.T[0:299])
    right_sum = np.sum(line_binary.T[300:599])

    if left_sum > right_sum:
        print("右へ進め")
        go_left(900)
    elif left_sum < right_sum:
        go_right(900)
        print("左へ進め")
    else:
        go_stright(300)
        print("分からない")

    if not os.environ['HOME'] == "/home/pi": 
        cv2.imshow('camera capture', line_gray)

    k = cv2.waitKey(1) 
    if k == 27: 
        break
if not os.environ['HOME'] == "/home/pi":
    cap.release()
    cv2.destroyAllWindows()



