#1. 교점에 별 만들기 -Level2
# 2023-10-06 -> CORRECT
# def solution(line):
#     answer = []
#     starPoints = []
#     max_x = max_y = -int(1e15)
#     min_x = min_y = int(1e15)

#     # 정수 교점 찾기 & 최대,최소 지점 찾기
#     for i in range(len(line)):
#         for j in range(i+1, len(line)):
#             tmp_x, tmp_y = findIntersection(line[i], line[j])
#             # 정수인지 판별 & x, y의 최대 최소 구하기
#             if tmp_x.is_integer() and tmp_y.is_integer():
#                 tmp_x, tmp_y = int(tmp_x), int(tmp_y)
#                 max_x, max_y = max(max_x, tmp_x), max(max_y, tmp_y)
#                 min_x, min_y = min(min_x, tmp_x), min(min_y, tmp_y)
#                 starPoints.append([tmp_x, tmp_y])

#     i = 0
#     # y축은 위에서 아래로 x축은 좌에서 우로 진행
#     for y in range(max_y, min_y-1, -1):
#         str = ""
#         for x in range(min_x, max_x+1):
#             if [x, y] in starPoints:
#                 str += "*"
#             else:
#                 str += "."
#         answer.append(str)

#     return answer




# # 교점이 있으면 교점을 리턴, 없으면(=일치 or 평행) (1.1, 1.1) 리턴 
# def findIntersection(point1, point2):
#     a, b, e = point1[0], point1[1], point1[2]
#     c, d, f = point2[0], point2[1], point2[2]

#     tmp = a*d - b*c
    
#     if tmp != 0:
#         cal_x = (b*f - e*d) / tmp
#         cal_y = (e*c - a*f) / tmp
#         return (cal_x, cal_y)
        
#     else:
#         return (1.1, 1.1)


# line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
# solution(line)

# 2. 행렬 테두리 회전하기
# 2023-10-09 -> WRONG (2차원 배열을 시계 방향으로 돌리는 문제 처음 만나봄 -> rotating skill 배움)

def solution(rows, columns, queries):
    answer = []

    grid = [[(i) * columns + (j + 1) for j in range(columns)] for i in range(rows)]
    
    for i in range(len(queries)):
        answer.append(rotate(queries[i], grid))



    return answer  

def rotate(query, grid):
    x1, y1, x2, y2 = query[0], query[1],query[2],query[3]
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
    first = grid[x1][y1]
    min_value = first
    
    # 왼쪽
    for i in range(x1, x2):
        grid[i][y1] = grid[i+1][y1]
        min_value = min(min_value, grid[i+1][y1])
    
    #아래
    for i in range(y1, y2):
        grid[x2][i] = grid[x2][i+1]
        min_value = min(min_value, grid[x2][i+1])

    #오른쪽
    for i in range(x2, x1,-1):
        grid[i][y2] = grid[i-1][y2]
        min_value = min(min_value, grid[i-1][y2])

    #위
    for i in range(y2, y1+1, -1):
        grid[x1][i] = grid[x1][i-1]
        min_value = min(min_value, grid[x1][i-1])

    grid[x1][y1+1] = first
    return min_value

answer = solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]])
print(answer)