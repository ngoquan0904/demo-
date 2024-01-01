#hello
def inputEdges():
    for i in range(edges):
        u, v, l = input().split()
        if u not in listOfEdges: listOfEdges.append(u)
        if v not in listOfEdges: listOfEdges.append(v) 
        length[(u, v)] = int(l)

def make_set():
    for par in listOfEdges:
        parent[par] = par
        size[par] = 1

def find(u):
    if parent[u] == u: return u
    return find(parent[u])

def union(u, v):
    u = find(u)
    v = find(v)
    if (u == v): return False
    if(size[u] < size[v]): u, v = v, u
    parent[v] = u  
    size[u] += size[v]
    return True

def kruskal(length):
    d = 0
    length = dict(sorted(length.items(), key = lambda item: item[1]))
    mst = []
    for par in length.keys():
        if len(mst) == edges - 1: break
        par = list(par)
        if union(par[0], par[1]):
            mst.append(par)
            d += length[tuple(par)]
    if len(mst) != vertexs - 1:
        print("do thi khong lien thong")
    else:
        print("MST: ", d)
        for par in mst:
            print(*par, length[tuple(par)])

vertexs, edges = map(int, input().split())
listOfEdges = []
length = {}
inputEdges()
parent = {}
size = {}
make_set()
kruskal(length)
