from navio.mpu9250 import *
from navio.lsm9ds1 import *

print("henllo World")
MPU = MPU9250()

MPU.initialize(100, "BITS_DLPF_CFG_256HZ_NOLPF2")
MPU.set_acc_scale("BITS_FS_2G")
MPU.set_gyro_scale("BITS_FS_250DPS")

p = MPU.getMotion6()

print(p)
