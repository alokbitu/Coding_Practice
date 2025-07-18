# find out the prime numbers within a given range


start = int(input("Enter the 1st number: "))
end = int(input("Enter the last number: "))

primes = []

for num in range(start, end + 1):
    count = 0
    if num > 1:
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count == 2:
            primes.append(num)

print("Prime numbers in range:", primes)


