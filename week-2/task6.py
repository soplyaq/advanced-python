<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
def all_eq(lst):
    max_len = 0

    for s in lst:
        if len(s) > max_len:
            max_len = len(s)

    result = []
    for s in lst:
        while len(s) < max_len:
            s += "_"
        result.append(s)

    return result

print(all_eq(["hi", "hello", "hey"]))

=======
>>>>>>> f167d6e (Add week-3 tasks)
def all_eq(lst):
    max_len = 0

    for s in lst:
        if len(s) > max_len:
            max_len = len(s)

    result = []
    for s in lst:
        while len(s) < max_len:
            s += "_"
        result.append(s)

    return result

<<<<<<< HEAD
print(all_eq(["wow", "mimi", "lyalya"]))

=======
print(all_eq(["hi", "hello", "hey"]))

>>>>>>> fcf8732 (Assignment 2)
>>>>>>> f167d6e (Add week-3 tasks)
=======
def all_eq(lst):
    max_len = 0

    for s in lst:
        if len(s) > max_len:
            max_len = len(s)

    result = []
    for s in lst:
        while len(s) < max_len:
            s += "_"
        result.append(s)

    return result

print(all_eq(["hi", "hello", "hey"]))

>>>>>>> 2d7dd3c8abe5127fffaae38ccd8350a63732413f
