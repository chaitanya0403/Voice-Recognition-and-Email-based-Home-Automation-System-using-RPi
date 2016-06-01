import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
for x in range(0,5):
    GPIO.output(7,True)
    time.sleep(2)
    GPIO.output(11,True)
    time.sleep(2)
    GPIO.output(12,True)
    time.sleep(2)
for x in range(0,5):
    GPIO.output(7,False)
    time.sleep(2)
    GPIO.output(11,False)
    time.sleep(2)
    GPIO.output(12,False)
    time.sleep(2)
GPIO.cleanup()