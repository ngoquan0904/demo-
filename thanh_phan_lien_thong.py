def bfs(u):
    visited.append(u)
    queue = [u]
    while(queue != []):
        u = queue[0]
        print(u, end =' ')
        queue.remove(u)
        for par in listEdges:
            if u in par:
                v = par[0] if u == par[1] else par[1]
                if v not in visited:
                    visited.append(v)
                    queue.append(v)
    print('\n')
def dfs(u):
    visited.append(u)
    print(u, end=' ')
    for par in listEdges:
        if u in par:
            v = par[0] if u == par[1] else par[1]
            if v not in visited:
                dfs(v)
def connect_component():
    cnt = 0
    for v in listVertexs:
        if v not in visited:
            cnt+=1
            print('Cac dinh thuoc thanh phan lien thong %d la: '%cnt, end='')
            bfs(v)
            # print('\n')
visited = []
listVertexs = [1,2,3,4,5,6,7,8,9,10]
listEdges = [[1,2], [2,3], [2,4], [3,6], [6, 7], [7,3], [5, 8], [9,8]]
connect_component()