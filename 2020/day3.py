f = open("day3.txt", "r")
path = [line.strip() for line in f.readlines()]
f.close()

def tree(right, down):
    trees = 0
    i = 0
    while True :
        #slope : y/x = right/down => y = (right/down)x
        j = int((i * right / down)) % len(path[0])
        if path[ i ][ j ] == '#':
            trees += 1
        i += down
        if i >= len(path):
            return trees

print(tree(1,1) * tree(3,1) * tree(5,1) * tree(7,1) * tree(1,2))
