# # 5-1
# stack=[]
# stack.append(5)
# stack.append(2)
# stack.append(3)
# stack.append(7)
# stack.pop()
# stack.append(1)
# stack.append(4)
# stack.pop()

# print(stack)
# print(stack[::-1]) # 최상단 원소부터 출력

# # 5-2
# from collections import deque # 파이썬으로 큐를 사용할 때 꼭 활용하자.

# # 큐 구현을 위해 deque 라이브러리 사용
# queue = deque()

# queue.append(5)
# queue.append(2)
# queue.append(3)
# queue.append(7)
# queue.popleft()
# queue.append(1)
# queue.append(4)
# queue.popleft()

# print(queue) # 먼저 들어온 순서대로 출력
# queue.reverse() # 다음 출력을 위해 역순으로 바꾸기
# print(queue) # 나중에 들어온 원소부터 출력

# 5-3

# def recursive_function():
#     print('재귀 함수를 호출합니다.')
#     recursive_function()

# recursive_function()

# 5-4

def recursive_function(i):
    # 100번째 출력했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return
    print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀 함수를 종료합니다.')

recursive_function(1)

# 5-5
# 반복적으로 구현한 n!
def factorial_iterative(n):
    
    result = 1
    for i in range(1, n+1):
        result *= i
    
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    
    if n <= 1:
        return 1

    return n * factorial_recursive(n-1)


print('반복적으로 구현 : ', factorial_iterative(5))
print('재귀적으로 구현 : ', factorial_recursive(5))

