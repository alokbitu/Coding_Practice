'''
1 2 3 4 5
2 0 0 0 4
3 0 0 0 3
4 0 0 0 2
5 4 3 2 1
'''

row,col=5,5
for i in range(1,row+1):
    for j in range(1,row+1):
        if i == 1:
            print(j,end=" ")
        elif i == row:
            print(row-j+1,end=" ")
        elif j == 1:
            print(i,end=" ")
        elif j== row:
            print(row-i+1,end=" ")
        else:
            print(0,end=" ")
    print()


