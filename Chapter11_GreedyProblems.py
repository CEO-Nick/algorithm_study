# 01. 모험가 길드
# 1354
# 내 생각 : 공포도가 제일 작은 사람을 기준으로 해당 인원만큼 그룹 구성 -> 공포도 작은 순으로 그룹에 넣기
n = int(input())
fears = list(map(int, input().split()))
fears.sort()
count = 0
result = 0
for fear in fears:
    count += 1
    
