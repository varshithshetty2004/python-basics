def insertion(element):
    l=len(element)
    for i in range(1,l):
        k=element[i]
        j=i-1
        while j>=0 and element[j]>k:
            element[j+1]=element[j]
            j=j-1
            element[j+1]=k
    return element
  
element=[10,12,2,5,7,100,87]
res=insertion(element)
print(res)
