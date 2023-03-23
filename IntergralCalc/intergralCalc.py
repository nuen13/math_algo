# Initial Importation
import re
from re import search

global partList, solList, var
# ---- Print Final Answer 
def finalIntergral(solList, partList):
    solListlen = len(solList)
    finalList = []

    count = 0 
    # Add intergrated part and symbol into 1 list and in correct position
    while count <= (solListlen - 1):
        part = solList[count]
        finalList.append(part)
        if count <= (solListlen - 2):
            symbol = symbolList[count][0]
            finalList.append(symbol)
        count += 1

    # Print final answer
    print(*finalList, sep=" ")

# ---- Get Part in the given equation ---- 
def getPart(fString):
    global partList
    # Get each part
    startPos = 0
    posCount = 0

    partList = []

    # Get the position of the symbol and each part is the start of first symbol
    # to the end of the next symbol 
    while posCount <= len(symbolList):
        if posCount <= len(symbolList) - 1:
            endPos = int(symbolList[posCount][1])
            char = fString[startPos:endPos]
            partList.append(char)
            startPos = endPos + 1
            #print("char: ", char)

            posCount += 1

        # Get the last part where there is no symbol at the end
        else: 
            char = fString[startPos:]
            partList.append(char)

            posCount += 1
    # Use the part to identify which formular will be used to intergrate
    identifyForm(partList)

# Identity formular used to intergrate 
def identifyForm(partList): 
    global solList 
    solList = []  

    # nothing special (normal form)
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
        return part
    # 1 /x form (e.g 3/x^3, 4/x^5)
    def seccondForm(part): 
        xPos = part.index(var) # get pos of variable
        divisionPos = part.index('/x')

        
        print('x: ', xPos)
        print('/: ', divisionPos)

        # get a pos
        a = int(part[:divisionPos])
        if part[(divisionPos + 2)] == "^":
            b = (part[(divisionPos + 3):])
        else: 
            pass
        #solList.append(sol)

        print('a: ', a)
        print('b: ', b)
        return part
    def thirdFormCos(part):
        return part
    def thirdFormSin(part):
        return part
    def fourthForm(part):
        return part
    def fifthForm(part):
        return part


    # Count how many Variable exist in 1 part
    oneVarPartL = []
    for part in partList:
        # if there's only 1 or 0 var in one part
        # e.g. 8, 8x, cos(x), 1/x etc. 
        if part.count(var) == 0 or part.count(var) == 1:
            oneVarPartL.append(part)
        
        # if there are 2 or more vars in 1 part 
        # 2xcos(x), e^x*ln(x)
        else: 
            print(" tinh sau")
    
    # if there only 1 or 0 var in part
    for part in oneVarPartL:

        # if ( ln ) in part 
        if search("ln", part):
            fifthForm(part)
            
        # if ( e^ ) in part  
        elif search("e^", part):
            fourthForm(part)

        # if ( cos ) in part 
        elif search("cos", part):
            thirdFormCos(part)

        # if ( sin ) in part 
        elif search("sin", part):
            thirdFormSin(part)

        # if ( /x ) in part (1/x, 3/x)
        elif search("/x", part):
            seccondForm(part)
    
        # if nothing special (3x, 78x^4 )
        else:
            firstForm(part)
    
    # Run the final answer
    finalIntergral(solList, partList)




def getSymbol(functionStr):
    global symbolList

    symbolList = [] 
    plusPosList = []
    minusPosList = []

    # ---- Get Symbol Location ---- 
    # Get plus Location
    for plusMatch in re.finditer(r"[+]", functionStr):
        plusPos = plusMatch.start()

        plusPosList = ['+', plusPos]

        symbolList.append(plusPosList)

    # Get minus Location
    for minusMatch in re.finditer(r"[-]", functionStr):
        minusPos = minusMatch.start()
        
        minusPosList = ['+', minusPos]
        symbolList.append(minusPosList)

    # Sort the Symbol List (First to Last Position)
    symbolListLen = len(symbolList)
    for i in range(0, symbolListLen):
        for j in range(0, symbolListLen-i-1):

            if (symbolList[j][1] > symbolList[j + 1][1]):
                tempo = symbolList[j]
                symbolList[j]= symbolList[j + 1]
                symbolList[j + 1]= tempo

def getEquation():
    global var
    # var = input("variable of intergration: ")
    # functionInp  = input("calculate the intergral of: ")

    var= "x"    
    functionInp = "2/x^4"

    fString = functionInp 
    functionStr = functionInp
    getSymbol(functionStr)
    getPart(fString)

getEquation()