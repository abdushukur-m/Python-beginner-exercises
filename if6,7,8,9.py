num1 = 70
num2 = 15

print(f"num1 = {num1}, num2 = {num2}")
print(f"{num1} > {num2}") if num1 > num2 else print(f"{num1} < {num2}")

temp = num1
num1 = num2
num2 = temp
print(f"num1 = {num1}, num2 = {num2}")

