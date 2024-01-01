def coloring(n, m, edges):
    # lst = [[1,2],[1,3],[2,3], [3,4],[4,5],[4,6], [1,5]]
  dic = {}
  for i in range(1, n + 1):
      dic[i] = sum([edges[j].count(i) for j in range(m)])
  dic = dict(sorted(dic.items(), key= lambda item: item[1], reverse = True))  
  color = [0 for i in range(n)]
  keyVerticle = list(dic.keys())
  for indexV, v in enumerate(keyVerticle):
      for c in range(1, max(dic.values()) + 2):
          for u in (keyVerticle[:indexV]):
              if([u, v] in edges or [v, u] in edges):
                  if(color[u - 1] == c):
                      break
          else:
              color[v - 1] = c
              break
  return color
with open('dothi.txt', 'r') as f:
    n, m = map(int, f.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, f.readline().split())
        edges.append([u, v])
color = coloring(n, m, edges)
with open('dothitomau.dot', 'w') as f:
    f.write("graph dothi {\n")
    for v in range(n):
      f.write("  %d [fillcolor=%d, style=filled];\n" % (v + 1, color[v]))
    for u, v in edges:
      f.write("  %d -- %d;\n" % (u, v))
    f.write("}")
