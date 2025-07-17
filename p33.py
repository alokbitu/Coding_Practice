'''
A A A A A
A A A B B
A A C C C
A D D D D
E E E E E
'''

n = 5
for i in range(n):
    ch = chr(65+i)
    for j in range(n):
        if j < n-i-1:
            print('A',end=' ')
        else:
            print(ch,end=' ')
    print()