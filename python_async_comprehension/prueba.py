#!/usr/bin/env python3

from random import random
import time

while True:
    us_num = input("Hola!, Bienvenido al dado pajero, Si desea un numero al azar presione | 1 | y si no marque | 2 | CHUPELO .i.\n")
    time.sleep(1.5)
    us_num = int(us_num)
    if us_num == 1:
        r_num = random()
        r_num = repr(r_num)
        l_num = r_num[-1]
        l_num = int(l_num)
        if l_num > 0 and l_num < 7:
            print("Generando numero al azar... \n... \n")
            time.sleep(3)

            print("Tu numero random es: {}.\n".format(l_num))
            break
    elif us_num == 2:
        print("CHUPELO X2")
        break
    else:
        print("|El valor es incorrecto y tambien CHUPELO|")
        break

