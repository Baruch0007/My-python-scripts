# Change machine which counting the amount of each bill to give back to customer

from time import sleep

def give_change(change,bills):
    
    if change==0:
        return 'nothing to return'
    
    while True:
        
        change=round(change,1)
        for i in range(len(bills)):
            if change < bills[i]:
                print(f'For {change} you have to give bill of: {bills[i-1]} \n')
                change=change-bills[i-1]
                break
            elif change==bills[i]:
                print(f'For {change} you have to give bill of: {bills[i]} \n')
                change=change-bills[i]
                break
            elif change > bills[i] and i==len(bills)-1:
                print(f'For {change} you have to give bill of: {bills[i]} \n')
                change=change-bills[i]
                break

        if change==0:
            break
        
    return 'All change had returned'
        
    

bills=[0.1, 0.5, 1 , 2 , 5 , 10 , 20 , 50 , 100 , 200]
print( give_change(float(input('Enter the amount of change:\n ')) , bills)) #134.9

sleep(5)