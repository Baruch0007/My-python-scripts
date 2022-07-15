from time import sleep

def factorial (n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)


print(f"The result is: {factorial(int(input('Enter an integer and not negative number for factorial calculation: ')))} ")


sleep(5)