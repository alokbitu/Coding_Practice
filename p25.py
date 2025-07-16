'''
O   O
 O O
  O
 O O
O    O
'''

n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j or j == n+1-i:
            print("O",end=' ')
        else:
            print(" ",end=" ")
    print()