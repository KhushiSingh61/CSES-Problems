s = input().strip()

best = 1
current = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        current += 1
    else:
        current = 1

    if current > best:
        best = current

print(best)