def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def sum_of_digits_is_prime(n):
    digit_sum = sum(int(d) for d in str(n))
    return prime(digit_sum)

def all_digits_prime(n):
    for d in str(n):
        if not prime(int(d)):
            return False
    return True
for i in range(100, 1000):
    if prime(i) and sum_of_digits_is_prime(i) and all_digits_prime(i):
        print(i, end=" ")