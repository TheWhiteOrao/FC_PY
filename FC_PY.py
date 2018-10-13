from navio.mpu9250 import *
from navio.lsm9ds1 import *

print("henllo World")
lsm = LSM9DS1()

print(lsm.getMotion6())
