# Created by: Brennan Lee
# Created on: April 2025
#
# This program turns a servo motor from 0 to 180 degrees and repeats

import time
import board
import pwmio
from adafruit_motor import servo

# constants
SLEEP_TIME = 0.05

# create a PWMOut object on pin GP12
pwm = pwmio.PWMOut(board.GP12, duty_cycle=2 ** 15, frequency=50)

# create a servo object, called my_servo
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees 5 degrees at a time
        my_servo.angle = angle
        time.sleep(SLEEP_TIME)
    for angle in range(180, 0, -5): # 180 - 0 degrees 5 degrees at a time
        my_servo.angle = angle
        time.sleep(SLEEP_TIME)
