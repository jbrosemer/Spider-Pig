from adafruit_servokit import ServoKit
# from pynput import keyboard
kit = ServoKit(channels=16)
# SERVO INT DEFINITIONS
# OUTER ARMS

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
    while True:
        x = input()
        if x == 'a':
            if angle < 180:
                angle += 1
        elif x == 's':
            if angle > 0:
                angle -= 1
        kit.servo[outerShoulderLeft].angle = angle
        print(str(angle))
except KeyboardInterrupt:
    Servos = 0
    while Servos < 16:
        kit.servo[Servos].angle = 90
        Servos+=1
