# Python program (pattern.py) to print the exact pattern:
num = 1

for i in range(1, 5):
    print("  " * (4 - i), end="")

    for j in range(i):
        print(num, end=" ")
        num += 1

    print()