#part 1
f = open("day4.txt", "r")
al = []
s = ""
while True:
    line = f.readline()
    if line == '\n':
        al.append(s)
        s=""
        continue
    s = s + line
    if not line:
        al.append(s)
        break
f.close()
c = 0
for i in range(0,len(al)):
    if "ecl" in al[i] and "pid" in al[i] and "eyr" in al[i] and "hcl" in al[i] and "byr" in al[i] and "iyr" in al[i] and "hgt" in al[i]:
        c +=1
print(c)
#part 2
f = open("day4.txt", "r")
