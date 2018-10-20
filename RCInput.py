import sys
import time

import navio.rcinput
import navio.util

navio.util.check_apm()

rcin = navio.rcinput.RCInput()

while (True):
    period_can_0 = rcin.read(0)
    period_can_1 = rcin.read(1)
    period_can_2 = rcin.read(2)
    period_can_3 = rcin.read(3)
    period_can_4 = rcin.read(4)
    period_can_5 = rcin.read(5)
    period_can_6 = rcin.read(6)
    period_can_7 = rcin.read(7)
    period_can_8 = rcin.read(8)

    print("CAN_0: %.6f" % float(period_can_0),
          "CAN_1: %.6f" % float(period_can_1),
          "CAN_2: %.6f" % float(period_can_2),
          "CAN_3: %.6f" % float(period_can_3),
          "CAN_4: %.6f" % float(period_can_4),
          "CAN_5: %.6f" % float(period_can_5),
          "CAN_6: %.6f" % float(period_can_6),
          "CAN_7: %.6f" % float(period_can_7),
          )
    time.sleep(0.01)
