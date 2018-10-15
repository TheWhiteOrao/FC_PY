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

mup = navio.mpu9250.MPU9250()
mup.initialize()

lsm = navio.lsm9ds1.LSM9DS1()
lsm.initialize()


time.sleep(2)
print("Startup loaded from FC_PY")

count = 0
while True:
    if count == 200000:
        led.setColor("Green")
    elif count == 400000:
        led.setColor("Black")
        count = 0

    gm6 = mup.getMotion6()
    time.sleep(0.01)

    gm9 = mup.getMotion9()
    time.sleep(0.01)

    print(gm6, gm9)
    count += 1
