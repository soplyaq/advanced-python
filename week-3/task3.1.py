s = input()

words = s.split()
result = []

for w in words:
    result.append("".join(sorted(w)))

print(" ".join(result))
