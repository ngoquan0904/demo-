def pushEdge(m, edges):
	for _ in range(m):
		u, v = input().split()
		edges.append([u,v])
def dfs(v, visited, edges, clock):
	visited[v] = [clock]
	clock += 1
	for par in edges:
		if par[0] == v and par[1] not in visited:
			dfs(par[1], visited, edges, clock)
	else:
		visited[v].append(clock)
		clock += 1
	return visited
n, m = map(int, input().split())
edges = []
pushEdge(m, edges)
visited = {}
clock = 1
visited = dfs(input(), visited, edges, clock)
print(visited)


