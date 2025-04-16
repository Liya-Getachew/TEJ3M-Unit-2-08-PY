"""
Created by: Liya Getachew
Created: 08/04/25

Move a servo with a potentiometer in sync
"""

import time
import board
import pwmio
import servo
from analogio import AnalogIn


# sets servo pulse width modulation on Pin 16
pwm = pwmio.PWMOut(board.GP16, duty_cycle=2 ** 15, frequency=50)

# sets potentiometer pin to pin 26 (analog pin 0)
potentionmeter = AnalogIn(board.GP26)

# Creates a servo object called my_servo
my_servo = servo.Servo(pwm, min_pulse = 650, max_pulse = 2500)

while True:
    print((potentionmeter.value))
    potentiometer_value = potentionmeter.value

    # shows value of the potentiometer
    print(potentiometer_value)

    # changes potentiometer range from 0-65535 to 0-180
    angle = potentiometer_value * (180/65535)

    # set servo angle value to match potentiometer value
    my_servo.angle = angle
    time.sleep(1)
