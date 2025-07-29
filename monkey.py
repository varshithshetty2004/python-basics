def cal(x, a, b):
    height = 0
    time = 0

    while True:
        time += 1
        height += a
        if height >= x:
            return time
        time += 1
        height -= b
print(cal(30,10,5))
