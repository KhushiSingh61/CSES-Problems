n = int(input())
numbers = input().split()

total = 0
for i in numbers:
    total += int(i)

expected = n * (n + 1) // 2

print(expected - total)