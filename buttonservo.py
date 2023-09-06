import time
import board
import pwmio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

btn = DigitalInOut(board.D6)
btn.direction = Direction.INPUT
btn.pull = Pull.DOWN 
btn2 = DigitalInOut(board.D2)
btn2.direction = Direction.INPUT
btn2.pull = Pull.DOWN

angle = 1

while True:
    if btn.value:
        print(angle)
        angle = angle -5
        my_servo.angle = angle 
        time.sleep(0.05)
    if btn2.value:
        print(angle)
        angle = angle + 5
        my_servo.angle = angle
        time.sleep(0.05)



    time.sleep(0.1) # sleep for debounce