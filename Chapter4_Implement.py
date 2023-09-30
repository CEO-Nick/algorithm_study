 # Chapter4_Implement
# 4- 1 : 상하좌우
# 내 알고리즘
"""
n = int(input())
moving = list(input().split())
location = [1,1]
for i in range(len(moving)):
    if moving[i] == 'U':
        if location[0] == 1:
            continue
        else:
            location[0] -= 1
    elif moving[i] == 'L':
        if location[1] == 1:
            continue
        else:
            location[1] -= 1
    elif moving[i] == 'R':
        if location[1] == n:
            continue
        else:
            location[1] += 1
    elif moving[i] == 'D':
        if location[0] == n:
            continue
        else:
            location[0] += 1
    print(i,location[0],location[1])
"""

# 교재 
"""
n = int(input())
plans = input().split()
x, y = 1, 1

# L, R, U, D   
dx = [0, 0, -1, 1]  
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x,y)
"""

# 4-2 : 시각
# 내 알고리즘 - 교재 알고와 동일!
"""
n = int(input())
result = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            tmp = str(i)+str(j)+str(k)
            if '3' in tmp:
                result += 1
print(result)
"""

# 2 : 왕실의 나이트
# 내 알고리즘 - 교재와 동일
"""
loc = input()
x = ord(loc[0]); y = int(loc[1])
movement = [(2,-1), (2,1), (-2,-1), (-2,1), (1,-2), (1,-2), (1,2), (-1, 2)]
result = 0

for move in movement:
    nx = x + move[0]
    ny = y + move[1]
    if nx < 97 or nx > 104 or ny < 1 or ny > 8:
        continue
    result += 1
print(result)
"""

# 3 : 게임 개발
"""
n, m = map(int, input().split())
a, b, direction = map(int, input().split())

d = [[0] * m for _ in range(n)]   # 방문한 위치 저장하기 위한 리스트
d[a][b] = 1 # 현재 좌표 방문 처리

array = []
# 전체 맵 정보 받기
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = a + dx[direction]
    ny = b + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0: # 방문한적 없고, 육지일 경우 -> 이동
        d[nx][ny] =1
        count += 1
        x = nx; y = ny
        turn_time = 0
        continue
    else:
        turn_time += 1
    
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if d[nx][ny] == 0:
            x = nx; y = ny
        else:
            break
        turn_time = 0
print(count)
"""

"""
## 백준 구현
    # 16234 : 인구이동
n, l, r = map(int, input().split())
country = []
for i in range(n):
    country.append(list(map(int,input().split())))
"""

## 2023.09.25
# 4-1. 상하좌우
"""
n = int(input())    
plan = list(input().split())

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]   # R L U D 순서

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def direction(direct):
    if direct == "R":
        return 0
    elif direct == "L":
        return 1
    elif direct == "U":
        return 2
    else:
        return 3
    
x, y = 0, 0
for i in range(len(plan)):
    direct = direction(plan[i])
    next_x, next_y = x + dx[direct], y + dy[direct]
    if in_range(next_x, next_y):
        x, y = next_x, next_y
    print(x, y)
    

print(x+1, y+1)
"""

"""
## 2023.09.25
# 4-2. 시각
n = int(input())

cnt = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1
print(cnt)
"""

"""
# 2023.09.26
# 2. 왕실의 나이트
pos = input()
r, c = int(pos[1]), ord(pos[0])  # 'a' -> 아스키코드 97로 변환

dx, dy = [2, 2, -1, 1, -2 , -2, -1, 1], [-1, 1, 2, 2, 1, -1, -2, -2]

def in_range(x, y):
    return 1 <= x and x <= 8 and 97 <= y and y <= 104

cnt = 0
for i in range(8):
    next_x, next_y = r + dx[i], c + dy[i]
    if in_range(next_x, next_y):
        cnt += 1

print(cnt)
"""

# 2023.09.27
# 3. 게임 개발 - 틀림
n, m = map(int, input().split())
x, y, d = map(int, input().split())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

visited = [[False for _ in range(m)] for _ in range(n)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]   # 싱 -> 우 -> 하 -> 좌

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

cnt = 1
turn_time = 0
visited[x][y] = True

while True:
    turn_left()
    nx, ny = x + dx[d], y + dy[d]
    
    if not visited[nx][ny] and grid[nx][ny] == 0:
        turn_time = 0
        x, y = nx, ny
        visited[x][y]
        cnt += 1
        continue
    else:
        turn_time += 1
    
    if turn_time == 4:
        nx, ny = x - dx[d], y - dy[d]
        if grid[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turn_time = 0

print(cnt)

