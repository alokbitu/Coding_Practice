#if the sum of its digit to the power equal to number of digits is equal with the original number
# suppose the number is 153
# 1**3 + 5**3+ 3**3 = 1+125+27=153.....Armstrong number

num = int(input("enter the number"))
sum =0
pow = len(str(num))
original = num
#print(pow)
while num > 0:
    digit = num % 10
    sum = sum +(digit**pow)
    num = num //10
if sum == original:
    print("Armstrong Number")
else:
    print("Not armstrong number")