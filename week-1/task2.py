# task2.py

salaries = list(map(int, input().split()))
max_salary = max(salaries)
min_salary = min(salaries)
difference = max_salary - min_salary

print(difference)