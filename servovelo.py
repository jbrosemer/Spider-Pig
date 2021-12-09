import time
from adafruit_servokit import ServoKit
# from pynput import keyboard
kit = ServoKit(channels=16)
def servovelo(timeelapsed, prevangle , newangle, servo):
    start = time.time()
    error = newangle - prevangle
    end = start + timeelapsed
    incrementalangle = prevangle
    increment = int(error/timeelapsed)
    print(increment)
    while time.time() < end:
            print(int(time.time()))
            kit.servo[servo].angle = incrementalangle
            incrementalangle = incrementalangle + increment
    kit.servo[servo].angle = newangle


servovelo(5,90,100,0)