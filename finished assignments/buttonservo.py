import time
import board
import pwmio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

btn = DigitalInOut(board.D6) #assign digital pins to buttons
btn.direction = Direction.INPUT
btn.pull = Pull.DOWN 
btn2 = DigitalInOut(board.D2)
btn2.direction = Direction.INPUT
btn2.pull = Pull.DOWN

angle = 90 #starter angle to declare variable

while True:#like void loop for arduino, if btn.value is saying if button is pressed
    if btn.value and angle > 5: # only running this loop when it's above 5 keeps angle from going out of range
        print(angle)    
        angle = angle -5 #make angle variable lower
        my_servo.angle = angle #set servo angle to variable
        time.sleep(0.05)
    if btn2.value and angle < 170:# keeps angle from going out of range on the other end
        print(angle)
        angle = angle + 5 
        my_servo.angle = angle #moving servo in the other direction
        time.sleep(0.05)



    time.sleep(0.1) # sleep for debounce