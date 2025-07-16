'''
O
 O
  O
   O
    O
'''

n = 5
for i in range(n):
    for j in range(n):
        if i == j:
            print("O",end=' ')
        else:
            print(" ",end=" ")
    print()