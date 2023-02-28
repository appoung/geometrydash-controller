import time
import board
import adafruit_hcsr04
import usb_hid
from adafruit_hid.mouse import Mouse
mouse = Mouse(usb_hid.devices)

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP22, echo_pin=board.GP16)

while True:
    try:
        if sonar.distance > 6:
            print("jump")
            mouse.click(Mouse.LEFT_BUTTON)
            
    except RuntimeError:
        print("Retrying!")
