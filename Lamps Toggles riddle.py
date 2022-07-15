# There is 100 lamps and for each lamp there is his own toggle.
# each toggle turn on his own lamp and the multiplies of this lamp
# for instance: toggle number 4 will turn on lamp number 4 and lamps numbers 8,12,16,20
# which lamps will remain lit after changing position of all 100 toggles?

import numpy as np

n=100
lamps = list(np.zeros(n,dtype='bool'))
numeration = list(range(1,n+1))


for toggel in numeration:
    
    #print(f'toggel number: {toggel}')
    for index, lamp in zip(numeration,lamps):
        if index % toggel == 0 and  lamps[index-1]== False:
            lamps[index-1]= True
        elif index % toggel == 0 and  lamps[index-1]== True:
            lamps[index-1]=False
            
        #print(index,lamps[index-1])
    #print()

results=[]
for index,lamp in zip(numeration,lamps):
    if lamp:
        results.append(index)
        
print(f'For {n} toggels the result: {results}')



    
