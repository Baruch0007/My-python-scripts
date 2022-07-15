'''
There are n soldiers standing in a circle, every soldier kill his neighbor from the left
(for n=3: soldier1 kill soldier2, 3 kill 1). which soldier will survive depending in n?
'''

def winner(arr):
    print(f'The soldiers:{arr}')
    
    while True:
        temp=[]
        if len(arr)==1:
             return f'The surviver is soldier: {arr[0]} '
            

        elif len(arr)%2==0:
            for i in range(1,len(arr)+1):
                if i%2 == 0:
                    arr[i-1]=0        
            
            for i in arr:
                if i!=0:
                    temp.append(i)
            arr=temp
           
            
        else:
            arr[0] = 0
            for i in range(1,len(arr)+1):
                if i%2 == 0:
                    arr[i-1]=0

            for i in arr:
                if i!=0:
                    temp.append(i)
            arr=temp
        

n=int(input('n: '))
arr=list(range(1,n+1))
print(winner(arr))
