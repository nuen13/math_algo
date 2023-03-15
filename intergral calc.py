
## intergral fomular

# x^3
#    3x^4+7x+3
# x^n = (x^(n+1)) / (n+1)
# 1/x = ln(x) 
# sin(x) = -cos(x)
# e^x = e^x 
# ln(x) = xln(x) - x
#var = input("variable of intergration: ")

import re
from re import search
mathSymbol = '\+-'

var= "x"
#functionInp  = input("calculate the intergral of: ")
functionInp = "3x^4-7x+3"
fString = functionInp 

plusPosList = []
minusPosList = []

# Get plus Location
for plusMatch in re.finditer(r"[+]", functionInp):
    plusPosList.append(plusMatch.start())
    #print(plusMatch.start())
    #print(plusPosList)


# Get minus Location
for minusMatch in re.finditer(r"[-]", functionInp):
    minusPosList.append(minusMatch.start())
    #print(minusMatch.start())
#print(plusPosList)
# symbol Locaton 
symbolPosList = plusPosList + minusPosList
symbolPosList.sort()

#print(symbolPosList)


# Get each part
startPos = 0
symbolCount = len(symbolPosList) 
posCount = 0

partList = []
while posCount <= len(symbolPosList):
    if posCount <= len(symbolPosList) - 1:
        endPos = int(symbolPosList[posCount])
        char = fString[startPos:endPos]
        partList.append(char)
        startPos = endPos + 1
        #print("char: ", char)

        posCount += 1
    else: 
        char = fString[startPos:]
        partList.append(char)
        #print("char: ", char) 

        posCount += 1

def firstForm(part):
    return part
def seccondForm(part):
    return part
def thirdFormCos(part):
    return part
def thirdFormSin(part):
    return part
def fourthForm(part):
    return part
def fifthForm(part):
    return part

# find if x in part
varInPartList = []
for part in partList:
    if part.count(var) == 0:
        pass
    elif part.count(var) == 1:
        varInPartList.append(part)
    else: 
        print(" tinh sau")

print(varInPartList)

for part in varInPartList:
    print(part)
    if search("ln", part):
        fifthForm(part)
        
    if search("e^", part):
        fourthForm(part)

    if search("cos", part):
        thirdFormCos(part)

    if search("sin", part):
        thirdFormSin(part)

    if search("/x", part):
        seccondForm(part)

    else:
        firstForm(part)
        print("yay")
# x^3
#    3x^4+7x+3

# 1. x^n = (x^(n+1)) / (n+1)
# 2. 1/x = ln(x) 
# 3. sin(x) = -cos(x)
# 4. e^x = e^x 
# 5. ln(x) = xln(x) - x
    #Psuedo Code
#1. Get the minus and plus location to divide equation in to part 
#2. intergrate each part