from time import time
from time import sleep

def is_prime(k):
    if k==2 or k==3:
        return True
    elif k>3:
        for i in range(2,int(k**0.5)+1):
            if k%i == 0:
                return False
        return True
                

def get_primes_array(n):
    primes=[]
    for i in range(2,n+1):
        p = is_prime(i)
        if p == True:
            primes.append(i)
    if p == True:
        print(f'The number {i} is prime')
    else:
        print(f"The number {i} isn't prime")
    return primes

print("Enter an integer and positive number above 1!")
n=int(input())
start_time=time()
a=get_primes_array(n)
print(f'Time running for creation array: {time()-start_time}')
print(f'The array of primes numbers till {n}:{a}',)
sleep(30)