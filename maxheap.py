import heapq
elemets=[20,40,30,1,3,6,2,5,36]
max_heap=[]
for i in elemets:
    heapq.heappush(max_heap,-i)
res=[-i for i in max_heap]
print(res)
