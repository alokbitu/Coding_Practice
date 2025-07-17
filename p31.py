'''
1 0 0 0 0
0 2 0 0 0
0 0 3 0 0
0 0 0 4 0
0 0 0 0 5
'''

n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            print(i,end=' ')
        else:
            print(0,end=' ')
    print()