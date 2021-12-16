from adafruit_servokit import ServoKit
import time
# from pynput import keyboard
kit = ServoKit(channels=16)
# SERVO INT DEFINITIONS
# OUTER ARMS
import curses
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
while True:
    servo = input("Please input servo you want to turn: ")
    angle = input("Please input the initial angle: ")
    if isinstance(angle, float):
        break
    while True:
        char = screen.getch()
        if char == ord('q'):
            if angle < 180:
                angle += 1
        if char == ord('a'):
            if angle > 0:
                angle -= 1
        if char == ord('p'):
            break

    kit.servo[servo].angle = angle
    print('Shoulder' + str(angle))

screen.keypad(False)
curses.echo()
curses.endwin()