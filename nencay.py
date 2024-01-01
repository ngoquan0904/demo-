# Ngô Minh Quân - 20225383
# Mã lớp: 144870

numEdge = int(input())
# danh sach canh   
listEdge = []                                                                                                                 
for i in range(numEdge):
    e1, e2 = map(int, input().split())                                              
    listEdge.append([e1, e2])
# so dinh
numOfVertex = max(max(listEdge[i]) for i in range(numEdge)) + 1                     

listPrufer = []
listDegree = []

#bac cac dinh
for v in range(1, numOfVertex):
    listDegree.append(sum(listEdge[i].count(v) for i in range(numEdge)))

for v in range(1, numOfVertex - 1):
    # tim dinh bac 1 co nhan nho nhat != 0
    m = min([i for i in range(1, numOfVertex) if listDegree[i - 1] == 1])
    # canh k chua m
    [k] = [par for par in listEdge if m in par]
    # giam bac moi dinh thuoc k di 1
    listDegree[m - 1] = 0
    if 0 not in k:
        listDegree[k[0] - 1 if k[0] != m else k[1] - 1] -= 1
    #bo di canh k
    listEdge.remove(k)
    listPrufer.append(k[0] if k[0] != m else k[1])

print(*listPrufer)
