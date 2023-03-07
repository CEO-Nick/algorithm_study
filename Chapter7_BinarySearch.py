# Chapter 7. Binary Search

# ex) 순차 탐색
"""
def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1

print('생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.')
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print('앞서 적은 원소 개수만큼 문자열을 입력하세요 구분은 띄어쓰기 한 칸으로 합니다. ')
array = input().split()

print(sequential_search(n,target,array))
"""

# ex) 재귀함수로 구현한 이진 탐색
"""
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid + 1, end)

n, target = map(int, input().split())
array = list(map(int, input().split()))
result = binary_search(array, target, 0, n-1)   
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)
"""

# ex) 반복문으로 구현한 이진 탐색
"""
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n, target = map(int, input().split())
array = list(map(int, input().split()))
result = binary_search(array, target, 0, n-1)   
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)
"""

# ex 한 줄 입력받아 출력하는 코드
"""
import sys
input_data = sys.stdin.readline().rstrip()      # rstrip() 필수!! readline()으로 입력하면 enter도 기호로 입력된다. 이걸 지우기 위해서 필요

print(input_data)
"""

# 2. 부품 찾기
n = int(input())
instock = list(map(int, input().split()))
instock.sort()

m = int(input())
requirement = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid + 1, end)

   

for target in requirement:
    result = binary_search(instock, target, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')


    
