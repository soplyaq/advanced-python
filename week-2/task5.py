<<<<<<< HEAD
<<<<<<< HEAD
import re

allowed = "ABCEFHKMOPTXYZ"
=======
<<<<<<< HEAD
import re

allowed = "ABCEHKMOPTXY"
pattern = re.compile(f"^[{allowed}][0-9]{{3}}[{allowed}]{{2}}$")

n = int(input())
for _ in range(n):
    plate = input().strip()
    print("Yes" if pattern.match(plate) else "No")
=======
import re

allowed = "ABCEHKMOPTXY"
>>>>>>> f167d6e (Add week-3 tasks)
pattern = re.compile(f"^[{allowed}][0-9]{{3}}[{allowed}]{{2}}$")

n = int(input())
for _ in range(n):
    plate = input().strip()
    print("Yes" if pattern.match(plate) else "No")
<<<<<<< HEAD
=======
>>>>>>> fcf8732 (Assignment 2)
>>>>>>> f167d6e (Add week-3 tasks)
=======
import re

allowed = "ABCEHKMOPTXY"
pattern = re.compile(f"^[{allowed}][0-9]{{3}}[{allowed}]{{2}}$")

n = int(input())
for _ in range(n):
    plate = input().strip()
    print("Yes" if pattern.match(plate) else "No")
>>>>>>> 2d7dd3c8abe5127fffaae38ccd8350a63732413f
