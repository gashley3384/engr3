import time #librarby
import board
import adafruit_hcsr04
import neopixel
import simpleio

NUMPIXELS = 1  # Update this to match the number of LEDs.
BRIGHTNESS = 0.05 # A number between 0.0 and 1.0, where 0.0 is off, and 1.0 is max.
PIN = board.NEOPIXEL  # This is the default pin on the 5x5 NeoPixel Grid BFF.

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6) #setup for ultrasonic, define pins and stuff

pixels = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=False)#setup for neopixels

blue = 0 #variables for each color to use
red = 0
green = 0

while True:
    try:
        print((sonar.distance)) #tell me how far away object is
        if (sonar.distance>=5 and sonar.distance<20): #red to blue distance
            blue=simpleio.map_range(sonar.distance,5,20,0,255) #blue is highest at 20 lowest at 0
            red=simpleio.map_range(sonar.distance,5,20,255,0) #red is highest at 0 lowest at 20
            green=0 #don't need green, so set it to 0
            pixels.fill((red,green,blue)) #sets each variable as the color it's supposed to be, use rgb order
            pixels.show()# prints values to led
            
        if (sonar.distance>=20 and sonar.distance<35):#blue to green distance
            blue=simpleio.map_range(sonar.distance,20,35,255,0) #same idea as first if except blue is decreasing and green is increasing
            green=simpleio.map_range(sonar.distance,20,35,0,255)
            red=0
            pixels.fill((red,green,blue))#need another print because the first one won't be active if distance isn't in the correct range
            pixels.show()
    except RuntimeError: #don't want it to do anything if it gets an error, so just tell me and move on
        print("Retrying!")
    time.sleep(0.1)

    