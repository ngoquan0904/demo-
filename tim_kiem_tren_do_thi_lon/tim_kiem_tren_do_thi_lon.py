#Ngô Minh Quân - 20225383 

def build_graph():
    for i in range(len(list_words)):
        for j in range(i+1, len(list_words)):
            if sum(1 for a, b in zip(list_words[i], list_words[j]) if a != b) == 1:
                list_edges.append([list_words[i], list_words[j]])

def bfs(u, visited):
    visited.append(u)
    queue = [u]
    while(queue != []):
        u = queue[0]
        queue.remove(u)
        for par in list_edges:
            if u in par:
                v = par[0] if u == par[1] else par[1]
                if v not in visited: 
                    parents[v] = u
                    visited.append(v)
                    queue.append(v)

def connect_component():
    cnt = 0
    for v in list_words:
        if v not in visited:
            cnt+=1
            bfs(v, visited)
    return cnt

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

list_words = []
list_edges = []
visited = []
parents = {}
with open('sgb-words.txt', 'r') as f:
    v = f.readline().rstrip('\n')
    while(v != ''):
        list_words.append(v)
        v = f.readline().rstrip('\n')
build_graph()
for vertex in list_words:
    parents[vertex] = vertex
cnt = connect_component()
print(cnt)

s, t = input().split()
path(s, t)

