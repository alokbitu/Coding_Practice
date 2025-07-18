#automorphic number is that number whose sqare number ends with the same original number
# suppose 6 is the original number then 6**2=36....which ends with 6...so 6 is a automorphic number

num = int(input("enter the number"))
power_num = num **2
digit = power_num % 10
if num == digit:
    print("automorphic number number")
else:
    print("non automorphic number")