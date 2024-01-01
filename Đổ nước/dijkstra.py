def pushEdges(edges, listVertexs, l):
	for _ in range(edges):
		u, v, length = input().split()
		listVertexs.append(u) if u not in listVertexs else None
		listVertexs.append(v) if v not in listVertexs else None
		l[(u,v)] = int(length)
def dijkstra(s, l, listVertexs):
	dist = {}
	for v in listVertexs:
		dist[v] = 100000
	dist[s] = 0
	while listVertexs != []:
		minDist = min([dist[par] for par in listVertexs])
		for par in listVertexs:
			if(dist[par]) == minDist:
				u = par
				listVertexs.remove(u)
		lCopy = l.copy()
		for par in lCopy.keys():
			if par[0] == u:
				v = par[1]
				if dist[v] > dist[u] + l[par]:
					dist[v] = dist[u] + l[par] 
				l.pop(par)
	return dist

vertexs, edges = map(int, input().split())
listVertexs = []
l = {}
pushEdges(edges, listVertexs, l)
print(dijkstra(input(), l, listVertexs))
