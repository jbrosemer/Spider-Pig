from adafruit_servokit import ServoKit
# from pynput import keyboard
kit = ServoKit(channels=16)
# SERVO INT DEFINITIONS
# OUTER ARMS
import time
import curses

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

# OUTER SHOULDERS
outerShoulderLeft = 0
outerShoulderRight = 9

# OUTER ELBOWS
outerElbowLeft = 1
outerElbowRight = 10

# OUTER WRISTS
outerWristLeft = 2
outerWristRight = 11
# INNER ARMS

# INNER SHOULDERS
innerShoulderLeft = 3
innerShoulderRight = 6

# INNER ELBOWS
innerElbowLeft = 4
innerElbowRight = 7

# INNER WRISTS
innerWristLeft = 5
innerWristRight = 8


angle0 = 58
angle1 = 125
angle2 = 117
angle3 = 180
angle4 = 27
angle5 = 90
angle6 = 0
angle7 = 150
angle8 = 72
angle9 = 45
angle10 = 65
angle11 = 47
#outerleftshoulder 58
#outerleftelbow 122
#outerleftwrist 117
#innerleftshoulder 180
#innerleftelbow 27
#innerleftwrist 90
#innerrightshoulder 0
#innerrightelbow 150
#innerrightwrist 72
#outerrightshoulder 45
#outerrightelbow 65
#outerrightwrist 47
"""
angle10 = 90
angle11 = 90
"""
first = True
try:
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

        if char == ord('d'):
            if angle2 < 180:
                angle2 += 1
        if char == ord('e'):
            if angle2 > 0:
                angle2 -= 1

        if char == ord('f'):
            if angle3 < 180:
                angle3 += 1
        if char == ord('r'):
            if angle3 > 0:
                angle3 -= 1

        if char == ord('g'):
            if angle4 < 180:
                angle4 += 1
        if char == ord('t'):
            if angle4 > 0:
                angle4 -= 1

        if char == ord('h'):
            if angle5 < 180:
                angle5 += 1
        if char == ord('y'):
            if angle5 > 0:
                angle5 -= 1

        if char == ord('j'):
            if angle6 < 180:
                angle6 += 1
        if char == ord('u'):
            if angle6 > 0:
                angle6 -= 1

        if char == ord('k'):
            if angle7 < 180:
                angle7 += 1
        if char == ord('i'):
            if angle7 > 0:
                angle7 -= 1

        if char == ord('l'):
            if angle8 < 180:
                angle8 += 1
        if char == ord('o'):
            if angle8 > 0:
                angle8 -= 1

        if char == ord('z'):
            if angle9 < 180:
                angle9 += 1
        if char == ord('x'):
            if angle9 > 0:
                angle9 -= 1

        if char == ord('c'):
            if angle10 < 180:
                angle10 += 1
        if char == ord('v'):
            if angle10 > 0:
                angle10 -= 1

        if char == ord('b'):
            if angle11 < 180:
                angle11 += 1
        if char == ord('n'):
            if angle11 > 0:
                angle11 -= 1

        if first:
            kit.servo[outerShoulderLeft].angle = angle0
            time.sleep(1)
            
            kit.servo[outerElbowLeft].angle = angle1
            time.sleep(1)
            kit.servo[outerWristLeft].angle = angle2
            time.sleep(1)

            kit.servo[innerShoulderLeft].angle = angle3
            time.sleep(1)
            kit.servo[innerElbowLeft].angle = angle4
            time.sleep(1)
            kit.servo[innerWristLeft].angle = angle5
            time.sleep(1)

            kit.servo[innerShoulderRight].angle = angle6
            time.sleep(1)
            kit.servo[innerElbowRight].angle = angle7
            time.sleep(1)
            kit.servo[innerWristRight].angle = angle8
            time.sleep(1)

            kit.servo[outerShoulderRight].angle = angle9
            time.sleep(1)
            kit.servo[outerElbowRight].angle = angle10
            time.sleep(1)
            kit.servo[outerWristRight].angle = angle11
            time.sleep(1)

        first = False
        kit.servo[outerShoulderLeft].angle = angle0

        kit.servo[outerElbowLeft].angle = angle1
        kit.servo[outerWristLeft].angle = angle2

        kit.servo[innerShoulderLeft].angle = angle3
        kit.servo[innerElbowLeft].angle = angle4
        kit.servo[innerWristLeft].angle = angle5

        kit.servo[innerShoulderRight].angle = angle6
        kit.servo[innerElbowRight].angle = angle7
        kit.servo[innerWristRight].angle = angle8

        kit.servo[outerShoulderRight].angle = angle9
        kit.servo[outerElbowRight].angle = angle10
        kit.servo[outerWristRight].angle = angle11
        #DO A PULLUP
        #SERVOS THAT SHOULD BE PAIRED
        #ALL SHOULDERS TURN CLOCKWISE
        #ALL ELBOWS TURN COUNTERCLOCKWISE
except KeyboardInterrupt:
    curses.nocbreak()
    screen.keypad(False)
    curses.echo()
    curses.endwin()