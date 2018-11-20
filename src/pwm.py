import RPi.GPIO as GPIO
import time
import Adafruit_PCA9685

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

while True:
    #val = int(input("> "))
    #pwm.set_pwm(0, 0, 600)
   # time.sleep(1)
    pwm.set_pwm(8, 0, 1000)
    time.sleep(2)
    pwm.set_pwm(9, 0, 1000)
    time.sleep(2)
    #pwm.set_pwm(1, 0, 100)



