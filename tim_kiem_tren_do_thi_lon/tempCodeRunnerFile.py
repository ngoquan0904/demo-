
# 	for i in range(len(list_words)):
# 		for j in range(len(list_words)):
# 			if j != i:
# 				for char in list_words[i][1:]:
# 					if list_words[i][1:].count(char) != list_words[j].count(char):
# 						break
# 				else:  
# 					list_edges.append([list_words[i], list_words[j]])

def build_graph():
	for i in range(len(list_words)):
		for j in range(len(list_words)):
			if j != i:
				tmp = list(list