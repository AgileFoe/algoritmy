
from collections import deque

# 1
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}

print("Граф:", graph)

# 2
graph['F'] = ['A', 'E']
graph['A'].append('F')
graph['E'].append('F')

print("\nПосле добавления вершины F:", graph)

# 3
def get_neighbors(graph, node):
    return graph.get(node, [])

print("\nСоседи вершины A:", get_neighbors(graph, 'A'))

# 4
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(node)
    print(node, end=' ')
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return visited

print("\n\nDFS (рекурсивный) от A:")
visited_dfs = dfs(graph, 'A')

# 5
def dfs_stack(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            stack.extend(reversed(graph[node]))
    
    return visited

print("\n\nDFS (стек) от A:")
visited_stack = dfs_stack(graph, 'A')

# 6
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(graph[node])
    
    return visited

print("\n\nBFS от A:")
visited_bfs = bfs(graph, 'A')

# 7
start = 'A'  # можно заменить input()

print("\n\nОбход от вершины:", start)

print("DFS:")
dfs(graph, start)

print("\nBFS:")
bfs(graph, start)

# 8
def has_path(graph, start, end):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        
        if node == end:
            return True
        
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])
    
    return False

print("\n\nЕсть ли путь A -> E:", has_path(graph, 'A', 'E'))
print("Есть ли путь B -> F:", has_path(graph, 'B', 'F'))

# 9
def reachable_count(graph, start):
    visited = dfs(graph, start)
    return len(visited)

print("\n\nКоличество достижимых из A:", reachable_count(graph, 'A'))


# 10

def shortest_path(graph, start, end):
    queue = deque([(start, [start])])
    visited = set()
    
    while queue:
        node, path = queue.popleft()
        
        if node == end:
            return path
        
        if node not in visited:
            visited.add(node)
            
            for neighbor in graph[node]:
                queue.append((neighbor, path + [neighbor]))
    
    return None

print("\nКратчайший путь A -> E:", shortest_path(graph, 'A', 'E'))
print("Кратчайший путь B -> F:", shortest_path(graph, 'B', 'F'))
