#calculate the no. of time a charachter in a string

str = "I am alok kumar patra, a computer science graduate"
chr = "a"

count = 0

for i in str:
    print(i)
    if i == chr:
        count += 1

print(count)
