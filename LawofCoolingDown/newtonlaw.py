import numpy as np
import math

def findTimeWTemp(zeroTi, zeroTe, oneTi, oneTe, ambTe, constK, constA): 
    #twoTe = input("given Temperature: ")
    twoTe = 50

    twoTi = ((math.log((twoTe - ambTe) / constA)) / constK)

    print("time when temp is {} is {}".format(twoTe, round(twoTi, 2)))

def find_constant_K():
    pass
def find_constant_A():
    pass
def get

def getUniqueSol(promptInp): 
    # zeroTi = input("Initial Time: ")
    # zeroTe = input("Initial Temperature: ")
    # oneTi = input("Seccond Time: ")
    # oneTe = input("Seccond Temperature: ")
    # ambTe = input("Ambient Temperature: ")

    if promptInp == "1" or promptInp == "2":
        zeroTi = 0
        zeroTe = 70
        oneTi = 3
        oneTe = 60
        ambTe = 25
        
    
        # Find A
        if zeroTi == 0: 
            constA  = zeroTe - ambTe
        else: 
            oneTi = oneTi - zeroTi
            constA  = zeroTe - ambTe

        # Find constantK
        constK = ((math.log((oneTe - ambTe) / constA)) / oneTi)

    uniqueSol = "T = {}e^({}t) + {}".format(constA, round(constK, 3), ambTe)
    if promptInp == "1":
        print(uniqueSol)
    elif promptInp == "2":
        findTimeWTemp(zeroTi, zeroTe, oneTi, oneTe, ambTe, constK, constA)
    else: 
        pass

def main():
    promtp = ("""

What are given? (type in number e.g. 1): 
(1) 2 Time, 2 Temperature, Ambient Temperature. Find Unique Solution
(2) 2 Time, 3 Temperature, Ambient Temperature. Find time with 1 given temp
(3) 2 Time, 3 Temperature, Ambient Temperature, constant k. Find t

            """)
    print(promtp)
    promptInp = input("What's the given type: ")

    if promptInp == "1": 
        getUniqueSol(promptInp)
    elif promptInp == "2":
        getUniqueSol(promptInp)
    else:
        pass

main()