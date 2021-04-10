if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    s=[x,y,z]
    a=[]

for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            if i+j+k != n:
                a.append([i,j,k])
print(a)


1
2
3
3
[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 3], [0, 2, 0], [0, 2, 2], [0, 2, 3], [1, 0, 0], [1, 0, 1], [1, 0, 3], [1, 1, 0], [1, 1, 2], [1, 1, 3], [1, 2, 1], [1, 2, 2], [1, 2, 3]]
