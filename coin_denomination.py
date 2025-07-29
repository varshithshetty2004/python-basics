a = int(input("Enter your amount: "))
a1 = [1, 2, 5, 10, 20, 50, 100, 200, 500]
c = sorted(a1, reverse=True)
for i in c:
    while a >= i:
        print(i, end=" ")
        a -= i
