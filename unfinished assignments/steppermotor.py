import asyncio
import board
import keypad
import time
import digitalio
from adafruit_motor import stepper 

DELAY = 0.01
STEPS = 100

coils = (
    digitalio.DigitalInOut(board.D9),  # A1
    digitalio.DigitalInOut(board.D10), # A2
    digitalio.DigitalInOut(board.D11), # B1
    digitalio.DigitalInOut(board.D12), # B2
)

for coil in coils:
    coil.direction = digitalio.Direction.OUTPUT

motor = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)

async def catch_pin_transitions(pin):
    # Print a message when pin goes low and when it goes high.
        with keypad.Keys((pin,), value_when_pressed=False) as keys:
            while True:
                event = keys.events.get()
                if event:
                    if event.pressed:
                        print("Limit Switch was pressed.")
                    elif event.released:
                        print("Limit Switch was released.")
                await asyncio.sleep(0)

async def main():
    interrupt_task = asyncio.create_task(catch_pin_transitions(board.D2))
    await asyncio.gather(interrupt_task)


asyncio.run(main())
