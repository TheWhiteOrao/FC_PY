import sys
import time
from navio.mpu9250 import *
from navio.lsm9ds1 import *
from navio.util import *
import navio.leds
import navio.util

print("Load START FC_PY")

navio.util.check_apm()
led = navio.leds.Led()

led.setColor('Red')


time.sleep(5)
print("Loadet START FC_PY")

while True:
    led.setColor("Green")
    led.setColor("Black")
