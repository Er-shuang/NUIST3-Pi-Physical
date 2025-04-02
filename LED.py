# Author: Nie Yujin
# Date: 2/4/25
# Some code to switch the LED on, using the RPi.GPIO library

# using RPi.GPIO library
import RPi.GPIO as GPIO
# import time library so that pause the script later on
import time

# Tell the program which convention is to be used
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

# trun on the LED
print("LED on")
# provide power of 3.3V
GPIO.output(18,GPIO.HIGH) # red LED

# Pause the program for 1 second
time.sleep(1)

# turn off the LED
print("LED off")
# do not supply any power
GPIO.output(18,GPIO.LOW)
