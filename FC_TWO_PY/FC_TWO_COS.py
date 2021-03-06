# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
#
# ████████ ██     ██  ██████       ██████  ██████  ███████
#    ██    ██     ██ ██    ██     ██      ██    ██ ██
#    ██    ██  █  ██ ██    ██     ██      ██    ██ ███████
#    ██    ██ ███ ██ ██    ██     ██      ██    ██      ██
#    ██     ███ ███   ██████       ██████  ██████  ███████
#
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
from decimal import *
from FC_TWO_FO import *

# def PI
getcontext().prec = 50
PI = Decimal(3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679)

# initialize COS


def COS(IN):

    # calculate COS
    DEG = Decimal(IN * PI) / Decimal(180)
    result = 1
    for i in range(1, 50):

        cos_cal = Decimal(DEG ** (2 * i)) / Decimal(FO(2 * i))
        sign_changer = (-1)**(i)
        result += cos_cal * sign_changer

    # returns COS
    return Decimal("% .6f" % result)


if __name__ == '__main__':
    pass
    print(COS(90))
