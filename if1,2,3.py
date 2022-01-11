#1

num = int(input("Enter a number: "))

if num < 0:
    num -= 2
    print(num)
elif num > 0:
    num += 1
    print(num)
else:
    num = 10
    print(num)

