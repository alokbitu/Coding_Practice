# spy number is that number whose sum of digits is equal with multiplications of digit
# suppose the number is 1124, 1+1+2+4=8,1*1*2*4=8....so this is a spy number


num = int(input("Enter a number: "))
temp = num  # Save original number
sum = 0
multiplication = 1

while temp > 0:
    digit = temp % 10
    sum += digit
    multiplication *= digit
    temp = temp // 10

print("Sum:", sum, "Product:", multiplication)

if sum == multiplication:
    print("Spy Number")
else:
    print("Non Spy Number")


