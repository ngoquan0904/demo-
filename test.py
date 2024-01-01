def dfs(u, visited, list_vertex, visited_scc):
	visited_scc.append(u)
	visited.append(u)
	for par in list_vertex:
		if u == par[0] and par[1] not in visited_scc:
			dfs(par[1], visited, list_vertex, visited_scc)
	return visited

def transpose_graph(list_vertex):
	swap = lambda x: [x[1], x[0]]
	list_vertex = [swap(par) for par in list_vertex]
	return list_vertex

def strongly_connect_component(listv, list_vertex):
	list_vertex = transpose_graph(list_vertex)
	scc = []
	visited_scc = []
	for v in listv:
		if v not in visited_scc:
			lst = []
			scc.append(dfs(v, lst, list_vertex, visited_scc))
	return scc


listv = ['A','B','C','D','E','F','G','H','I','J','K','L']
list_vertex = [['A','B'], ['B','C'], ['C','F'], ['F','C'], ['B','E'], ['E','B'], ['B','D'], ['E','F'], ['F','H'], ['E','G'], ['G','H'], ['I','G'], ['G','J'], ['H','K'], ['K','L'], ['L','J'], ['J', 'I']]
print(strongly_connect_component(listv, list_vertex))
