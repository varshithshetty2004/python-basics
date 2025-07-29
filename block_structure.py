a = int(input("enter the blocks:"))
b = int(input("enter the lines:"))
c = int(input("enter the stars:"))
sum = 0
print("----------------")
for i in range(a):
    print(f"------{i + 1}------------")
    count = 0
    for j in range(b - i):
        for k in range(c):
            print("*", end=" ")
        print()
