m = int(input())
arr = list(map(int, input().split()))

print("Original:", arr)

arr[0], arr[-1] = arr[-1], arr[0]

print("Result:", arr)
