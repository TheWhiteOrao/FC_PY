from navio.mpu9250 import *
from navio.lsm9ds1 import *

print("henllo World")
MPU = MPU9250()

MPU.set_acc_scale(2)

p = MPU.getMotion6()

print(p)
