colorWord = ['','red', 'green','blue','yellow','black','white','pink','brown','grey','violet','orange']

# tìm đỉnh có liên quan hạ bậc đi 1 và thêm c vào danh sách cấm
def relatedVertex(edges, v, dic, c, banColor):
  for u in dic.keys():
    if([u,v] in edges or [v, u] in edges):
      # dic[u] -= 1
      banColor[u - 1].append(c)

#chon màu nằm ngoài ds cấm
def chooseColor(maxDegree, v, banColor, color):
  for c in range(1, maxDegree + 2):
        if(c not in banColor[v - 1]):
          color[v - 1] = c
          break
  return c

def coloring(n, m, edges):
  dic = {}
  #tìm bậc
  for i in range(1, n + 1):
      dic[i] = sum([edges[j].count(i) for j in range(m)])

  banColor = [[] for i in range (n)]
  color = [0 for i in range(n)]
  maxDegree = max(dic.values())
 
  for count in range(n):
    #đỉnh có bậc cao nhất
    v = max(dic.items(), key= lambda item: item[1])[0]
    c = chooseColor(maxDegree, v, banColor, color)
    relatedVertex(edges, v, dic, c, banColor)
    dic.pop(v)
  return color

with open('dothi.txt', 'r') as f:
  n, m = map(int, f.readline().split())
  edges = []
  for _ in range(m):
    u, v = map(int, f.readline().split())
    edges.append([u,v])
color = coloring(n, m , edges)

with open('dothitomau.dot', 'w') as f:
  f.write("graph dothi {\n")
  for v in range(n):
    f.write("  %d [fillcolor=%s, style=filled];\n" % (v + 1, colorWord[color[v]]))
  for u, v in edges:
    f.write("  %d -- %d;\n" % (u, v))
  f.write("}")