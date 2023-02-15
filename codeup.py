# 4013 : 진법 변환
"""
num = input()
num = int(num)
print(2, format(num,'b'))
print(8, format(num,'o'))
print(16, format(num,'X'))
"""

# 4026 : 중앙값
"""
num_list = list(map(int, input().split()))
num_list.sort()
print(num_list[int(5/2)])
"""

# 4031 : 가장 큰 수
"""
num_list = list(map(int, input().split()))
num_list.sort()
even = []; odd = []
for data in num_list:
    if data % 2 == 0:
        even.append(data)
    else:
        odd.append(data)

if len(even) == 0:
    print(odd[6])
elif len(odd) == 0:
    print(even[6])
else:
    print(odd[len(odd)-1] + even[len(even)-1]) 
"""

# 4036 : 합과 차
"""
n = int(input())
m = int(input())
print(int((n+m)/2))
print(int((n-m)/2))
"""

# 4041 : 숫자 다루기
"""
n = input()
print(int(n[::-1]))
sum = 0
for c in n:
    sum += int(c)
print(sum)
"""

# 4051 : 시간외 근무 수당
"""
time = []
sum = 0
for i in range(5):
    x, y = map(float, input().split())
    time.append(x); time.append(y)


for i in range(0,10,2):
    tmp = time[i+1] - time[i]
    if tmp >= 5:
        sum += 4
    elif tmp >= 1:
        sum += (tmp -1)
    

if sum <= 5.0:
    sum *= 10000
    sum *= 1.05
elif sum >= 15.0:
    sum *= 10000
    sum *= 0.95
else:
    sum *= 10000
print(int(sum))
"""

# 4056 : 연말 정산
"""
num = int(input())

if num <= 500:
    num = num*0.7
elif num <= 1500:
    num = 350 + (num -500) * 0.4
elif num <= 4500:
    num = (750 + (num - 1500) * 0.15)
elif num <= 10000:
    num = (1200 + (num - 4500) * 0.05)
else:
    num = (1475 + (num - 10000) * 0.02)

print(int(num))
"""

# 4501 : 백설공주와 난장이
"""
height = []
for i in range(7):
    height.append(int(input()))
height.sort()
len = len(height)
print(height[len-1])
print(height[len-2])
"""

# 4506 : 최대공약수와 최소공배수
"""
import math 
a, b = map(int, input().split())
print(math.gcd(a,b))
print(math.lcm(a,b))
"""

