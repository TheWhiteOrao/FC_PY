import sys
import time

import navio.rcinput
import navio.util

navio.util.check_apm()

rcin = navio.rcinput.RCInput()

while (True):
    period = rcin.read(1)
    print(period)
    time.sleep(0.01)
