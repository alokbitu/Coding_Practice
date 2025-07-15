'''
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
'''

row,col = 5,5
for i in range(row):
    for j in range (col,0,-1):
        print(j,end=" ")
    print()