'''
      A
    A B A
  A B C B A
A B C D C B A
'''

n = 4
for i in range(1,n+1):
    print('  '*(n-i),end='')
    for j in range(i):
        print(chr(65+j),end=' ')
    for j in range(i-2,-1,-1):
        print(chr(65+j),end=' ')
    print()