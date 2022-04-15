
n, k = map(int, input().split())
result = 0

while True :

    target = (n // k) * k # target을 k로 나누어 떨어지게 설정 즉 k의 배수가 되도록 한다
    result += (n - target) # 배수가 되도록 1을 뺀 값을 결과값에 더해준다
    n = target # n을 target으로 설정한다.

    if n < k :
        break
    result+=1
    n //= k # 나누어진 값의 몫이 새로운 n값이 되도록 설정


print(result)
