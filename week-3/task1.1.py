arr1 = list(map(int, input("Enter first array: ").split()))
arr2 = list(map(int, input("Enter second array: ").split()))
arr3 = list(map(int, input("Enter third array: ").split()))

for arr in [arr1, arr2, arr3]:
    s = sum(arr)
    avg = s / len(arr)
    print("Sum:", s, "Average:", avg)
