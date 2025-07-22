def is_prime(n):
    if n < 2: 
        return False
    for i in range(2, int(n*0.5)+1):
        if n % i == 0: 
            return False
    return True

def digits_prime():
    while n>0:
        
        

for i in range(100,999):
    if is_prime(i) and is_prime(digit[i]) and digits_prime(i):
        print(i)