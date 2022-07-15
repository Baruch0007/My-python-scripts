from time import sleep

counter=1
total=1
target=int(input('Enter an integer and not negative number for factorial calculation:\n '))

while counter <= target:
    total*=counter
    print(f'Factorial of: {counter}! = {total} ')
    counter+=1

print(f'Total result: {total}')
    
sleep(5)

