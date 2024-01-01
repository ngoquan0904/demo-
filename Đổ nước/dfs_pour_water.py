# Ngô Minh Quân - 20225383

def pour_water_dfs(current_state, full_state, visited):

    visited.add(current_state)
    
    # Nếu có bình 2 or 3 chứa 2 đơn vị nước, dừng 
    if 2 in list(current_state)[1:]:
        print("\"{}\" [fillcolor=red, style=filled];".format(current_state))
        return 1
    print("\"{}\"".format(current_state), end='->')

    # Thử các cách đổ nước và tiếp tục tìm kiếm
    for i in range(len(current_state)):
        for j in range(len(current_state)):
            if i != j:
                pour = min(current_state[i], full_state[j] - current_state[j])
                new_state = list(current_state)
                new_state[i] -= pour
                new_state[j] += pour
                if tuple(new_state) not in visited:
                    print("\"{}\"".format(tuple(new_state)),end=';\n')
                    result = pour_water_dfs(tuple(new_state), full_state, visited)
                    if result is not None:    
                        return 1
    return None

def pour_water_tree(current_state, full_state):
    visited = set()
    pour_water_dfs(current_state, full_state, visited)


# Trạng thái ban đầu: (0, 7, 4), trạng thái đầy: (10, 7, 4)
current_state = (0, 7, 4)
full_state = (10, 7, 4)

print("digraph {")
pour_water_tree(current_state, full_state)
print("}")