a=int(input("enter the number:"))
b=int(input("enter the number:"))
while b != 0:
    a, b = b, a % b

print("GCD is:", a)
