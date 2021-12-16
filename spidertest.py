from adafruit_servokit import ServoKit
import time
# from pynput import keyboard
kit = ServoKit(channels=16)
# SERVO INT DEFINITIONS
# OUTER ARMS

import curses
first = True
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
"""
angle0 = 58
angle1 = 125
angle2 = 117
"""
angle3 = 90
angle4 = 90
angle5 = 90
angle6 = 90
#outerleftshoulder 58
#outerleftelbow 125
#outerleftwrist 117
#innerleftwrist 171
#
try:
    while True:
        char = screen.getch()

        if char == ord('q'):
            if angle4 < 180:
                angle4 += 1
        if char == ord('a'):
            if angle4 > 0:
                angle4 -= 1
        if char == ord('s'):
            if angle5 < 180:
                angle5 += 1
        if char == ord('w'):
            if angle5 > 0:
                angle5 -= 1
        if char == ord('d'):
            if angle6 < 180:
                angle6 += 1
        if char == ord('e'):
            if angle6 > 0:
                angle6 -= 1
        if first:
            kit.servo[innerShoulderLeft].angle = angle4
            print(angle4)
            time.sleep(1)
            kit.servo[innerElbowLeft].angle = angle5
            print(angle5)
            time.sleep(1)
            kit.servo[innerWristLeft].angle = angle6
            print(angle6)
            time.sleep(1)
        first = False
        kit.servo[innerShoulderLeft].angle = angle4
        print('Shoulder' + str(angle4))
        kit.servo[innerElbowLeft].angle = angle5
        print('elbow' + str(angle5))
        kit.servo[innerWristRight].angle = angle6
        print('Wrist' + str(angle6))

except KeyboardInterrupt:
    curses.nocbreak()
    screen.keypad(False)
    curses.echo()
    curses.endwin()