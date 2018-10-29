# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
#
#  ██████  ██████   █████  ██████       █████  ███    ██ ██████       ██████  ██████   ██████  ██████  ██████  ██ ███    ██  █████  ████████ ███████ ███████
# ██       ██   ██ ██   ██ ██   ██     ██   ██ ████   ██ ██   ██     ██      ██    ██ ██    ██ ██   ██ ██   ██ ██ ████   ██ ██   ██    ██    ██      ██
# ██   ███ ██████  ███████ ██   ██     ███████ ██ ██  ██ ██   ██     ██      ██    ██ ██    ██ ██████  ██   ██ ██ ██ ██  ██ ███████    ██    █████   ███████
# ██    ██ ██   ██ ██   ██ ██   ██     ██   ██ ██  ██ ██ ██   ██     ██      ██    ██ ██    ██ ██   ██ ██   ██ ██ ██  ██ ██ ██   ██    ██    ██           ██
#  ██████  ██   ██ ██   ██ ██████      ██   ██ ██   ████ ██████       ██████  ██████   ██████  ██   ██ ██████  ██ ██   ████ ██   ██    ██    ███████ ███████
#
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████

# All rotor positions in Grad

# 1:  X = 90°       Y = 0°
# 2:  X = 18°       Y = 72°
# 3:  X = 54°       Y = 36°
# 4:  X = 90°       Y = 0°
# 5:  x = -54°      Y = -36°
# 6:  X = -18°      Y = -72°

# All rotor positions in coordinates X and Y

# 1: X = 0                                      Y = -500
# 2: X = -475.52825814757678605821966668969     Y = -154.50849718747371205114670859141
# 3: X = -293.89262614623656458435297731954     Y =  404.50849718747371205114670859141
# 3: X =  0                                     Y =  131.16298
# 5: X =  293.89262614623656458435297731954     Y = -404.50849718747371205114670859141
# 6: X =  475.52825814757678605821966668969     Y = -154.50849718747371205114670859141
#
# motor_rotor_1_x = 0
# motor_rotor_1_y = 500
# motor_rotor_2_x = 475.52825814757678605821966668969
# motor_rotor_2_y = 154.50849718747371205114670859141
# motor_rotor_3_x = 293.89262614623656458435297731954
# motor_rotor_3_y = 404.50849718747371205114670859141
# motor_rotor_4_x = 0
# motor_rotor_4_y = 131.16298
# motor_rotor_5_x = 293.89262614623656458435297731954
# motor_rotor_5_y = 404.50849718747371205114670859141
# motor_rotor_6_x = 475.52825814757678605821966668969
# motor_rotor_6_y = 154.50849718747371205114670859141

# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
#
# ███    ███  ██████  ██████  ██    ██ ██      ███████     ██ ███    ███ ██████   ██████  ██████  ████████ ███████
# ████  ████ ██    ██ ██   ██ ██    ██ ██      ██          ██ ████  ████ ██   ██ ██    ██ ██   ██    ██    ██
# ██ ████ ██ ██    ██ ██   ██ ██    ██ ██      █████       ██ ██ ████ ██ ██████  ██    ██ ██████     ██    ███████
# ██  ██  ██ ██    ██ ██   ██ ██    ██ ██      ██          ██ ██  ██  ██ ██      ██    ██ ██   ██    ██         ██
# ██      ██  ██████  ██████   ██████  ███████ ███████     ██ ██      ██ ██       ██████  ██   ██    ██    ███████
#
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████

from decimal import *
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
#
# ██    ██  █████  ██████  ██  █████  ██████  ██      ███████ ███████
# ██    ██ ██   ██ ██   ██ ██ ██   ██ ██   ██ ██      ██      ██
# ██    ██ ███████ ██████  ██ ███████ ██████  ██      █████   ███████
#  ██  ██  ██   ██ ██   ██ ██ ██   ██ ██   ██ ██      ██           ██
#   ████   ██   ██ ██   ██ ██ ██   ██ ██████  ███████ ███████ ███████
#
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████


radius_of_reaction_wheel = 131.16298    # Millimeter
radius_of_rotors = 500        # Millimeter
force_of_rotors = 10             # Newton


# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
#
# ██████  ██     ██████  ███████ ███████
# ██   ██ ██     ██   ██ ██      ██
# ██████  ██     ██   ██ █████   █████
# ██      ██     ██   ██ ██      ██
# ██      ██     ██████  ███████ ██
#
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████

getcontext().prec = 50
pi = Decimal(3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679)

# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
#
# ███████  █████   ██████ ████████  ██████  ██████  ██  █████  ██          ██████  ███████ ███████
# ██      ██   ██ ██         ██    ██    ██ ██   ██ ██ ██   ██ ██          ██   ██ ██      ██
# █████   ███████ ██         ██    ██    ██ ██████  ██ ███████ ██          ██   ██ █████   █████
# ██      ██   ██ ██         ██    ██    ██ ██   ██ ██ ██   ██ ██          ██   ██ ██      ██
# ██      ██   ██  ██████    ██     ██████  ██   ██ ██ ██   ██ ███████     ██████  ███████ ██
#
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████


def factorial(x):
    k = 1
    for i in range(1, x + 1):
        k *= i
    return k

# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
#
#  ██████  ██████  ███████      ████████ ██     ██  ██████      ██████  ███████ ███████
# ██      ██    ██ ██              ██    ██     ██ ██    ██     ██   ██ ██      ██
# ██      ██    ██ ███████         ██    ██  █  ██ ██    ██     ██   ██ █████   █████
# ██      ██    ██      ██         ██    ██ ███ ██ ██    ██     ██   ██ ██      ██
#  ██████  ██████  ███████ ███████ ██     ███ ███   ██████      ██████  ███████ ██
#
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████


def cos_two(y):
    x = Decimal(y * pi) / Decimal(180)
    res = 1
    for i in range(1, 50):

        r = Decimal(x ** (2 * i)) / Decimal(factorial(2 * i))
        n = (-1)**(i)
        res += r * n

    return Decimal("% .6f" % res)


# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
#
#  ██████  █████  ██       ██████ ██    ██ ██       █████  ████████ ██  ██████  ███    ██
# ██      ██   ██ ██      ██      ██    ██ ██      ██   ██    ██    ██ ██    ██ ████   ██
# ██      ███████ ██      ██      ██    ██ ██      ███████    ██    ██ ██    ██ ██ ██  ██
# ██      ██   ██ ██      ██      ██    ██ ██      ██   ██    ██    ██ ██    ██ ██  ██ ██
#  ██████ ██   ██ ███████  ██████  ██████  ███████ ██   ██    ██    ██  ██████  ██   ████
#
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
# 1:  X = 90°       Y = 0°
# 2:  X = 18°       Y = 72°
# 3:  X = 54°       Y = 36°
# 4:  X = 90°       Y = 0°
# 5:  x = -54°      Y = -36°
# 6:  X = -18°      Y = -72°
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
getcontext().prec = 16

rotor_rig_bacX_5 = cos_two(54) * radius_of_rotors
rotor_rig_bacY_5 = cos_two(36) * radius_of_rotors

rotor_rig_froX_6 = cos_two(18) * radius_of_rotors
rotor_rig_froY_6 = cos_two(72) * radius_of_rotors

rotor_mid_froX_1 = cos_two(90) * radius_of_rotors
rotor_mid_froY_1 = cos_two(00) * radius_of_rotors

rotor_lef_froX_2 = cos_two(18) * radius_of_rotors
rotor_lef_froY_2 = cos_two(72) * radius_of_rotors

rotor_lef_bacX_3 = cos_two(54) * radius_of_rotors
rotor_lef_bacY_3 = cos_two(36) * radius_of_rotors


# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
#
# print("rotor_rig_bacX_5 : ", rotor_rig_bacX_5)
# print("rotor_rig_bacY_5 : ", rotor_rig_bacY_5, "\n")
#
# print("rotor_rig_froX_6 : ", rotor_rig_froX_6)
# print("rotor_rig_froY_6 : ", rotor_rig_froY_6, "\n")
#
# print("rotor_mid_froX_1 : ", rotor_mid_froX_1)
# print("rotor_mid_froY_1 : ", rotor_mid_froY_1, "\n")
#
# print("rotor_lef_froX_2 : ", rotor_lef_froX_2)
# print("rotor_lef_froY_2 : ", rotor_lef_froY_2, "\n")
#
# print("rotor_lef_bacX_3 : ", rotor_lef_bacX_3)
# print("rotor_lef_bacY_3 : ", rotor_lef_bacY_3, "\n")
#
#
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
#
# ██████   █████  ███████ ██  ██████     ██      ███████ ██    ██ ███████ ██████       █████   ██████ ████████
# ██   ██ ██   ██ ██      ██ ██          ██      ██      ██    ██ ██      ██   ██     ██   ██ ██         ██
# ██████  ███████ ███████ ██ ██          ██      █████   ██    ██ █████   ██████      ███████ ██         ██
# ██   ██ ██   ██      ██ ██ ██          ██      ██       ██  ██  ██      ██   ██     ██   ██ ██         ██
# ██████  ██   ██ ███████ ██  ██████     ███████ ███████   ████   ███████ ██   ██     ██   ██  ██████    ██
#
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
# F1 x L1 = F2 x L2
#
# F1 = (F2 x L2) / L1
# L1 = (F2 x L2) / F1
#
# F2 = (F1 x L1) / L2
# L2 = (F1 x L1) / F2
#
# F1 = force_of_rotors x L2 = radius_of_rotors
# L2 = rotor_mid_froX_1, rotor_mid_froY_1, rotor_lef_froX_2, rotor_lef_froY_2, rotor_lef_bacX_3, rotor_lef_bacY_3,rotor_rig_bacX_5, rotor_rig_bacY_5, rotor_rig_froX_6, rotor_rig_froY_6,
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████

basic_lever_act = force_of_rotors * radius_of_rotors

lever_act_rig_bacX_5 = basic_lever_act / rotor_rig_bacX_5
lever_act_rig_bacY_5 = basic_lever_act / rotor_rig_bacY_5

lever_act_rig_froX_6 = basic_lever_act / rotor_rig_froX_6
lever_act_rig_froY_6 = basic_lever_act / rotor_rig_froY_6

# lever_act_mid_froX_1 = basic_lever_act / rotor_mid_froX_1
lever_act_mid_froY_1 = basic_lever_act / rotor_mid_froY_1

lever_act_lef_froX_2 = basic_lever_act / rotor_lef_froX_2
lever_act_lef_froY_2 = basic_lever_act / rotor_lef_froY_2

lever_act_lef_bacX_3 = basic_lever_act / rotor_lef_bacX_3
lever_act_lef_bacY_3 = basic_lever_act / rotor_lef_bacY_3

# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
#
# print("lever_act_rig_bacX_5 :  ", lever_act_rig_bacX_5)
# print("lever_act_rig_bacY_5 :  ", lever_act_rig_bacY_5, "\n")
#
# print("lever_act_rig_froX_6 :  ", lever_act_rig_froX_6)
# print("lever_act_rig_froY_6 :  ", lever_act_rig_froY_6, "\n")
#
# # print("lever_act_mid_froX_1 :  ", lever_act_mid_froX_1)
# print("lever_act_mid_froY_1 :  ", lever_act_mid_froY_1, "\n")
#
# print("lever_act_lef_froX_2 :  ", lever_act_lef_froX_2)
# print("lever_act_lef_froY_2 :  ", lever_act_lef_froY_2, "\n")
#
# print("lever_act_lef_bacX_3 :  ", lever_act_lef_bacX_3)
# print("lever_act_lef_bacY_3 :  ", lever_act_lef_bacY_3, "\n")
#
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
#
# ██████  ███████ ██████   ██████ ███████ ███    ██ ████████
# ██   ██ ██      ██   ██ ██      ██      ████   ██    ██
# ██████  █████   ██████  ██      █████   ██ ██  ██    ██
# ██      ██      ██   ██ ██      ██      ██  ██ ██    ██
# ██      ███████ ██   ██  ██████ ███████ ██   ████    ██
#
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
# 90 = 360 / 100 * 25
# 360 = 90 / 25 * 100
# 100 = 25 * 360 / 90
# 25 = 90 / 360 * 100
#
# output_value = base_value / 100 * percent
# base_value = output_value / percent * 100
# 100 = percent * base_value / output_value
# percent = output_value / base_value * 100

percent_rig_bacX_5 = lever_act_rig_bacX_5 / lever_act_mid_froY_1
percent_rig_bacY_5 = lever_act_rig_bacY_5 / lever_act_mid_froY_1

percent_rig_froX_6 = lever_act_rig_froX_6 / lever_act_mid_froY_1
percent_rig_froY_6 = lever_act_rig_froY_6 / lever_act_mid_froY_1

# percent_mid_froX_1 = lever_act_mid_froX_1 / lever_act_mid_froY_1
percent_mid_froY_1 = lever_act_mid_froY_1 / lever_act_mid_froY_1

percent_lef_froX_2 = lever_act_lef_froX_2 / lever_act_mid_froY_1
percent_lef_froY_2 = lever_act_lef_froY_2 / lever_act_mid_froY_1

percent_lef_bacX_3 = lever_act_lef_bacX_3 / lever_act_mid_froY_1
percent_lef_bacY_3 = lever_act_lef_bacY_3 / lever_act_mid_froY_1


# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
#
# print("percent_rig_bacX_5 :  ", percent_rig_bacX_5)
# print("percent_rig_bacY_5 :  ", percent_rig_bacY_5, "\n")
#
# print("percent_rig_froX_6 :  ", percent_rig_froX_6)
# print("percent_rig_froY_6 :  ", percent_rig_froY_6, "\n")
#
# # print("percent_mid_froX_1 :  ", percent_mid_froX_1)
# print("percent_mid_froY_1 :  ", percent_mid_froY_1, "\n")
#
# print("percent_lef_froX_2 :  ", percent_lef_froX_2)
# print("percent_lef_froY_2 :  ", percent_lef_froY_2, "\n")
#
# print("percent_lef_bacX_3 :  ", percent_lef_bacX_3)
# print("percent_lef_bacY_3 :  ", percent_lef_bacY_3, "\n")
#
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
#
# ████████  ██████      ████████ ██   ██ ███████     ██████  ██  ██████  ██   ██ ████████
#    ██    ██    ██        ██    ██   ██ ██          ██   ██ ██ ██       ██   ██    ██
#    ██    ██    ██        ██    ███████ █████       ██████  ██ ██   ███ ███████    ██
#    ██    ██    ██        ██    ██   ██ ██          ██   ██ ██ ██    ██ ██   ██    ██
#    ██     ██████         ██    ██   ██ ███████     ██   ██ ██  ██████  ██   ██    ██
#
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████

print("to the Right", force_of_rotors, "= 1 = 100%")

# print(lever_act_lef_bacX_3, "3")
# print(lever_act_lef_froX_2, "2", "\n")
#
# print(percent_lef_bacX_3, "3")
# print(percent_lef_froX_2, "2", "\n")
#
# print(percent_lef_bacX_3 * 2, "3")
# print(percent_lef_froX_2 * 2, "2", "\n")

print(percent_lef_bacX_3 / 2, force_of_rotors * (percent_lef_bacX_3 / 2), "3")
print(percent_lef_froX_2 / 2, force_of_rotors * (percent_lef_froX_2 / 2), "2", "\n")

sideways_rig_lef_bacX_3 = percent_lef_bacX_3 / 2
sideways_rig_lef_froX_2 = percent_lef_froX_2 / 2

# print(lever_act_lef_bacX_3 / (percent_lef_bacX_3 * 2), "3")
# print(lever_act_lef_froX_2 / (percent_lef_froX_2 * 2), "2", "\n")

# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
#
# ████████  ██████      ████████ ██   ██ ███████     ██      ███████ ███████ ████████
#    ██    ██    ██        ██    ██   ██ ██          ██      ██      ██         ██
#    ██    ██    ██        ██    ███████ █████       ██      █████   █████      ██
#    ██    ██    ██        ██    ██   ██ ██          ██      ██      ██         ██
#    ██     ██████         ██    ██   ██ ███████     ███████ ███████ ██         ██
#
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████

print("to the Left", force_of_rotors, "= 1 = 100%")

# print(lever_act_rig_bacX_5, "5")
# print(lever_act_rig_froX_6, "6", "\n")
#
# print(percent_rig_bacX_5, "5")
# print(percent_rig_froX_6, "6", "\n")
#
# print(percent_rig_bacX_5 * 2, "5")
# print(percent_rig_froX_6 * 2, "6", "\n")

print(percent_rig_bacX_5 / 2, force_of_rotors * (percent_rig_bacX_5 / 2), "5")
print(percent_rig_froX_6 / 2, force_of_rotors * (percent_rig_froX_6 / 2), "6", "\n")

sideways_left_rig_bacX_5 = percent_rig_bacX_5 / 2
sideways_left_rig_froX_6 = percent_rig_froX_6 / 2

# print(lever_act_rig_bacX_5 / (percent_rig_bacX_5 * 2), "5")
# print(lever_act_rig_froX_6 / (percent_rig_froX_6 * 2), "6", "\n")

# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
#
# ███████  ██████  ██████  ██     ██  █████  ██████  ██████
# ██      ██    ██ ██   ██ ██     ██ ██   ██ ██   ██ ██   ██
# █████   ██    ██ ██████  ██  █  ██ ███████ ██████  ██   ██
# ██      ██    ██ ██   ██ ██ ███ ██ ██   ██ ██   ██ ██   ██
# ██       ██████  ██   ██  ███ ███  ██   ██ ██   ██ ██████
#
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████

print("Forward", force_of_rotors, "= 1 = 100%")

# print(lever_act_lef_bacY_3, "3")
# print(lever_act_rig_bacY_5, "5", "\n")
#
# print(percent_lef_bacY_3, "3")
# print(percent_rig_bacY_5, "5", "\n")
#
# print(percent_lef_bacY_3 * 2, "3")
# print(percent_rig_bacY_5 * 2, "5", "\n")

print(percent_lef_bacY_3 / 2, force_of_rotors * (percent_lef_bacY_3 / 2), "3")
print(percent_rig_bacY_5 / 2, force_of_rotors * (percent_rig_bacY_5 / 2), "5", "\n")

forward_lef_bacY_3 = percent_lef_bacY_3 / 2
forward_rig_bacY_5 = percent_rig_bacY_5 / 2

# print(lever_act_lef_bacY_3 / (percent_lef_bacY_3 * 2), "3")
# print(lever_act_rig_bacY_5 / (percent_rig_bacY_5 * 2), "5", "\n")

# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
#
# ██████   █████   ██████ ██   ██ ██     ██  █████  ██████  ██████
# ██   ██ ██   ██ ██      ██  ██  ██     ██ ██   ██ ██   ██ ██   ██
# ██████  ███████ ██      █████   ██  █  ██ ███████ ██████  ██   ██
# ██   ██ ██   ██ ██      ██  ██  ██ ███ ██ ██   ██ ██   ██ ██   ██
# ██████  ██   ██  ██████ ██   ██  ███ ███  ██   ██ ██   ██ ██████
#
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████

print("Backward", force_of_rotors, "= 1 = 100%")

# print(lever_act_lef_froY_2, "2")
# print(lever_act_mid_froY_1, "1")
# print(lever_act_rig_froY_6, "6", "\n")
#
# print(percent_lef_froY_2, "2")
# print(percent_mid_froY_1, "1")
# print(percent_rig_froY_6, "6", "\n")
#
# print(percent_lef_froY_2 * 3, "2")
# print(percent_mid_froY_1 * 3, "1")
# print(percent_rig_froY_6 * 3, "6", "\n")

print(percent_lef_froY_2 / 3, force_of_rotors * (percent_lef_froY_2 / 3), "2")
print(percent_mid_froY_1 / 3, force_of_rotors * (percent_mid_froY_1 / 3), "1")
print(percent_rig_froY_6 / 3, force_of_rotors * (percent_rig_froY_6 / 3), "6", "\n")

backward_lef_froY_2 = percent_lef_froY_2 / 3
backward_mid_froY_1 = percent_mid_froY_1 / 3
backward_rig_froY_6 = percent_rig_froY_6 / 3

# print(lever_act_lef_froY_2 / (percent_lef_froY_2 * 3), "2")
# print(lever_act_mid_froY_1 / (percent_mid_froY_1 * 3), "1")
# print(lever_act_rig_froY_6 / (percent_rig_froY_6 * 3), "6", "\n")
#
# print(lever_act_mid_froY_1 * (percent_lef_froY_2 / 3))
# print(lever_act_mid_froY_1 * (percent_mid_froY_1 / 3))
# print(lever_act_mid_froY_1 * (percent_rig_froY_6 / 3), "\n")
#
#
# print(146456 * 500)
# print(rotor_lef_froY_2 * (lever_act_mid_froY_1 * (percent_lef_froY_2 / 3)))
# print(rotor_mid_froY_1 * (lever_act_mid_froY_1 * (percent_mid_froY_1 / 3)))
# print(rotor_rig_froY_6 * (lever_act_mid_froY_1 * (percent_rig_froY_6 / 3)), "\n")
