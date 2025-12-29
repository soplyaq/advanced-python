def inside(x, y, r, px, py):
    return (px-x)**2 + (py-y)**2 <= r*r

x = float(input())
y = float(input())
r = float(input())

count = 0
for i in range(3):
    px = float(input())
    py = float(input())
    if inside(x, y, r, px, py):
        count += 1

print(count)
