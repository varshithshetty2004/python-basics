num=int(input("Enter any number: "))

def gcd(a,b):
    while b!=0:
        temp=a%b 
        a=b 
        b=temp
    return a 
    
def cop(a,b):
    return gcd(a,b)==1 
for i in range(1,num):
    for j in range(1,i):
        for k in range(1,j):
            if(j*j+k*k==i*i) and cop(j,k) and cop(i,k):
                print(i,j,k)