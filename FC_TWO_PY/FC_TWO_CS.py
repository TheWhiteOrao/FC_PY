
from FC_TWO_CA import *

#    .LF    1yF    .RF                 1
#
#   -1xL           1xR            6         2
#
#    .LB   -1yB    .RB              5     3

while True:

    in_X = 0.0
    in_Y = 0.0
    smm = ""

    if in_X > 0 and in_Y > 0:
        smm = "RF"
        print("RF")

    elif in_X < 0 and in_Y > 0:
        smm = "LF"
        print("LF")

    elif in_X < 0 and in_Y < 0:
        smm = "LB"
        print("LB")

    elif in_X > 0 and in_Y < 0:
        smm = "RB"
        print("RB")

    if smm == "RF":

        RightFront_R = CA("R")
        print(RightFront_R[0], RightFront_R[1] + abs(in_X), RightFront_R[2], RightFront_R[3] + abs(in_X), CA("R"), abs(in_X))

        RightFront_F = CA("F")
        print(RightFront_F[0], RightFront_F[1] + abs(in_Y), RightFront_F[2], RightFront_F[3] + abs(in_Y), CA("F"), abs(in_Y))

    if smm == "LF":

        LeftBack_L = CA("L")
        print(LeftBack_L[0], LeftBack_L[1] + abs(in_X), LeftBack_L[2], LeftBack_L[3] + abs(in_X), CA("L"), abs(in_X))

        LeftFront_F = CA("F")
        print(LeftFront_F[0], LeftFront_F[1] + abs(in_Y), LeftFront_F[2], LeftFront_F[3] + abs(in_Y), CA("F"), abs(in_Y))

    if smm == "RB":

        RightBack_R = CA("R")
        print(RightBack_R[0], RightBack_R[1] + abs(in_X), RightBack_R[2], RightBack_R[3] + abs(in_X), CA("R"), abs(in_X))

        RightBack_B = CA("B")
        print(RightBack_B[0], RightBack_B[1] + abs(in_Y), RightBack_B[2], RightBack_B[3] + abs(in_Y), RightBack_B[4], RightBack_B[5] + abs(in_Y), CA("B"), abs(in_Y))

    if smm == "LB":

        LeftBack_L = CA("L")
        print(LeftBack_L[0], LeftBack_L[1] + abs(in_X), LeftBack_L[2], LeftBack_L[3] + abs(in_X), CA("L"), abs(in_X))

        LeftBack_B = CA("B")
        print(LeftBack_B[0], LeftBack_B[1] + abs(in_Y), LeftBack_B[2], LeftBack_B[3] + abs(in_Y), LeftBack_B[4], LeftBack_B[5] + abs(in_Y), CA("B"), abs(in_Y))

    break
