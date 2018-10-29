# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
#
#  ██████  ██████  ███    ██ ████████ ██████   ██████  ██           █████  ██       ██████   ██████  ██████  ██ ████████ ██   ██ ███    ███
# ██      ██    ██ ████   ██    ██    ██   ██ ██    ██ ██          ██   ██ ██      ██       ██    ██ ██   ██ ██    ██    ██   ██ ████  ████
# ██      ██    ██ ██ ██  ██    ██    ██████  ██    ██ ██          ███████ ██      ██   ███ ██    ██ ██████  ██    ██    ███████ ██ ████ ██
# ██      ██    ██ ██  ██ ██    ██    ██   ██ ██    ██ ██          ██   ██ ██      ██    ██ ██    ██ ██   ██ ██    ██    ██   ██ ██  ██  ██
#  ██████  ██████  ██   ████    ██    ██   ██  ██████  ███████     ██   ██ ███████  ██████   ██████  ██   ██ ██    ██    ██   ██ ██      ██
#
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████

from decimal import *
from FC_TWO_COS import *

# initialize COS


def CA(direction="", force_of_rotors=10000, radius_of_rotors=500):  # "F","L","R","B"

    # calculate CA
    getcontext().prec = 16

    basic_lever_act = force_of_rotors * radius_of_rotors

    rotor_rig_bacX_5 = COS(54) * radius_of_rotors
    rotor_rig_bacY_5 = COS(36) * radius_of_rotors

    rotor_rig_froX_6 = COS(18) * radius_of_rotors
    rotor_rig_froY_6 = COS(72) * radius_of_rotors

    rotor_mid_froX_1 = COS(90) * radius_of_rotors
    rotor_mid_froY_1 = COS(00) * radius_of_rotors

    rotor_lef_froX_2 = COS(18) * radius_of_rotors
    rotor_lef_froY_2 = COS(72) * radius_of_rotors

    rotor_lef_bacX_3 = COS(54) * radius_of_rotors
    rotor_lef_bacY_3 = COS(36) * radius_of_rotors

    #

    lever_act_rig_bacX_5 = basic_lever_act / rotor_rig_bacX_5
    lever_act_rig_bacY_5 = basic_lever_act / rotor_rig_bacY_5

    lever_act_rig_froX_6 = basic_lever_act / rotor_rig_froX_6
    lever_act_rig_froY_6 = basic_lever_act / rotor_rig_froY_6

    # lever_act_mid_froX_1 = basic_lever_act / rotor_mid_froX_1 # is not need for calculate
    lever_act_mid_froY_1 = basic_lever_act / rotor_mid_froY_1

    lever_act_lef_froX_2 = basic_lever_act / rotor_lef_froX_2
    lever_act_lef_froY_2 = basic_lever_act / rotor_lef_froY_2

    lever_act_lef_bacX_3 = basic_lever_act / rotor_lef_bacX_3
    lever_act_lef_bacY_3 = basic_lever_act / rotor_lef_bacY_3

    #

    percent_rig_bacX_5 = lever_act_rig_bacX_5 / lever_act_mid_froY_1
    percent_rig_bacY_5 = lever_act_rig_bacY_5 / lever_act_mid_froY_1

    percent_rig_froX_6 = lever_act_rig_froX_6 / lever_act_mid_froY_1
    percent_rig_froY_6 = lever_act_rig_froY_6 / lever_act_mid_froY_1

    # percent_mid_froX_1 = lever_act_mid_froX_1 / lever_act_mid_froY_1 # can't divide by zero
    percent_mid_froY_1 = lever_act_mid_froY_1 / lever_act_mid_froY_1

    percent_lef_froX_2 = lever_act_lef_froX_2 / lever_act_mid_froY_1
    percent_lef_froY_2 = lever_act_lef_froY_2 / lever_act_mid_froY_1

    percent_lef_bacX_3 = lever_act_lef_bacX_3 / lever_act_mid_froY_1
    percent_lef_bacY_3 = lever_act_lef_bacY_3 / lever_act_mid_froY_1

    # to the Right
    sideways_rig_lef_bacX_3 = percent_lef_bacX_3 / 2
    sideways_rig_lef_froX_2 = percent_lef_froX_2 / 2

    # to the Left
    sideways_left_rig_bacX_5 = percent_rig_bacX_5 / 2
    sideways_left_rig_froX_6 = percent_rig_froX_6 / 2

    # Forward
    forward_lef_bacY_3 = percent_lef_bacY_3 / 2
    forward_rig_bacY_5 = percent_rig_bacY_5 / 2

    # Backward
    backward_lef_froY_2 = percent_lef_froY_2 / 3
    backward_mid_froY_1 = percent_mid_froY_1 / 3
    backward_rig_froY_6 = percent_rig_froY_6 / 3

    # returns COS
    if direction == "F":
        return sideways_left_rig_bacX_5, sideways_left_rig_froX_6
    elif direction == "B":
        return backward_lef_froY_2, backward_mid_froY_1, backward_rig_froY_6
    elif direction == "L":
        return sideways_left_rig_bacX_5, sideways_left_rig_froX_6
    elif direction == "R":
        return sideways_rig_lef_bacX_3, sideways_rig_lef_froX_2
    else:
        print("not def return, try \"F\" \"L\" \"R\" \"B\" ")


if __name__ == '__main__':
    pass
    print(CA("F"))
