from time import sleep

def binary_search (n,lis):
    
    if not lis:
        return False
    
    elif lis[len(lis)//2] == n:
        return True
    
    elif lis[len(lis)//2] > n:
        return binary_search ( n , lis[: len(lis)//2] )

    else:
         return binary_search ( n , lis[(len(lis)//2)+1 :] )
        
              
list1=[1,2,3,4,5]
print(f'Binary Search,Enter an number for checking existstion in this array: {list1}\n ')
print( binary_search (int(input()), list1))

sleep(5)