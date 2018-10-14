from navio.mpu9250 import *
from navio.lsm9ds1 import *

print("henllo World")
MPU = MPU9250()


a = MPU.read_acc()
g = MPU.read_gyro()


print(a, g)
