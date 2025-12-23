a = input().strip()
b = input().strip()

m = len(b)
double_b = b + b
shifts = set(double_b[i:i+m] for i in range(m))

count = 0
for i in range(len(a) - m + 1):
    if a[i:i+m] in shifts:
        count += 1

print(count)
