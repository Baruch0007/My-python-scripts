from time import sleep

def factorial (target):
    total=1
    for counter in range(1,target+1):
        total*=counter
        print(f'Factorial of: {counter}! = {total} ')
    return total


print(f"Total result: {factorial(int(input('Enter an integer and not negative number for factorial calculation: ')))} ")

sleep(3)