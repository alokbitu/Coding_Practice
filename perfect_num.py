#perfect number is that of which sum of divisiors except that number is equall to original number
# suppose the number is 6 , its divisors are 1,2,3,6 so then 1+2+3 = 6....this is a perfect number

num = int(input("Enter the number"))
divisor = []


for i in range(1,num+1):
        if num % i == 0 and i != num:
            divisor.append(i)

print(divisor)
if sum(divisor) == num:
    print("Perfect number")
else:
    print("Non-perfect number")


