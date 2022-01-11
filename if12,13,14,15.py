num1 = 7
num2 = 7
num3 = 20
min = 0
med = 0
max = 0

if num1 >= num2:
    if num2 >= num3:
        max = num1
        med  = num2
        min = num3
    elif num2 < num3 :
        max = num1
        med  = num3
        min = num2
elif num2 >= num3:
    if num3 >= num1:
        max = num2
        med = num3
        min = num1
    elif num3 < num1 and num2 >= num1:
        max = num2
        med = num1
        min = num3
elif num3 >= num1:
    if num1 >= num2:
        max = num3
        med = num1
        min = num2
    elif num1 < num2 and num3 >= num2:
        max  = num3
        med  = num2
        min = num1

print(f"{min} < {med} < {max}")






