import time
import board
import digitalio
from lib.lcd.lcd import LCD
from lib.lcd.i2c_pcf8574_interface import I2CPCF8574Interface #librarby

interruptnum = 0 #number of interrupts

# Set up the photointerrupter using digital pin 2.
photointerrupter = digitalio.DigitalInOut(board.D2)

# Set the photointerrupter as an input.
photointerrupter.direction = digitalio.Direction.INPUT

# Use the internal pull-up resistor. 
photointerrupter.pull = digitalio.Pull.UP

# Set the photointerrupter_state as None for now!
photointerrupter_state = None   

lcd = LCD(I2CPCF8574Interface(board.I2C(), 0x3f), num_rows=2, num_cols=16)

while True:
     print(photointerrupter.value)
     lcd.set_cursor_pos(0,0) #setting where the text is printed on LCD screen
     lcd.print("number interrupt") #what text to write
     lcd.set_cursor_pos(1,0)
     lcd.print("                ")
     lcd.set_cursor_pos(1,0)
     lcd.print(str(interruptnum))#str is string, print the value of interruptnum
     print(interruptnum)
     if not photointerrupter.value and photointerrupter_state is None:# button stuff
          photointerrupter_state = "interrupted"
     if photointerrupter_state is "interrupted" :
          photointerrupter_state = None
     if photointerrupter.value is True:
          interruptnum = interruptnum + 1
     time.sleep(1.5) #deeeeeeebooouuunnnnccceee