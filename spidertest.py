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
angle0 = 90
try:
    while True:
        char = screen.getch()

        if char == ord('q'):
            if angle0 < 180:
                angle0 += 1
        if char == ord('a'):
            if angle0 > 0:
                angle0 -= 1

        kit.servo[outerElbowLeft].angle = angle0
except KeyboardInterrupt:
    curses.nocbreak()
    screen.keypad(False)
    curses.echo()
    curses.endwin()