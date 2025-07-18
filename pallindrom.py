# check a number is pallindrom or not
#   pallindrom means reversing a number would be same number

num = int(input("enter the number"))
original = num
rev = 0
while num > 0:
        reminder = num % 10
        rev = rev*10+reminder
        num = num // 10
if rev == original:
        print("Palindrom number")
else:
    print("Not palindrom number")