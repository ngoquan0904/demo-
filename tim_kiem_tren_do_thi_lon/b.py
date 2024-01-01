#Ngô Minh Quân - 20225383 

def build_graph():
	for i in range(len(list_words)):
		for j in range(len(list_words)):
			if j != i:
				tmp = list(list_words[j])
				for char in list_words[i][1:]:
					if char not in tmp:
						break
					else:
						tmp.remove(char)

				else:
					list_edges.append([list_words[i], list_words[j]])



def dfs(v, visited, list_edges, visited_scc):
	visited.append(v)
	visited_scc.append(v)
	for par in list_edges:
		if par[0] == v and par[1] not in visited_scc:
			dfs(par[1], visited, list_edges, visited_scc)
	return visited

def transpose_graph(list_edges):
	swap = lambda x: [x[1], x[0]]
	list_edges = [swap(par) for par in list_edges]
	return list_edges

def SCC(list_words, list_edges):
	list_edges = transpose_graph(list_edges)
	scc = []
	visited_scc = []
	for v in list_words:
		if v not in visited_scc:
			lst = []
			scc.append(dfs(v, lst, list_edges, visited_scc))
	return scc 

def bfs(u, visited):
    visited.append(u)
    queue = [u]
    while(queue != []):
        u = queue[0]
        queue.remove(u)
        for par in list_edges:
            if u == par[0]:
                v = par[1]
                if v not in visited: 
                    parents[v] = u
                    visited.append(v)
                    queue.append(v)
def path(s, t):
    path = []
    visited_start_s = []
    bfs(s, visited_start_s)
    if(t not in visited_start_s):
        print("Khong co duong di")
    else:
        while (t != s):
            path.append(t)
            t = parents[t]
        path.append(s)
        path.reverse()
        print(*path)
#
list_words = []
list_edges = []
with open('sgb-words.txt', 'r') as f:
    v = f.readline().rstrip('\n')
    while(v != ''):
    	# if v not in list_words:
    	list_words.append(v)
    	v = f.readline().rstrip('\n')
build_graph()
print(len(list_words))
scc = SCC(list_words, list_edges)
print(len(scc))

#b.
u = input()
for par in scc:
	if u in par:
		print(par)

#c
parent = {} 
s, t = input.split()
path(s, t)




