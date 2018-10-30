class AHRS:

    def __init__(self, arg):
        self.arg = arg

    q0 = 1
    q1 = 0
    q2 = 0
    q3 = 0
    twoKi = 0
    twoKp = 2
    gyroOffset = {0: 0, 1: 0, 2: 0}

    def setGyroOffset(offsetX, offsetY, offsetZ):
        AHRS.gyroOffset[0] = offsetX
        AHRS.gyroOffset[1] = offsetY
        AHRS.gyroOffset[2] = offsetZ

    def update(AccX, AccY, AccZ, GyrX, GyrY, GyrZ, MagX, MagY, MagZ, delta_time):

        # Use IMU algorithm if magnetometer measurement invalid (avoids NaN in magnetometer normalisation)
        if MagX == 0.0 and MagY == 0.0 and MagZ == 0.0:
            updateIMU(GyrX, GyrY, GyrZ, AccX, AccY, AccZ, delta_time)

        # Compute feedback only if accelerometer measurement valid(avoids NaN in accelerometer normalisation)
        if not AccX == 0.0 and AccY == 0.0 and AccZ == 0.0:

            # Normalise accelerometer measurement
            recipNorm = (AccX * AccX + AccY * AccY + AccZ * AccZ) ** -0.5
            AccX *= recipNorm
            AccY *= recipNorm
            AccZ *= recipNorm

            # Normalise magnetometer measurement
            recipNorm = (MagX * MagX + MagY * MagY + MagZ * MagZ) ** -0.5
            MagX *= recipNorm
            MagY *= recipNorm
            MagZ *= recipNorm

            # Auxiliary variables to avoid repeated arithmetic
            q0q0 = q0 * q0
            q0q1 = q0 * q1
            q0q2 = q0 * q2
            q0q3 = q0 * q3
            q1q1 = q1 * q1
            q1q2 = q1 * q2
            q1q3 = q1 * q3
            q2q2 = q2 * q2
            q2q3 = q2 * q3
            q3q3 = q3 * q3


AHRS.setGyroOffset(0, 1, 3)
AHRS.test(2)
