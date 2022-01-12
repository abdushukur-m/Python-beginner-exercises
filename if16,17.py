num1 = 17
num2 = 2
num3 = 0

#16
nums = [num1, num2, num3]
if num1 <= num2 and num2 <= num3:
    print(2*num1, 2*num2, 2*num3)
else:
    print(-num1, -num2, -num3)
#17
if (num1 <= num2 and num2 <= num3) or (num1 >= num2 and num2 >= num3):
    print(2*num1, 2*num2, 2*num3)
else:
    print(-num1, -num2, -num3)