
## intergral fomular

# x^3
#    3x^4+7x+3
# x^n = (x^(n+1)) / (n+1) done 

# 1/x = ln(x) 
# sin(x) = -cos(x)
# e^x = e^x 
# ln(x) = xln(x) - x
#var = input("variable of intergration: ")

import re
from re import search

var= "x"
#functionInp  = input("calculate the intergral of: ")
functionInp = "3x^4-7x+3"
fString = functionInp 
  
symbolList = [] 

plusPosList2 = []
minusPosList2 = []

plusPosList = []
minusPosList = []

# ---- Get Symbol Location ---- 
# Get plus Location
for plusMatch in re.finditer(r"[+]", functionInp):
    plusPos = plusMatch.start()

    plusPosList2 = ['+', plusPos]
    symbolList.append(plusPosList2)

    plusPosList.append(plusPos)

# Get minus Location
for minusMatch in re.finditer(r"[-]", functionInp):
    minusPos = minusMatch.start()
    
    minusPosList2 = ['+', minusPos]
    symbolList.append(minusPosList2)

    minusPosList.append(minusPos )

# Sort the Symbol List (First to Last Position)
l = len(symbolList)
for i in range(0, l):
    for j in range(0, l-i-1):

        if (symbolList[j][1] > symbolList[j + 1][1]):
            tempo = symbolList[j]
            symbolList[j]= symbolList[j + 1]
            symbolList[j + 1]= tempo

# Add plus & minus position (only position) list 
symbolPosList = plusPosList + minusPosList
symbolPosList.sort()




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
    if part.count(var) == 0:
        a = part 
        sol = ("{}x".format(a))
    elif part.count(var) == 1:
        xPos = part.index(var)
        if xPos != 0:
            a = int(part[:xPos])
            #print("a1: ", a)
        else:
            a = 1
        
        if xPos+1 == len(part):
            n = 1
        else:
            if part[xPos + 1] == "^":
                n = int(part[xPos+2: ])
                #print("n1: ", n)
            else:
                n = 1
        leftSide = (a/(n+1))
        rightSide =  (n+1)

        sol = ("{}x^{}".format(leftSide, rightSide))
        
        
    solList.append(sol)

    
 
    #get x position 
    #if x pos not 0
    #find a = :posx
    # if behind x is ^ then 
    # number behind ^ is n


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
    if part.count(var) == 0 or part.count(var) == 1:
        varInPartList.append(part)
    else: 
        print(" tinh sau")

#print(varInPartList)

solList = []  

for part in varInPartList:
    #print(part)
    if search("ln", part):
        fifthForm(part)
        
    elif search("e^", part):
        fourthForm(part)

    elif search("cos", part):
        thirdFormCos(part)

    elif search("sin", part):
        thirdFormSin(part)
    elif search("/x", part):
        seccondForm(part)

    else:
        firstForm(part)
        #print("yay")


# print("solution: ", solList)
# print("symbol and pos", symbolList)



lenn = len(solList)
# print("lenn: ", lenn)
finalList = []


x = 0 
while x <= (lenn - 1):
    b = solList[x]
    finalList.append(b)
    if x <= (lenn - 2):
        d = symbolList[x][0]
        finalList.append(d)
    x += 1
print(*finalList, sep=" ")

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