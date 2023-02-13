# 가장 낮은 값 중 가장 큰 값이 존재하는 행의 큰 값을 선택한다.

n, m = map(int, input().split())
# 결과 값을 넣어주는 게 중요하다.
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)

    result = max(result, min_value)
    
print(result)

