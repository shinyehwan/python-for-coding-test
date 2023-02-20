# 문제 해결 방법
# - 뒤의 숫자를 크게 만든다 괄호를 거기다 넣는다.

# 55-50+40
n = list(map(str, input().split('-')))
num = []
# print(n)

for i in n:
    
    if i.__contains__('+'):
        result = 0
        m = i.split('+')
        for j in m:
            result+=int(j)
    else:
        result = int(n[0])

    num.append(result)

# print(num)

for i in range(1,len(num)):
    num[0] -= num[i]

print(num[0])