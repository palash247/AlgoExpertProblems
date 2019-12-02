def riverSizes(matrix):
    # Write your code here.
    visited = [[False  for x in row] for row in matrix]
    i,j = 0,0
    sizes = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if visited[i][j]:
                continue
            traverse_node(i,j,matrix,visited,sizes)
    return sizes

def traverse_node(i,j,matrix,visited,sizes):
    current_size = 0
    node_to_traverse = [[i,j]]
    while len(node_to_traverse)>0:
        current_node = node_to_traverse.pop()
        x,y = current_node
        if visited[x][y]:
            continue
        visited[x][y] = True
        if matrix[x][y] == 0:
            continue
        current_size += 1
        unvisited_neighbours = []
        get_unvisited_neighbours(x,y,visited,unvisited_neighbours)
        node_to_traverse.extend(unvisited_neighbours)
    if current_size > 0:
        sizes.append(current_size)

def get_unvisited_neighbours(x,y,visited,unvisited_neighbours):
    if x > 0 and not visited[x-1][y]:
        unvisited_neighbours.append([x-1,y])
    if x < len(visited)-1 and not visited[x+1][y]:
        unvisited_neighbours.append([x+1,y])
    if y > 0 and not visited[x][y-1]:
        unvisited_neighbours.append([x,y-1])
    if y < len(visited[0])-1 and not visited[x][y+1]:
        unvisited_neighbours.append([x,y+1])
