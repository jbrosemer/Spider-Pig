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
angle6 = 90
angle8 = 90
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
            if angle1 > 0:
                angle1 -= 1
        if char == ord('l'):
            if angle6 < 180:
                angle6 += 1
        if char == ord('p'):
            if angle6 > 0:
                angle6 -= 1
        if char == ord('k'):
            if angle8 < 180:
                angle8 += 1
        if char == ord('o'):
            if angle8 > 0:
                angle8 -= 1
        kit.servo[outerShoulderLeft].angle = angle0
        kit.servo[outerShoulderRight].angle = angle0
        kit.servo[outerElbowLeft].angle = angle1
        kit.servo[outerElbowRight].angle = angle1
        kit.servo[innerElbowLeft].angle = angle8
        kit.servo[innerShoulderRight].angle = angle6
        #DO A PULLUP
        #SERVOS THAT SHOULD BE PAIRED
        #ALL SHOULDERS TURN CLOCKWISE
        #ALL ELBOWS TURN COUNTERCLOCKWISE
except KeyboardInterrupt:
    curses.nocbreak()
    screen.keypad(False)
    curses.echo()
    curses.endwin()