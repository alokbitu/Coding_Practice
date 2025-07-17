'''
1 1 1 1 1
1 1 1 2 2
1 1 3 3 3
1 4 4 4 4
5 5 5 5 5
'''

n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if j <= n-i :
            print(1,end=' ')
        else:
            print(i,end=' ')
    print()
