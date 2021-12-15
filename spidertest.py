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
angle4 = 90
angle5 = 90
angle6 = 90
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
            kit.servo[outerShoulderLeft].angle = angle4
            print(angle4)
            time.sleep(1)
            kit.servo[outerElbowLeft].angle = angle5
            print(angle5)
            time.sleep(1)
            kit.servo[outerWristLeft].angle = angle6
            print(angle6)
            time.sleep(1)
        first = False
        kit.servo[outerShoulderLeft].angle = angle4
        print('Shoulder' + str(angle4))
        kit.servo[outerElbowLeft].angle = angle5
        print('elbow' + str(angle5))
        kit.servo[outerWristLeft].angle = angle6
        print('Wrist' + str(angle6))
except KeyboardInterrupt:
    curses.nocbreak()
    screen.keypad(False)
    curses.echo()
    curses.endwin()