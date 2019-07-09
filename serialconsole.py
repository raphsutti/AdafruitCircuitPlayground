# Windows 10 
# Find COM number from device manager
# Download PuTTy
# Use serial connection type, enter COM# and change speed to baud rate of 115200

import board
import digitalio
import time
 
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT
 
while True:
    print("Hello, CircuitPython!")
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)