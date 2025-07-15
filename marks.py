total = 0
while True:
    a = int(input("Enter the marks (0 to stop): "))
    if a == 0:
        break
    total += a
print("Total marks:", total)
