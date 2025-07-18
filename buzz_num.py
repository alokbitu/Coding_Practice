#buzz number is that number of which last digit is 7 or the number is divisible by 7
#ex- 7,49,217

num = int(input("enter the number"))

if num % 10 == 7 or num % 7 == 0:
    print("Buzz number")
else:
    print("Non-buzz number")
