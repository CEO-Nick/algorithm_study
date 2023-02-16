# Chapter 3. Greedy

# 1. 거스름돈
"""
n = int(input())
coin_size = [500, 100, 50, 10]
count = 0
for coin in coin_size:
    count += n // coin
    n %= coin
print(count)
"""

# 2. 큰 수의 법칙
# 내 알고리즘
"""
N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))
sum = 0
numbers.sort()
first = numbers[N-1]
second = numbers[N-2]   

for i in range(M):
    if i % (K+1) == K:
        sum += second
    else:
        sum += first
print(sum)
"""

# 교재 - 1
"""
while True:
    for i in range(K):
        if M == 0:
            break
        sum += first
        M -= 1
    if M == 0:
        break
    sum += second
    M -= 1
print(sum)
"""

# 교재 - 2
"""
count = int(M/(K+1)) * K
count += M % (K+1)

sum = count * first
sum += (M-count) * second
print(sum)
"""

# 3. 숫자 카드 게임
# 내 알고리즘 : 너무 단순하고 중복되는 부분이 많음, 메모리 낭비도 심한듯
"""
card = []
min_list = []

n, m = map(int, input().split())

for i in range(n):
    card.append(list(map(int, input().split())))

for i in range(n):
    min = card[i][0]
    for j in range(m):
        if min > card[i][j]:
            min = card[i][j]
    min_list.append(min)

max = min_list[0]
for i in range(1, n):
    if max < min_list[i]:
        max = min_list[i]
print(max)
"""

# 교재 - min() 함수 사용, 현재 줄에서 가장 작은 값 구하고 바로 기존의 최댓값과 비교후 최댓값만 유지
"""
n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
print(result)
"""

# 4. 1이 될 때까지
# 내 알고리즘 
"""
n, k = map(int, input().split())
count = 0
while n!= 1:
    if n % k == 0:
        n = n//k
        count += 1
    else:
        n -= 1
        count += 1
print(count)
"""

## 백준 그리디
    # 11047 : 동전 0
"""
n, k = map(int, input().split())
coins = []
result = 0
for i in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)

for coin in coins:
    result += k // coin
    k %= coin
print(result)
"""

    # 1026 : 보물
"""
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = 0
while len(A) != 0:
    min_value = min(A)
    max_value = max(B)
    result += min_value * max_value
    A.remove(min_value)
    B.remove(max_value)
print(result)
"""

    # 11399 : ATM
"""
n = int(input())
waiting = list(map(int, input().split()))
waiting.sort()
result = 0
for data in waiting:
    result += (data * n)
    n -= 1
print(result)
"""

    # 1439 : 뒤집기
"""
s = input()
count0 = 0
count1 = 0
isFirst = True
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if isFirst == True:
            count0 += 1
            count1 += 1
            isFirst = False
        else:
            if s[i+1] == '0':
                count0 += 1
            else:
                count1 += 1

print(min(count0,count1))


    # 2847 : 게임을 만든 동준이
n = int(input())
score = []
for i in range(n):
    score.append(int(input()))
len = len(score)
last = score[len-1]
result = 0
for i in range(n-1):
    tmp = last - (n-i-1)
    if tmp < score[i]:
        result += (score[i] - tmp)
print(result)
"""

order = 'a 123'
print(order.split()[1])