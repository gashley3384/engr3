import rotaryio
import board
import neopixel
import digitalio
from lib.lcd.lcd import LCD
from lib.lcd.i2c_pcf8574_interface import I2CPCF8574Interface

enc = rotaryio.IncrementalEncoder(board.D4, board.D3, divisor=2)

#lcd = LCD(I2CPCF8574Interface(board.I2C(), 0x3f), num_rows=2, num_cols=16)
last_index = None
menu_index = 0
menu = ["stop", "caution", "go"]
led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.3

button = digitalio.DigitalInOut(board.D2)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
button_state = None

while True:
    menu_index = enc.position
    menu_indexlcd = menu_index % 3
    if last_index is None or menu_index is not last_index:
        print(menu[menu_indexlcd])
        last_index = menu_index
    if not button.value and button_state is None:
        button_state = "pressed"
    if button.value and button_state == "pressed":
	    print("Button is pressed")
        button_state = None