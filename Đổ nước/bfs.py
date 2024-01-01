def pushEdge(m, listEdges):
	for _ in range(m):
		u, v = input().split()
		listEdges.append([u,v])
def bfs(u, dist, listEdges):
	dist[u] = 0
	queue = [u]
	while(queue != []):
		u = queue[0]
		queue.remove(u)
		for par in listEdges:
			if u in par:
				v = par[1] if u == par[0] else par[0]
				if v not in dist:
					queue.append(v)
					dist[v] = dist[u] + 1
	return dist
vertex, edges = map(int, input().split())
listEdges = []
pushEdge(edges, listEdges)
dist = {}
print(bfs(input(), dist, listEdges))
