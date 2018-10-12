import cv2, matplotlib
import numpy as np
import matplotlib.pyplot as plt

line = cv2.imread('../images/line_data1.jpg')
line_gray = cv2.cvtColor(line, cv2.COLOR_BGR2GRAY)
line_preprocessed = cv2.GaussianBlur(line_gray, (5, 5), 0)
 
# get binary image
_, line_binary = cv2.threshold(line_preprocessed, 60, 255, cv2.THRESH_BINARY)
 
# invert image to get coins
line_binary = cv2.bitwise_not(line_binary)
plt.imshow(line_binary)
plt.savefig("../images/results/line1_2.png")
