import pandas as pd
import numpy as np
data=pd.DataFrame(data=pd.read_csv('can.csv'))
concepts=np.array(data.iloc[:,0:-1])
target=np.array(data.iloc[:,-1])

def learn(concepts,target):
    specific_h=concepts[0].copy()
    print('Initialization of specific_h and general_h: ')
    print(specific_h)
    general_h=[["?" for i in range(len(specific_h))]for i in range(len(specific_h))]
    print(general_h)
    
    for i,h in enumerate(concepts):
        if target[i]=='yes':
            for x in range(len(specific_h)):
                if h[x]!=specific_h[x]:
                    specific_h[x]='?'
                    general_h[x][x]='?'
                print(specific_h)
            print(specific_h)
        if target[i]=='no':
            for x in range(len(specific_h)):
                if h[x]!=specific_h[x]:
                    general_h[x][x]=specific_h[x]
                else:
                    general_h[x][x]='?'
        print('Steps for Candidate eliminaton algorithm ',i+1)
        print(specific_h)
        print(general_h)
    indicies=[i for i,val in enumerate(general_h) if val==['?','?','?','?','?','?']]
    for i in indicies:
        general_h.remove(['?','?','?','?','?','?'])
    return specific_h,general_h
sfinal,gfinal=learn(concepts,target)
print('Final Specific_h:',sfinal,sep='\n')
print('Final General_h',gfinal,sep='\n')
            