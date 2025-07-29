n = "aaabbcccccaannnn"
c = 1
res = ""
for i in range(len(n) - 1):
    if n[i] == n[i + 1]:
        c += 1
    else:
        res = res + n[i] + str(c)
        c = 1
res = res + n[-1] + str(c)
print(res)
