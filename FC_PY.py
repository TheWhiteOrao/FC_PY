from navio.mpu9250 import *
from navio.lsm9ds1 import *

print("henllo World")
MPU = MPU9250()

MPU.WriteReg(1, 1)
MPU.ReadReg(1)
MPU.initialize(100, "BITS_DLPF_CFG_188HZ")
MPU.set_acc_scale("BITS_FS_2G")
MPU.set_gyro_scale("BITS_FS_250DPS")
MPU.read_acc()
MPU.read_gyro()

p = MPU.getMotion6()

print(p)
