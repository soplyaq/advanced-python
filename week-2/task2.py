<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
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
=======
>>>>>>> f167d6e (Add week-3 tasks)
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
<<<<<<< HEAD
=======
>>>>>>> fcf8732 (Assignment 2)
>>>>>>> f167d6e (Add week-3 tasks)
=======
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
>>>>>>> 2d7dd3c8abe5127fffaae38ccd8350a63732413f
