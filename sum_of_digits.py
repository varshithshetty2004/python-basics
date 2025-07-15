a = int(input("Enter the number: "))
sum_digits = 0
while a > 0:
    sum_digits += a % 10
    a //= 10
print("Sum of digits:", sum_digits)
