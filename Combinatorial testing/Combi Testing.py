from itertools import combinations
#faulty combinations are (var1=2,var1=1) and (var2=2,var3=3)
inputs={(1,1,1):'Pass',
       (1,1,2):'Pass',
       (1,1,3):'Pass',
       (1,2,1):'Pass',
       (1,2,2):'Pass',
       (1,2,3):'Fail',
       (1,3,1):'Pass',
       (1,3,2):'Pass',
       (1,3,3):'Pass',
       (2,1,1):'Fail',
       (2,1,2):'Fail',
       (2,1,3):'Fail',
       (2,2,1):'Pass',
       (2,2,2):'Pass',
       (2,2,3):'Fail',
       (2,3,1):'Pass',
       (2,3,2):'Pass',
       (2,3,3):'Pass'}
n=3
dictionary={}
variables=('var1','var2','var3')
for i in range(1,n):
    comb=combinations(('var1','var2','var3'),i)
    for i in comb:
        dictionary[i]={}
varnames=[]
for x in range(1,n):
    varnames+=combinations(('var1','var2','var3'),x)
for i in inputs:
    if inputs[i]=='Pass':
        combi=[]
        for x in range(1,n):
            combi+=combinations(i,x)
        ptr=0
        for j in varnames:
            dictionary[j][combi[ptr]]='Not Faulty'
            ptr=ptr+1
for i in inputs:
    if inputs[i]=='Fail':
        combi=[]
        for x in range(1,n):
            combi+=combinations(i,x)
        count=0
        fails={}
        for x in varnames:
            fails[x]=combi[count]
            count+=1
        for x in fails:
            if fails[x] in dictionary[x] and dictionary[x][fails[x]]=='Not Faulty':
                continue
            else:
                variable=list(variables)
                for item in x:
                    variable.remove(item)
                variable=tuple(variable)
                combin=fails[variable]
                if combin in dictionary[variable] and dictionary[variable][combin]=='Not Faulty':
                    dictionary[x][fails[x]]='Faulty'
                else:
                    dictionary[x][fails[x]]='Likely Faulty'
                
print("Failure Inducing Combinations are")
for x in dictionary:
    for y in dictionary[x]:
        if dictionary[x][y] == 'Faulty':
            print(x,y)
print("Suspicious Combinations are")
for x in dictionary:
    for y in dictionary[x]:
        if dictionary[x][y] == 'Likely Faulty':
            print(x,y)
            
                
        
        

        
            

