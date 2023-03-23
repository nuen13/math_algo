import numpy as np
import math

def find_constant_A(zeroTe, zeroTi, ambTe, oneTi):
    print(zeroTi)
    if zeroTi == 0: 
        constA  = zeroTe - ambTe
        return constA
    else: 
        oneTi -= zeroTi
        constA  = zeroTe - ambTe
        return constA
def find_constant_K(oneTe, ambTe, constA, oneTi):
    constK = ((math.log((oneTe - ambTe) / constA)) / oneTi)
    
    return constK

def find_time(ambTe, constK, constA, twoTe): 
    twoTi = ((math.log((twoTe - ambTe) / constA)) / constK)
    return twoTi

def find_temp():
    pass
def show_unique_sol(constA, constK, ambTe):
    uniqueSol = "T = {}e^({}t) + {}".format(constA, round(constK, 3), ambTe)

    return uniqueSol
def get_values(promptInp):
    # find unique solution
    if promptInp == "1":
        zeroTi = float(input("Initial Time: "))
        zeroTe = float(input("Initial Temperature: "))
        oneTi = float(input("Seccond Time: "))
        oneTe = float(input("Seccond Temperature: "))
        ambTe = float(input("Ambient Temperature: "))

        constA = find_constant_A(zeroTe, zeroTi, ambTe, oneTi)
        constK = find_constant_K(oneTe, ambTe, constA, oneTi)

        uniqueSol = show_unique_sol(constA, constK, ambTe)

        print(uniqueSol)

    elif promptInp == "2":
        zeroTi = float(input("Initial Time: "))
        zeroTe = float(input("Initial Temperature: "))
        oneTi = float(input("Seccond Time: "))
        oneTe = float(input("Seccond Temperature: "))
        ambTe = float(input("Ambient Temperature: "))
        twoTe = float(input("given Temperature: "))
   

        constA = float(find_constant_A(zeroTe, zeroTi, ambTe, oneTi))
        constK = float(find_constant_K(oneTe, ambTe, constA, oneTi))

        twoTi = find_time(ambTe, constK, constA, twoTe)

        print("time when temp is {} is {}".format(twoTe, round(twoTi, 2)))

    elif promptInp == "3":
        # zeroTi = float(input("Initial Time: "))
        # zeroTe = float(input("Initial Temperature: "))

        # ambTe = float(input("Ambient Temperature: "))

        # constK = float(input("constant K: "))
        # twoTe = float(input("given Temperature: "))

    
    
        
        
        constA = float(find_constant_A(zeroTe, zeroTi, ambTe, oneTi))
        time = float(find_time(ambTe, constK, constA, twoTe))

        print("time when temp is {} is {}".format(twoTe, round(time, 2)))

def main():
    promtp = ("""

What are given? (type in number e.g. 1): 
(1) 2 Time, 2 Temperature, Ambient Temperature. Find Unique Solution
(2) 2 Time, 3 Temperature, Ambient Temperature. Find time with 1 given temp
(3) 1 Time, 2 Temperature, Ambient Temperature, constant k. Find time

            """)
    print(promtp)
    promptInp = input("What's the given type: ")

    get_values(promptInp)

main()