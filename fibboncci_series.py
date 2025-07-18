#print the fibbonaci series upto n

a = 0
b = 1
n = int(input("enter the number"))
for i in range(n):
    print(a,end=',')
    a,b = b,a+b

