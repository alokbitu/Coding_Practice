'''
        1
      2 3 2
    3 4 5 4 3
  4 5 6 7 6 5 4
5 6 7 8 9 8 7 6 5
'''

n = 5
for i in range(1, n + 1):
    print("  " * (n - i), end="")  # Leading spaces
    start = i
    # Increasing numbers
    for j in range(i):
        print(start, end=" ")
        start += 1
    start -= 2
    # Decreasing numbers
    for j in range(i - 1):
        print(start, end=" ")
        start -= 1
    print()