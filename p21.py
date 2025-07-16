'''
p
q r
s t u
v w x y
z a b c d
e f g h i j
'''

n = 6
start = ord("p")
for i in range(1,n+1):
    for j in range(i):
        print(chr(start),end=" ")
        start += 1
        if start>ord('z'):
            start = ord('a')
    print()