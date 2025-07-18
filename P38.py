'''
         1
       1   1
     1   2   1
    1  3   3   1
  1  4   6   4  1
1  5  10  10  5  1
'''

n = 6  # Number of rows

for i in range(n):
    print("  " * (n - i - 1), end="")  # Leading spaces for alignment
    num = 1
    for j in range(i + 1):
        print(f"{num:<3}", end=" ")   # Print number with fixed width
        num = num * (i - j) // (j + 1)  # Compute next number using combinatorics
    print()