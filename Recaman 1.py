from time import time
from time import sleep

def get_recaman(n):
    rec=[0]

    for i in range(1,n+1):
        #print(rec , i)

        if rec[-1]-i<0:
            rec.append(rec[-1]+i)
        
        else:
            if rec[-1]-i not in rec:
                rec.append(rec[-1]-i)
            else:
                rec.append(rec[-1]+i)
    return  rec

print('Enter the length of the array')
n=int(input())
start_time=time()
a=get_recaman(n)
print(time()-start_time)       
print(a)
sleep(30)