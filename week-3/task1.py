print("Choose shape:")
print("1 - rectangle")
print("2 - circle")
print("3 - triangle")

choice = int(input())

if choice == 1:
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    area = a * b
    print(area)

elif choice == 2:
    r = float(input("Enter radius: "))
    area = 3.14 * r * r
    print(area)

elif choice == 3:
    a = float(input("Enter base: "))
    h = float(input("Enter height: "))
    area = 0.5 * a * h
    print(area)
