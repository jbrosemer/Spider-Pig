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
angle = 90

try:
    kit.servo[outerShoulderLeft].angle = angle
    print(str(angle))
    while True:
        char = screen.getch()
        if char == ord('q'):
            if angle < 180:
                angle += 1
        if char == ord('a'):
            if angle > 0:
                angle -= 1
        kit.servo[outerShoulderLeft].angle = angle
except KeyboardInterrupt:
    Servos = 0
    while Servos < 16:
        kit.servo[Servos].angle = 90
        Servos+=1
