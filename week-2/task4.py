<<<<<<< HEAD
=======
<<<<<<< HEAD
n, m = map(int, input().split())
text = input().strip()

words = set()
for i in range(n - m + 1):
    words.add(text[i:i+m])

print(len(words))
=======
>>>>>>> f167d6e (Add week-3 tasks)
n, m = map(int, input().split())
text = input().strip()

words = set()
for i in range(n - m + 1):
    words.add(text[i:i+m])

print(len(words))
<<<<<<< HEAD
=======
>>>>>>> fcf8732 (Assignment 2)
>>>>>>> f167d6e (Add week-3 tasks)
