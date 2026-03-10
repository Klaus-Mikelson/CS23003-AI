from collections import deque
nodes = ['A','B','C','D','E','F','G','H','I','J']
graph = [
    [0,6,0,0,0,3,0,0,0,0],
    [6,0,3,2,0,0,0,0,0,0],
    [0,3,0,1,5,0,0,0,0,0],
    [0,2,1,0,8,0,0,0,0,0],
    [0,0,5,8,0,0,0,0,5,5],
    [3,0,0,0,0,0,1,7,0,0],
    [0,0,0,0,0,1,0,0,3,0],
    [0,0,0,0,0,7,0,0,2,0],
    [0,0,0,0,5,0,3,2,0,3],
    [0,0,0,0,5,0,0,0,3,0]
]
heuristic = [10,8,5,7,3,6,5,3,1,0]

def astar(start, goal):
    open_list = deque()
    closed_list = []
    graph_cost = {}
    parent = {}

    for node in nodes:
        graph_cost[node] = 9999
    
    graph_cost[start] = 0
    parent[start] = None
    open_list.append(start)
    
    while open_list:
        current = open_list[0]
        for node in open_list:
            if (graph_cost[node] + heuristic[nodes.index(node)]) < (graph_cost[current] + heuristic[nodes.index(current)]):
                current = node
    
        if current == goal:
            break
    
        open_list.remove(current)
        closed_list.append(current)
        current_index = nodes.index(current)
    
        for i in range(len(nodes)):
            if graph[current_index][i] != 0:
                neighbor = nodes[i]
                new_cost = graph_cost[current] + graph[current_index][i]
    
                if neighbor not in closed_list and new_cost < graph_cost[neighbor]:
                    graph_cost[neighbor] = new_cost
                    parent[neighbor] = current
    
                    if neighbor not in open_list:
                        open_list.append(neighbor)
    
    # Path reconstruction
    path = []
    temp = goal
    
    while temp is not None:
        path.append(temp)
        temp = parent[temp]
    
    path.reverse()
    print("A* Path:", path)
    print("A* Shortest Path Cost:", graph_cost[goal])

astar('A','G')
