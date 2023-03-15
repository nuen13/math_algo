import numpy as np

mainList = ['0.6x^5', '3.5x^2', '3x']
sub_li = [['+', 7], ['-', 4]]
 
l = len(sub_li)
for i in range(0, l):
    for j in range(0, l-i-1):
        print(j)
        if (sub_li[j][1] > sub_li[j + 1][1]):
            tempo = sub_li[j]
            sub_li[j]= sub_li[j + 1]
            sub_li[j + 1]= tempo



print(mainList)
print(sub_li)

lenn = len(mainList)
print("lenn: ", lenn)
finalList = []


x = 0 
while x <= (lenn - 1):
    b = mainList[x]
    finalList.append(b)
    if x <= (lenn - 2):
        d = sub_li[x][0]
        finalList.append(d)
    x += 1

finalLen = len(finalList)

print(*finalList, sep=" ")