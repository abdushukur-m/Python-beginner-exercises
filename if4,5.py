num1 = 1
num2 = -7
num3 = 2

nums = [num1, num2, num3]

posNum = 0
negNum = 0

for num in nums:
    if num > 0:
        posNum += 1
    elif num < 0:
        negNum += 1
print(f"Positive numbers: {posNum}\nNegative numbers: {negNum}")


