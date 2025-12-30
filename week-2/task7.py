<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
from collections import Counter

items = input().split()
count = Counter(items)

print("Purchase frequency:")
for item, c in count.items():
    print(f"{item}: {c}")

most_popular = max(count, key=count.get)
print("Most popular item:", most_popular)

once = [item for item in count if count[item] == 1]
print("Purchased once:", " ".join(once))

print("Sorted by frequency:")
for item, c in count.most_common():
    print(item, c)

=======
>>>>>>> f167d6e (Add week-3 tasks)
from collections import Counter

items = input().split()
count = Counter(items)

print("Purchase frequency:")
for item, c in count.items():
    print(f"{item}: {c}")

most_popular = max(count, key=count.get)
print("Most popular item:", most_popular)

once = [item for item in count if count[item] == 1]
print("Purchased once:", " ".join(once))

print("Sorted by frequency:")
for item, c in count.most_common():
    print(item, c)

<<<<<<< HEAD
=======
>>>>>>> fcf8732 (Assignment 2)
>>>>>>> f167d6e (Add week-3 tasks)
=======
from collections import Counter

items = input().split()
count = Counter(items)

print("Purchase frequency:")
for item, c in count.items():
    print(f"{item}: {c}")

most_popular = max(count, key=count.get)
print("Most popular item:", most_popular)

once = [item for item in count if count[item] == 1]
print("Purchased once:", " ".join(once))

print("Sorted by frequency:")
for item, c in count.most_common():
    print(item, c)

>>>>>>> 2d7dd3c8abe5127fffaae38ccd8350a63732413f
