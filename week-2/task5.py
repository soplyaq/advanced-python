import re

allowed = "ABCEHKMOPTXY"
pattern = re.compile(f"^[{allowed}][0-9]{{3}}[{allowed}]{{2}}$")

n = int(input())
for _ in range(n):
    plate = input().strip()
    print("Yes" if pattern.match(plate) else "No")
