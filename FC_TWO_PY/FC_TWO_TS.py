# import time as tv
# while True:
#     print(tv.time())
#
# print(": {0:20} :".format(1343423.345123))
# g = {0: 1}
# g[0] += 1
# print(g)

from time import *


def usleep(x): return time.sleep(x / 1000000.0)


currenttime = NULL
previoustime = NULL

for i in range(10000000):

    previoustime = currenttime
    currenttime = time_ns()
    delta_time = (currenttime, previoustime) / 1000000

    if delta_time < (1 / 1300):
        usleep((1 / 1300.0 - delta_time) * 1000000)

    currenttime = time_ns()
    delta_time = (currenttime, previoustime) / 1000000
