import re

f = open("day2.txt", "r")
pas = [line for line in f.readlines()]
f.close()

validpw = 0
valid2 = 0
for i in range(1000):
    l = re.split('-|: | ',pas[i])
    low = int(l[0])
    up = int(l[1])
    ch = l[2]
    pw = l[3].strip()
    countCh = pw.count(ch)
    #Part 1
    if low <= countCh <= up : validpw += 1 #
    #Part 2
    if((pw[low-1]==ch and pw[up-1]!=ch) or (pw[low-1]!=ch and pw[up-1]==ch)):
        valid2 +=1
        
print(validpw)
print(valid2)