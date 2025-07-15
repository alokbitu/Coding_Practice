'''
1
1 1
1 1 1
1 1 1 1
1 1 1 1 1
1 1 1 1
1 1 1
1 1
1
'''

n = 9
for i in range(1,n+1):
    if i <=5:
        for j in range(1,i+1):
            print(1,end=" ")
    else:
        for j in range(1,n+2-i):
            print(1,end=" ")
    print()