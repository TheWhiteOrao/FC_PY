import sys
import time
from navio.mpu9250 import *
from navio.lsm9ds1 import *
from navio.util import *
import navio.leds
import navio.util

print("Start startup from FC_PY")

navio.util.check_apm()
led = navio.leds.Led()

led.setColor('Red')


time.sleep(2)
print("Startup loaded from FC_PY")


count = 0
while True:
    if count == 200:
        led.setColor("Green")
    elif count == 400:
        led.setColor("Black")
        count = 0

    count += 1
