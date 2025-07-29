sum = 0
while True:
    x = int(input("Enter the number: "))
    if x == 0:
        break
    if x < 100 and x % 2 != 0 and x % 3 != 0 and x % 5 != 0:
        sum += x
print("Filtered sum:", sum)
