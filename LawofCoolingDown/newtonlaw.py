import numpy as np
import math

def formOne(): 
    # initialTime = input("Initial Time: ")
    # initialTemp = input("Initial Temperature: ")
    # seccondTime = input("Seccond Time: ")
    # seccondTemp = input("Seccond Temperature: ")
    # ambientTemp = input("Ambient Temperature: ")

    initialTime = 0
    initialTemp = 50
    seccondTime = 5
    seccondTemp = 40
    ambientTemp = 15
 
    # Find A
    if initialTime == 0: 
        constantA  = initialTemp - ambientTemp
    else: 
        seccondTime = seccondTime - initialTime
        constantA  = initialTemp - ambientTemp

    # Find constantK
    constantK = ((math.log((seccondTemp - ambientTemp) / constantA)) / seccondTime)

    uniqueSol = "T = {}e^({}t) + {}".format(constantA, round(constantK, 3), ambientTemp)

    print(uniqueSol)

def main():
    promtp = ("""What are given? (type in number e.g. 1): 
    (1) 2 Time, 2 Temperature, Ambient Temperature. Find Unique Solution
            """)
    print(promtp)
    promptInp = input("What's the given type: ")

    if promptInp == "1": 
        formOne()
    else:
        pass

main()