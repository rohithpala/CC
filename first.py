from collections import defaultdict

First = defaultdict(list)
def first(productionSet,nt,parent):
   
    for x in productionSet[nt]:
        if not x[0].isupper():
            if x[0] not in First[parent]:
                First[parent].append(x[0])
        else:
            first(productionSet,x[0],parent)
productionSet = {'E' : ['TZ'],'Z' : ['+TZ','e'],'T':['FY'],'Y': ['*FY','e'],'F':['(E)','i']}
for key,val in productionSet.items():
    first(productionSet,key,key)
   
for key,val in First.items():
    print("First({0}) = {1}".format(key,val))
