import sys
import time
from navio.leds import *
from navio.mpu9250 import *
from navio.lsm9ds1 import *
from navio.util import *

check_apm()

# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
#
# ██ ████████     ██       ██████   █████  ██████  ███████     ████████ ██   ██ ███████     ███████ ████████  █████  ██████  ████████ ██    ██ ██████
# ██    ██        ██      ██    ██ ██   ██ ██   ██ ██             ██    ██   ██ ██          ██         ██    ██   ██ ██   ██    ██    ██    ██ ██   ██
# ██    ██        ██      ██    ██ ███████ ██   ██ ███████        ██    ███████ █████       ███████    ██    ███████ ██████     ██    ██    ██ ██████
# ██    ██        ██      ██    ██ ██   ██ ██   ██      ██        ██    ██   ██ ██               ██    ██    ██   ██ ██   ██    ██    ██    ██ ██
# ██    ██        ███████  ██████  ██   ██ ██████  ███████        ██    ██   ██ ███████     ███████    ██    ██   ██ ██   ██    ██     ██████  ██
#
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████

print("It Loads the Startup")
led = Led()
led.setColor('Red')

# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
#
# ██ ███    ██ ██ ████████ ██  █████  ██      ██ ███████ ███████     ███    ███ ██████  ██    ██  █████  ██████  ███████  ██████
# ██ ████   ██ ██    ██    ██ ██   ██ ██      ██    ███  ██          ████  ████ ██   ██ ██    ██ ██   ██      ██ ██      ██  ████
# ██ ██ ██  ██ ██    ██    ██ ███████ ██      ██   ███   █████       ██ ████ ██ ██████  ██    ██  ██████  █████  ███████ ██ ██ ██
# ██ ██  ██ ██ ██    ██    ██ ██   ██ ██      ██  ███    ██          ██  ██  ██ ██      ██    ██      ██ ██           ██ ████  ██
# ██ ██   ████ ██    ██    ██ ██   ██ ███████ ██ ███████ ███████     ██      ██ ██       ██████   █████  ███████ ███████  ██████
#
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████

MPU9250 = MPU9250()
MPU9250.initialize()

# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
#
# ██ ███    ██ ██ ████████ ██  █████  ██      ██ ███████ ███████     ██      ███████ ███    ███  █████  ██████  ███████  ██
# ██ ████   ██ ██    ██    ██ ██   ██ ██      ██    ███  ██          ██      ██      ████  ████ ██   ██ ██   ██ ██      ███
# ██ ██ ██  ██ ██    ██    ██ ███████ ██      ██   ███   █████       ██      ███████ ██ ████ ██  ██████ ██   ██ ███████  ██
# ██ ██  ██ ██ ██    ██    ██ ██   ██ ██      ██  ███    ██          ██           ██ ██  ██  ██      ██ ██   ██      ██  ██
# ██ ██   ████ ██    ██    ██ ██   ██ ███████ ██ ███████ ███████     ███████ ███████ ██      ██  █████  ██████  ███████  ██
#
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████

LSM9DS1 = LSM9DS1()
LSM9DS1.initialize()

# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
#
# ███████ ████████  █████  ██████  ████████ ██    ██ ██████      ██       ██████   █████  ██████  ███████ ██████
# ██         ██    ██   ██ ██   ██    ██    ██    ██ ██   ██     ██      ██    ██ ██   ██ ██   ██ ██      ██   ██
# ███████    ██    ███████ ██████     ██    ██    ██ ██████      ██      ██    ██ ███████ ██   ██ █████   ██   ██
#      ██    ██    ██   ██ ██   ██    ██    ██    ██ ██          ██      ██    ██ ██   ██ ██   ██ ██      ██   ██
# ███████    ██    ██   ██ ██   ██    ██     ██████  ██          ███████  ██████  ██   ██ ██████  ███████ ██████
#
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████

print("Startup loaded")

# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
#
# ███    ███  █████  ██ ███    ██     ██    ██  █████  ██      ██    ██ ███████ ███████
# ████  ████ ██   ██ ██ ████   ██     ██    ██ ██   ██ ██      ██    ██ ██      ██
# ██ ████ ██ ███████ ██ ██ ██  ██     ██    ██ ███████ ██      ██    ██ █████   ███████
# ██  ██  ██ ██   ██ ██ ██  ██ ██      ██  ██  ██   ██ ██      ██    ██ ██           ██
# ██      ██ ██   ██ ██ ██   ████       ████   ██   ██ ███████  ██████  ███████ ███████
#
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████

number_of_cycles = 0
G_SI = 9.80665
PI = 3.14159

q0 = 1
q1 = 0
q2 = 0
q3 = 0
twoKi = 0
twoKp = 2

# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
#
# ███    ███  █████  ██ ███    ██     ██████  ██████   ██████   ██████  ██████   █████  ███    ███ ███    ███
# ████  ████ ██   ██ ██ ████   ██     ██   ██ ██   ██ ██    ██ ██       ██   ██ ██   ██ ████  ████ ████  ████
# ██ ████ ██ ███████ ██ ██ ██  ██     ██████  ██████  ██    ██ ██   ███ ██████  ███████ ██ ████ ██ ██ ████ ██
# ██  ██  ██ ██   ██ ██ ██  ██ ██     ██      ██   ██ ██    ██ ██    ██ ██   ██ ██   ██ ██  ██  ██ ██  ██  ██
# ██      ██ ██   ██ ██ ██   ████     ██      ██   ██  ██████   ██████  ██   ██ ██   ██ ██      ██ ██      ██
#
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████


def update():
    # Get Motion of the sensor MPU9250
    MPU9250_AGM = MPU9250.getMotion9()

    MPU9250_ACC = MPU9250_AGM[0]  # X:, Y:, Z:, accelerometer_data of MPU9250
    MPU9250_GYR = MPU9250_AGM[1]  # X:, Y:, Z:, gyroscope_data of MPU9250
    MPU9250_MAG = MPU9250_AGM[2]  # X:, Y:, Z:, magnetometer_data of MPU9250

    MPU9250_ACC_x = MPU9250_ACC[0]  # MPU9250 accelerometer_x_data
    MPU9250_ACC_y = MPU9250_ACC[1]  # MPU9250 accelerometer_y_data
    MPU9250_ACC_z = MPU9250_ACC[2]  # MPU9250 accelerometer_z_data

    MPU9250_GYR_x = MPU9250_GYR[0]  # MPU9250 gyroscope_x_data
    MPU9250_GYR_y = MPU9250_GYR[1]  # MPU9250 gyroscope_y_data
    MPU9250_GYR_z = MPU9250_GYR[2]  # MPU9250 gyroscope_z_data

    MPU9250_MAG_x = MPU9250_MAG[0]  # MPU9250 magnetometer_x_data
    MPU9250_MAG_y = MPU9250_MAG[1]  # MPU9250 magnetometer_y_data
    MPU9250_MAG_z = MPU9250_MAG[2]  # MPU9250 magnetometer_z_data

    # Use IMU algorithm if magnetometer measurement invalid (avoids NaN in magnetometer normalisation)
    if (MPU9250_MAG_x == 0.0 and MPU9250_MAG_y == 0.0 and MPU9250_MAG_z == 0.0):
        print("updateIMU_MPU9250()")

    # Compute feedback only if accelerometer measurement valid (avoids NaN in accelerometer normalisation)
    if not (MPU9250_ACC_x == 0.0 and MPU9250_ACC_y == 0.0 MPU9250_ACC_z == 0.0):

        # Normalise accelerometer measurement
        recipNorm = (MPU9250_ACC_x * MPU9250_ACC_x + MPU9250_ACC_y * MPU9250_ACC_y + MPU9250_ACC_z * MPU9250_ACC_z) ** -0.5
        MPU9250_ACC_x *= recipNorm
        MPU9250_ACC_y *= recipNorm
        MPU9250_ACC_z *= recipNorm

        # Normalise magnetometer measurement
        recipNorm = (MPU9250_MAG_x * MPU9250_MAG_x + MPU9250_MAG_y * MPU9250_MAG_y + MPU9250_MAG_z * MPU9250_MAG_z) ** -0.5
        MPU9250_MAG_x *= recipNorm
        MPU9250_MAG_y *= recipNorm
        MPU9250_MAG_z *= recipNorm

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

        # Reference direction of Earth's magnetic field
        hx = 2.0 * (MPU9250_MAG_x * (0.5 - q2q2 - q3q3) + MPU9250_MAG_y * (q1q2 - q0q3) + MPU9250_MAG_z * (q1q3 + q0q2))
        hy = 2.0 * (MPU9250_MAG_x * (q1q2 + q0q3) + MPU9250_MAG_y * (0.5 - q1q1 - q3q3) + MPU9250_MAG_z * (q2q3 - q0q1))
        bx = (hx * hx + hy * hy) ** 0.5
        bz = 2.0 * (MPU9250_MAG_x * (q1q3 - q0q2) + MPU9250_MAG_y * (q2q3 + q0q1) + MPU9250_MAG_z * (0.5 - q1q1 - q2q2))

        # Estimated direction of gravity and magnetic field
        halfvx = q1q3 - q0q2
        halfvy = q0q1 + q2q3
        halfvz = q0q0 - 0.5 + q3q3
        halfwx = bx * (0.5 - q2q2 - q3q3) + bz * (q1q3 - q0q2)
        halfwy = bx * (q1q2 - q0q3) + bz * (q0q1 + q2q3)
        halfwz = bx * (q0q2 + q1q3) + bz * (0.5 - q1q1 - q2q2)

        # Error is sum of cross product between estimated direction and measured direction of field vectors
        halfex = (MPU9250_ACC_y * halfvz - MPU9250_ACC_z * halfvy) + (MPU9250_MAG_y * halfwz - MPU9250_MAG_z * halfwy)
        halfey = (MPU9250_ACC_z * halfvx - MPU9250_ACC_x * halfvz) + (MPU9250_MAG_z * halfwx - MPU9250_MAG_x * halfwz)
        halfez = (MPU9250_ACC_x * halfvy - MPU9250_ACC_y * halfvx) + (MPU9250_MAG_x * halfwy - MPU9250_MAG_y * halfwx)

        # Compute and apply integral feedback if enabled
        if twoKi > 0.0:
            integralFBx += twoKi * halfex * dt  # integral error scaled by Ki
            integralFBy += twoKi * halfey * dt
            integralFBz += twoKi * halfez * dt
            MPU9250_GYR_x += integralFBx  # apply integral feedback
            MPU9250_GYR_y += integralFBy
            MPU9250_GYR_z += integralFBz
        else:
            integralFBx = 0.0  # prevent integral windup
            integralFBy = 0.0
            integralFBz = 0.0

        # Apply proportional feedback
        MPU9250_GYR_x += twoKp * halfex
        MPU9250_GYR_y += twoKp * halfey
        MPU9250_GYR_z += twoKp * halfez

    # Integrate rate of change of quaternion
    MPU9250_GYR_x *= (0.5 * dt)  # pre-multiply common factors
    MPU9250_GYR_y *= (0.5 * dt)
    MPU9250_GYR_z *= (0.5 * dt)
    qa = q0
    qb = q1
    qc = q2
    q0 += (-qb * MPU9250_GYR_x - qc * MPU9250_GYR_y - q3 * MPU9250_GYR_z)
    q1 += (qa * MPU9250_GYR_x + qc * MPU9250_GYR_z - q3 * MPU9250_GYR_y)
    q2 += (qa * MPU9250_GYR_y - qb * MPU9250_GYR_z + q3 * MPU9250_GYR_x)
    q3 += (qa * MPU9250_GYR_z + qb * MPU9250_GYR_y - qc * MPU9250_GYR_x)

    # Normalise quaternion
    recipNorm = invSqrt(q0 * q0 + q1 * q1 + q2 * q2 + q3 * q3)
    q0 *= recipNorm
    q1 *= recipNorm
    q2 *= recipNorm
    q3 *= recipNorm

    print(MPU9250_ACC_x,
          MPU9250_ACC_y,
          MPU9250_ACC_z,
          MPU9250_GYR_x,
          MPU9250_GYR_y,
          MPU9250_GYR_z,
          MPU9250_MAG_x,
          MPU9250_MAG_y,
          MPU9250_MAG_z)


def updateIMU_MPU9250():
    # Get Motion of the sensor MPU9250
    MPU9250_AGM = MPU9250.getMotion9()

    MPU9250_ACC = MPU9250_AGM[0]  # X:, Y:, Z:, accelerometer_data of MPU9250
    MPU9250_GYR = MPU9250_AGM[1]  # X:, Y:, Z:, gyroscope_data of MPU9250
    MPU9250_MAG = MPU9250_AGM[2]  # X:, Y:, Z:, magnetometer_data of MPU9250

    MPU9250_ACC_x = MPU9250_ACC[0]  # MPU9250 accelerometer_x_data
    MPU9250_ACC_y = MPU9250_ACC[1]  # MPU9250 accelerometer_y_data
    MPU9250_ACC_z = MPU9250_ACC[2]  # MPU9250 accelerometer_z_data

    MPU9250_GYR_x = MPU9250_GYR[0]  # MPU9250 gyroscope_x_data
    MPU9250_GYR_y = MPU9250_GYR[1]  # MPU9250 gyroscope_y_data
    MPU9250_GYR_z = MPU9250_GYR[2]  # MPU9250 gyroscope_z_data

    MPU9250_ACC_x /= G_SI
    MPU9250_ACC_y /= G_SI
    MPU9250_ACC_z /= G_SI
    MPU9250_GYR_x *= (180 / PI) * 0.0175
    MPU9250_GYR_y *= (180 / PI) * 0.0175
    MPU9250_GYR_z *= (180 / PI) * 0.0175

    MPU9250_GYR_x -= gyroOffset[0]
    MPU9250_GYR_y -= gyroOffset[1]
    MPU9250_GYR_z -= gyroOffset[2]

    # Compute feedback only if accelerometer measurement valid (avoids NaN in accelerometer normalisation)
    if not (MPU9250_ACC_x == 0.0 and MPU9250_ACC_y == 0.0 MPU9250_ACC_z == 0.0):

        # Normalise accelerometer measurement
        recipNorm = invSqrt(MPU9250_ACC_x * MPU9250_ACC_x + MPU9250_ACC_y * MPU9250_ACC_y + MPU9250_ACC_z * MPU9250_ACC_z)
        MPU9250_ACC_x *= recipNorm
        MPU9250_ACC_y *= recipNorm
        MPU9250_ACC_z *= recipNorm

        # Estimated direction of gravity and vector perpendicular to magnetic flux
        halfvx = q1 * q3 - q0 * q2
        halfvy = q0 * q1 + q2 * q3
        halfvz = q0 * q0 - 0.5 + q3 * q3

        # Error is sum of cross product between estimated and measured direction of gravity
        halfex = (MPU9250_ACC_y * halfvz - MPU9250_ACC_z * halfvy)
        halfey = (MPU9250_ACC_z * halfvx - MPU9250_ACC_x * halfvz)
        halfez = (MPU9250_ACC_x * halfvy - MPU9250_ACC_y * halfvx)

        # Compute and apply integral feedback if enabled
        if (twoKi > 0.0):
            integralFBx += twoKi * halfex * dt  # integral error scaled by Ki
            integralFBy += twoKi * halfey * dt
            integralFBz += twoKi * halfez * dt
            MPU9250_GYR_x += integralFBx  # apply integral feedback
            MPU9250_GYR_y += integralFBy
            MPU9250_GYR_z += integralFBz

        else:
            integralFBx = 0.0  # prevent integral windup
            integralFBy = 0.0
            integralFBz = 0.0

        # Apply proportional feedback
        MPU9250_GYR_x += twoKp * halfex
        MPU9250_GYR_y += twoKp * halfey
        MPU9250_GYR_z += twoKp * halfez

    # Integrate rate of change of quaternion
    MPU9250_GYR_x *= (0.5 * dt)		# pre-multiply common factors
    MPU9250_GYR_y *= (0.5 * dt)
    MPU9250_GYR_z *= (0.5 * dt)
    qa = q0
    qb = q1
    qc = q2
    q0 += (-qb * MPU9250_GYR_x - qc * MPU9250_GYR_y - q3 * MPU9250_GYR_z)
    q1 += (qa * MPU9250_GYR_x + qc * MPU9250_GYR_z - q3 * MPU9250_GYR_y)
    q2 += (qa * MPU9250_GYR_y - qb * MPU9250_GYR_z + q3 * MPU9250_GYR_x)
    q3 += (qa * MPU9250_GYR_z + qb * MPU9250_GYR_y - qc * MPU9250_GYR_x)
    # Normalise quaternion
    recipNorm = invSqrt(q0 * q0 + q1 * q1 + q2 * q2 + q3 * q3)
    q0 *= recipNorm
    q1 *= recipNorm
    q2 *= recipNorm
    q3 *= recipNorm

    print(MPU9250_ACC_x,
          MPU9250_ACC_y,
          MPU9250_ACC_z,
          MPU9250_GYR_x,
          MPU9250_GYR_y,
          MPU9250_GYR_z)

    # Get Motion of the sensor LSM9DS1
LSM9DS1_AGM = LSM9DS1.getMotion9()

LSM9DS1_ACC = LSM9DS1_AGM[0]  # X:, Y:, Z:, accelerometer_data of LSM9DS1
LSM9DS1_GYR = LSM9DS1_AGM[1]  # X:, Y:, Z:, gyroscope_data of LSM9DS1
LSM9DS1_MAG = LSM9DS1_AGM[2]  # X:, Y:, Z:, magnetometer_data of LSM9DS1

LSM9DS1_ACC_x = LSM9DS1_ACC[0]  # LSM9DS1 accelerometer_x_data
LSM9DS1_ACC_y = LSM9DS1_ACC[1]  # LSM9DS1 accelerometer_y_data
LSM9DS1_ACC_z = LSM9DS1_ACC[2]  # LSM9DS1 accelerometer_z_data

LSM9DS1_GYR_x = LSM9DS1_GYR[0]  # LSM9DS1 gyroscope_x_data
LSM9DS1_GYR_y = LSM9DS1_GYR[1]  # LSM9DS1 gyroscope_y_data
LSM9DS1_GYR_z = LSM9DS1_GYR[2]  # LSM9DS1 gyroscope_z_data

LSM9DS1_MAG_x = LSM9DS1_MAG[0]  # LSM9DS1 magnetometer_x_data
LSM9DS1_MAG_y = LSM9DS1_MAG[1]  # LSM9DS1 magnetometer_y_data
LSM9DS1_MAG_z = LSM9DS1_MAG[2]  # LSM9DS1 magnetometer_z_data

# print(("accelerometer_data:" + "x: %.6f" % (gm9[0][0]), "y: %.6f" % (gm9[0][1]), "z: %.6f" % (gm9[0][2])),
#       ("gyroscope_data:" + "x: %.6f" % (gm9[1][0]), "y: %.6f" % (gm9[1][1]), "z: %.6f" % (gm9[1][2])),
#       ("magnetometer_data:" + "x: %.6f" % (gm9[2][0]), "y: %.6f" % (gm9[2][1]), "z: %.6f" % (gm9[2][2])))
# print(("accelerometer_data:" + "x: %.6f" % (lgm9[0][0]), "y: %.6f" % (lgm9[0][1]), "z: %.6f" % (lgm9[0][2])),
#       ("gyroscope_data:" + "x: %.6f" % (lgm9[1][0]), "y: %.6f" % (lgm9[1][1]), "z: %.6f" % (lgm9[1][2])),
#       ("magnetometer_data:" + "x: %.6f" % (lgm9[2][0]), "y: %.6f" % (lgm9[2][1]), "z: %.6f" % (lgm9[2][2])))
#

while True:

                # Visual view that the program is running
    if number_of_cycles == 200:
        led.setColor("Green")

    elif number_of_cycles == 400:
        led.setColor("Black")
        number_of_cycles = 0

    update()

    time.sleep(0.01)
    count += 1
