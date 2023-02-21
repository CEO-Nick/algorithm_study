# Chapter 6. Sorting

# ex) 선택 정렬 
"""
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(len(array)):
    min = i
    for j in range(i+1, len(array)):
        if array[min] > array[j]:
            min = j

    # python에서 swap
    array[min], array[i] = array[i], array[min]

print(array)
"""

# ex) 삽입 정렬
"""
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):

    for j in range(i, 0, -1):

        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)
"""

# ex) 퀵 정렬 
"""
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return 
    
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # pivot보다 큰 data 찾을 때까지 left += 1
        while left <= end and array[pivot] >= array[left]:
            left += 1
        # pivot보다 작은 data 찾을 때까지
        while right > start and array[pivot] <= array[right]:
            right -= 1

        # 엇갈렸을 때
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)

def quick_sorting(array):
    if len(array) <=1:
        return array
    
    pivot = array[0]    
    tail = array[1:]    

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sorting(left_side) + [pivot] + quick_sorting(right_side)

print(quick_sorting(array))
"""

# 2. 위에서 아래로
"""
n = int(input())
array = []
for i in range(n):
    array.append(int(input()))
array.sort(reverse=True)

for data in array:
    print(data, end=' ')
"""

# 3. 성적이 낮은 순서로 학생 출력하기
"""
n = int(input())

array = []
for i in range(n):
    tmp = input().split()
    array.append((tmp[0], int(tmp[1])))

array = sorted(array, key = lambda x : x[1])

for data in array:
    print(data[0], end=' ')
"""

# 4. 두 배열의 원소 교체

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort(); b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
    
print(sum(a))
