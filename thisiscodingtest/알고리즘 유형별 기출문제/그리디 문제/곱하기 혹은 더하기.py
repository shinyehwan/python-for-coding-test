# 핵심 : 두 수 중 하나라도 1이거나 0이면 전값에 더해주고 두 수가 모두 2보다 큰 경우 곱해준다.
data = list(map(int, input()))


# 결과값에 대한 조건문을 안적어줬다.
result = 0
for i in data:
    if i <= 1 or result <= 1:
        result += i
    else :
         result *= i

print(result)
