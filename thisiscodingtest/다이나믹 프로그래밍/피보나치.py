# 8-1
# 피보나치 함수를 재귀 함수로 표현

def fibo(x):
    if x == 1 or x == 2:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)

print(fibo(4))

# 다이나믹 프로그래밍 조건
# 1. 큰 문제를 작은 문제로 나눌 수 있다.
# 2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일히다.
# 메모이제이션
# 8-2 피보나치 수열 소스코드(재귀적)

# 한 번 계산된 결과를 메모이제션하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo(x):
    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]
    
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    else:
        d[x] = fibo[x-1] + fibo[x-2]
        return d[x]

print(fibo(99))

# 8-4 반복문 사용(바텀업)

d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[n] = d[n-1] + d[n-2]

print(d[n])