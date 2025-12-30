<<<<<<< HEAD

eq = input().strip()

a, op, b, _, c = eq

if a == 'x':
    b = int(b)
    c = int(c)
    x = c - b if op == '+' else c + b
elif b == 'x':
    a = int(a)
    c = int(c)
    x = c - a if op == '+' else a - c
else:
    a = int(a)
    b = int(b)
    x = a + b if op == '+' else a - b

print(x)
=======
>>>>>>> f167d6e (Add week-3 tasks)
eq = input().strip()

a, op, b, _, c = eq

if a == 'x':
    b = int(b)
    c = int(c)
    x = c - b if op == '+' else c + b
elif b == 'x':
    a = int(a)
    c = int(c)
    x = c - a if op == '+' else a - c
else:
    a = int(a)
    b = int(b)
    x = a + b if op == '+' else a - b

print(x)
<<<<<<< HEAD
=======
>>>>>>> fcf8732 (Assignment 2)
>>>>>>> f167d6e (Add week-3 tasks)
=======
eq = input().strip()

a, op, b, _, c = eq

if a == 'x':
    b = int(b)
    c = int(c)
    x = c - b if op == '+' else c + b
elif b == 'x':
    a = int(a)
    c = int(c)
    x = c - a if op == '+' else a - c
else:
    a = int(a)
    b = int(b)
    x = a + b if op == '+' else a - b

print(x)
>>>>>>> 2d7dd3c8abe5127fffaae38ccd8350a63732413f
