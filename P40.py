'''
1 2 3 4 5 6
 2 3 4 5 6
  3 4 5 6
   4 5 6
    5 6
     6
    5 6
   4 5 6
  3 4 5 6
 2 3 4 5 6
1 2 3 4 5 6
'''

n = 6

# Upper Half
for i in range(n):
    print(" " * i, end="")  # Indentation
    for j in range(i + 1, n + 1):
        print(j, end=" ")
    print()

# Lower Half
for i in range(n - 2, -1, -1):
    print(" " * i, end="")  # Indentation
    for j in range(i + 1, n + 1):
        print(j, end=" ")
    print()
