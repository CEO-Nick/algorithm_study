# 알고리즘 기초 1/2	200 - 자료구조 1
    # 10828 스택
"""
stack = []

def empty():
    global stack
    if len(stack) == 0:
        return 1
    else:
        return 0
    
def pop():
    global stack
    if empty():
        return (-1)
    else:
        tmp = stack[-1]
        del stack[-1]
        return tmp
    
def push(data):
    global stack
    stack.append(data)

def size():
    global stack
    return (len(stack))

def top():
    if empty():
        return -1
    else:
        return (stack[-1])

result = []
n = int(input())
while n != 0:
    order = input()
    if 'push' in order:
        push(int(order.split()[1]))
    elif 'pop' in order:
        result.append(pop())
    elif 'top' in order:
        result.append(top())
    elif 'empty' in order:
        if empty() == 1:
            result.append(1)
        else:
            result.append(0)
    elif 'size' in order:
        result.append(size())
    n -= 1
for data in result:
    print(data)
"""

    # 9093 단어 뒤집기
"""
n = int(input())
sentences = []
for i in range(n):
    sentences.append(input())

for sentence in sentences:
    tmp = sentence.split()
    for c in tmp:
        print(c[::-1],end=' ')
    print()
"""

    # 9012 괄호
n = int(input())

result = []
while n != 0:
    status = 0  
    flag = 1
    ps = input()

    for c in ps:
        if c == '(':
            status += 1
        else:
            status -= 1
        if status < 0:  # 괄호가 열리지 않았는데 먼저 닫아버릴 때 status 값이 음수가 된다.
            flag = 1
            break
    
    # 괄호가 열린만큼 닫혔다면 status 값은 0일 것이다. 덜 닫혔으면 양수, 더 닫혔으면 음수가 된다.
    if status == 0:
        result.append('YES')
    else:
        result.append('NO')

    n -= 1

for data in result:
    print(data)