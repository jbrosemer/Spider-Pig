from adafruit_servokit import ServoKit
# from pynput import keyboard
kit = ServoKit(channels=16)
# SERVO INT DEFINITIONS
# OUTER ARMS

import curses

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

# OUTER SHOULDERS
outerShoulderLeft = 0
outerShoulderRight = 1

# OUTER ELBOWS
outerElbowLeft = 2
outerElbowRight = 3

# OUTER WRISTS
outerWristLeft = 4
outerWristRight = 5
# INNER ARMS

# INNER SHOULDERS
innerShoulderLeft = 6
innerShoulderRight = 7

# INNER ELBOWS
innerElbowLeft = 8
innerElbowRight = 9

# INNER WRISTS
innerWristLeft = 10
innerWristRight = 11
angle0 = 90
angle1 = 90
angle2 = 90
try:
    kit.servo[outerShoulderLeft].angle = angle0
    while True:
        char = screen.getch()
        if char == ord('q'):
            if angle0 < 180:
                angle0 += 1
        if char == ord('a'):
            if angle0 > 0:
                angle0 -= 1
        if char == ord('s'):
            if angle1 < 180:
                angle1 += 1
        if char == ord('w'):
            if angle0 > 0:
                angle1 -= 1
        kit.servo[outerShoulderLeft].angle = angle0
        kit.servo[outerShoulderRight].angle = angle0
        kit.servo[outerElbowLeft].angle = angle1
        kit.servo[outerElboRight].angle = angle1
except KeyboardInterrupt:
    Servos = 0
    while Servos < 16:
        kit.servo[Servos].angle = 90
        Servos+=1
