# Chapter 5. DFS/BFS

# ex) queue
"""
from collections import deque

queue = deque()

queue.append(5)
queue.append(9)
queue.append(6)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(0)
queue.popleft()
print(queue)
queue.reverse()
print(queue)
"""

# ex) recursive func
"""
def recursive_func(i):
    if i == 100:
        return
    print('[%d]번째 출력' %(i+1))
    recursive_func(i+1)
    print(i, '번째 재귀함수를 종료합니다.')

recursive_func(0)
"""

# ex) 인접 행렬
"""
INF = 999999999
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]
print(graph)
"""

# ex) 인접 리스트
"""
graph = [[] for _ in range(3)]  # 행이 3개인 2차원 리스트 선언

graph[0].append((1,7))
graph[0].append((2,5))

graph[1].append((0,7))

graph[2].append((0,5))

print(graph)
"""

# ex) DFS 메서드 정의
"""
graph = [           # 각 노드가 연결된 정보를 2차원 리스트 자료형으로 표현
    [],
    [2,3,8],
    [1, 7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9   # 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
"""

"""
def dfs(graph, v, visited):
    # 현재 노드 방문처리
    visited[v] = True 
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited)
"""

# ex) BFS 메서드 정의
"""
from collections import deque  

def bfs(graph, start, visited):
    queue = deque([start])

    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
bfs(graph, 1, visited)
"""

# 3. 음료수 얼려먹기
"""
n, m = map(int, input().split())
ice = []
for i in range(n):
    ice.append(list(map(int, input())))

def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m :
        return False
    if ice[x][y] == 0:
        ice[x][y] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            print(i,j)
            result += 1
print(result)
"""

"""
# 4. 미로 탈출
from collections import deque

n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >=n or ny >= m:
                continue
            if maze[nx][ny] == 0:
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                print(nx, ny, maze[nx][ny])
                queue.append((nx, ny))

    
    return maze[n-1][m-1]

print(bfs(0,0))
"""

n, m = map(int, input().split())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

visited = [[False for _ in range(m)] for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 1:
        return False
    
    return True

def dfs(x, y):
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y +dy
        if can_go(nx, ny):
            visited[x][y] = True
            dfs(nx, ny)
            return True
    return False

res = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            continue
        visited[i][j] = True
        if dfs(i, j):
            res += 1

print(res)