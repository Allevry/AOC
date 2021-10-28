def read():
    f = open("case.txt", "r")
    lis = [line for line in f.readlines()]
    f.close()
    size = len(lis)
    for i in range(size):
        for j in range(i+1,size):
            a = int(lis[i])
            b = int(lis[j])
            if a + b == 2020 :
                print(a," x ",b," = ",(a*b))
    for i in range(size):
        for j in range(i+1,size):
            for k in range(j+1,size):
                a = int(lis[i])
                b = int(lis[j])
                c = int(lis[k])
                if a + b + c == 2020 :
                    print(a," x ",b," x",c," = ",(a*b*c))

read()
