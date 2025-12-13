
A = float(input())  

int_part = int(A)  # целая часть
frac_part = A - int_part  # дробная часть

new_number = frac_part * 100 + int_part / 100
print(round(new_number, 2))