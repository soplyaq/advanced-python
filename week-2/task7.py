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

