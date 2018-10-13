import sys

import navio.leds
import time
import navio.util

navio.util.check_apm()

led = navio.leds.Led()

led.setColor('Yellow')
print("LED is yellow")
time.sleep(1)

while (True):

    led.setColor('Black')
    print("LED is Black")
    time.sleep(0.05)

    led.setColor('Red')
    print("LED is Red")
    time.sleep(0.05)

    led.setColor('Green')
    print("LED is Green")
    time.sleep(0.05)

    led.setColor('Blue')
    print("LED is Blue")
    time.sleep(0.05)

    led.setColor('Cyan')
    print("LED is Cyan")
    time.sleep(0.05)

    led.setColor('Magenta')
    print("LED is Magenta")
    time.sleep(0.05)

    led.setColor('Yellow')
    print("LED is Yellow")
    time.sleep(0.05)

    led.setColor('White')
    print("LED is White")
    time.sleep(0.05)
