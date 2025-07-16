'''
z
y x
w v u
t s r q
p o n m l
'''

n = 5
start = ord('z')
for i in range (1,n+1):
    for j in range(i):
        print(chr(start),end=' ')
        start -= 1
    print()