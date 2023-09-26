import time
import board
import adafruit_hcsr04
import neopixel
import simpleio

NUMPIXELS = 1  # Update this to match the number of LEDs.
BRIGHTNESS = 0.05 # A number between 0.0 and 1.0, where 0.0 is off, and 1.0 is max.
PIN = board.NEOPIXEL  # This is the default pin on the 5x5 NeoPixel Grid BFF.

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

pixels = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=False)

blue = 0
red = 0
green = 0

while True:
    try:
        print((sonar.distance))
        if (sonar.distance>=5 and sonar.distance<20):
            blue=simpleio.map_range(sonar.distance,5,20,0,255)
            red=simpleio.map_range(sonar.distance,5,20,255,0)
            green=0
            pixels.fill((red,green,blue))
            pixels.show()
            
        if (sonar.distance>=20 and sonar.distance<35):
            blue=simpleio.map_range(sonar.distance,20,35,255,0)
            red=0
            pixels.fill((red,green,blue))
            pixels.show()
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)

    