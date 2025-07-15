'''
1 2 3 4 5
5 4 3 2 1
1 2 3 4 5
5 4 3 2 1
1 2 3 4 5
'''

row,col=5,5
for i in range(row):
    if i%2 ==0:
        for j in range(col):
            print(j+1,end=" ")
        print()
    else:
        for j in range(col,0,-1):
            print(j,end=" ")
        print()