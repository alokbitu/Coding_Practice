'''
1 1 1 1 1
      1
    1
  1
1 1 1 1 1
'''

n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 or i == 5 or j == n+1-i:
            print(1,end=" ")
        else:
            print(" ",end=" ")
    print()