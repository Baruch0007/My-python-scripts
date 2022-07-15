# Greatest Common Divisor (Euclidean algorithm - אוקלידיס)

from time import time

def gcd(x,y):
    
    if x%y==0 or x%y==0:
        return y if x>y else x   
    
    while x!=y:
        
        if x>y:        
            x-=y
        else:
            y-=x
            
    if x==y:
        return x



x=int(input('Enter first number '))
y=int(input('Enter second number '))
start_time=time()
a = gcd(x,y)
print(time()-start_time)
print(f'The Gratest divisor is {a}')
