n = 1 
num = 100000
tempNum = num

while (tempNum//10!=0):
    tempNum //= 10
    n += 1

print(f"{num} is a {n}-number")

