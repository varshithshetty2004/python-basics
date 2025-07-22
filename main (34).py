def prime_factors(n, i=2):
    if n == 1:
        return
    if n % i == 0:
        print(i, end=' ')
        prime_factors(n//i, i)
    else:
        prime_factors(n, i + 1)
num = int(input("Enter a number:"))
print("Prime factors are:")
prime_factors(num)