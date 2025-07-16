'''
      1
    1 1 1
  1 1 1 1 1
1 1 1 1 1 1 1
'''


n = 4
for i  in range(n):
    space = '  '* (n-i+1)
    ones = '1 ' * (2*i+1)
    print(space,ones)